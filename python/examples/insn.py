#!/usr/bin/env python
#
# Copyright (C) Mar 2012  W. Trevor King <wking@drexel.edu>
# Public Domain contributions Spencer E. Olson <olsonse@umich.edu>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
This example does 3 instructions in one system call.  It does a
`gettimeofday()` call, then reads `N_SAMPLES` samples from an analog
input, and the another `gettimeofday()` call.
"""

import comedi, sys
from ctypes import c_uint32


arefs = dict(
  diff    = comedi.AREF_DIFF,
  common  = comedi.AREF_COMMON,
  ground  = comedi.AREF_GROUND,
  other   = comedi.AREF_OTHER,
)

def get_subdev_status(dev, subdev):
  flags = comedi.get_subdevice_flags(dev,subdev)
  return comedi.extensions.subdev_flags.to_dict(flags)


def setup_gtod_insn(insn):
  insn.insn = comedi.INSN_GTOD
  insn.subdev = 0
  insn.chanspec = 0
  insn.n = 2
  # allocate; this data is "owned" by this instruction
  insn.data = (c_uint32 * 2)(0,0)

def get_time(insn):
  assert insn.insn == comedi.INSN_GTOD, 'expect GTOD instuction'
  assert insn.n == 2, 'exepct data length == 2 for GTOD'
  seconds       = insn.data[0]
  microseconds  = insn.data[1]
  return seconds + microseconds/1e6

def setup_read_insn(dev, subdev, chan, range, aref, n_scan, insn):
  """
  Sets up a read instruction where `n_scan` samples are taken sequentially, but
  not necessarily following any particular timing pattern.
  """
  aref = arefs[aref]
  insn.insn = comedi.INSN_READ
  insn.n = n_scan
  insn.data = (c_uint32 * n_scan)() # always 32bit in insn regardless of sampl_t
  insn.subdev = subdev
  insn.chanspec = comedi.CR_PACK(chan, range, aref)


def run(args):
  dev = comedi.open(args.filename)
  if not dev:
    raise RuntimeError('error opening Comedi device {}'.format(args.filename))

  if args.ai_subdev < 0:
    args.ai_subdev = comedi.find_subdevice_by_type(dev, comedi.SUBD_AI, 0)

  # get comedi.to_phys piceces to convert from raw data to physical voltages
  status = get_subdev_status(dev, args.ai_subdev)
  rng = comedi.get_range(dev, args.ai_subdev, args.ai_chan, args.ai_range)
  maxdata = (1<<16 if status.sample_16bit else 1<<32) - 1

  # prepare the instructions
  insns = comedi.insnlist()
  insns.set_length(3)
  setup_gtod_insn(insns[0])
  setup_read_insn(dev, args.ai_subdev, args.ai_chan, args.ai_range, args.ai_ref,
                  args.ai_scans, insns[1])
  setup_gtod_insn(insns[2])

  # execute
  ret = comedi.do_insnlist(dev, insns)
  if ret != insns.n_insns:
    raise RuntimeError('error running instructions ({})'.format(ret))

  t1 = get_time(insns[0])
  t2 = get_time(insns[2])
  print('initial time: {} s'.format(t1))
  print('final time:   {} s'.format(t2))
  print('difference:   {} s'.format(t2-t1))

  to_out = lambda data : comedi.to_phys(data, rng, maxdata)
  if args.raw:
    to_out = lambda data : data

  print('data (in Volts):')
  for i in range(insns[1].n):
    print('\t', to_out(insns[1].data[i]))

  # we don't need the device anymore
  # we close this last so we don't invalidate rng contents
  ret = comedi.close(dev)
  if ret != 0:
    raise RuntimeError('error closing Comedi device {} ({})'
                       .format(args.filename, ret))


def process_args(arglist):
  import argparse

  def check_nscans(val):
    val = int(val)
    if val <= 0 or val > 1000:
      raise argparse.ArgumentTypeError('invalid reasonable number of scans')
    return val

  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    '-f', '--filename', default='/dev/comedi0',
    help='path to comedi device file [Default /dev/comedi0]')
  parser.add_argument(
    '-s', '--subdevice', type=int, default=-1, dest='ai_subdev',
    help='subdevice for analog input [Default -1].  If <0, find ai subdevice')
  parser.add_argument(
    '-c', '--channel', type=int, default=0, dest='ai_chan',
    help='channel for analog input [Default 0]')
  parser.add_argument(
    '-a', '--analog-reference', default='ground', dest='ai_ref',
    choices=arefs.keys(), help='reference for analog input [Default ground]')
  parser.add_argument(
    '-r', '--range', type=int, default=0, dest='ai_range',
    help='range index for analog input (use info.py to find all ranges) '
         '[Default 0]')
  parser.add_argument(
    '-N', '--num-scans', type=check_nscans, default=10, dest='ai_scans',
    help='number of analog input scans (select 1..1000) [Default 10]')
  parser.add_argument(
    '--raw', action='store_true', help='Give output in raw integer values')

  return parser.parse_args(arglist)

def main(arglist):
  args = process_args(arglist)
  try:
    run(args)
  except RuntimeError, e:
    print('error: {}'.format(e))

if __name__ == '__main__':
  main(sys.argv[1:])
