#!/usr/bin/env python

"""
Asynchronous Analog Input Example
Part of Comedilib

Public domain contributions 2016 Spencer E Olson <olsonse@umich.edu>

This file may be freely modified, distributed, and combined with
other software, as long as proper attribution is given in the
source code.

Requirements: Analog input device capable of asynchronous commands.

Using command line arguments (parsed with argparse module), one can select the
trigger and clock sources, and the number of samples to accumulate.

The point of this example was to show a simple method of reading from an analog
input channel using the mmap data interface.
"""

import comedi
from comedi import CR_PACK, TRIG_EXT
import numpy as np
from ctypes import c_uint, c_ubyte, sizeof
from mmap import mmap, PROT_READ, MAP_SHARED

arefs = dict(
  diff    = comedi.AREF_DIFF,
  common  = comedi.AREF_COMMON,
  ground  = comedi.AREF_GROUND,
  other   = comedi.AREF_OTHER,
)

def get_subdev_status(dev, subdev):
  flags = comedi.get_subdevice_flags(dev,subdev)
  return comedi.extensions.subdev_flags.to_dict(flags)


def main(device='/dev/comedi0', subdevice=-1, channel=0, trigger=None,
         aref='ground', clock='timer', frequency=1000., n_samples = 1000,
         output='output.txt'):
  outf = open(output, 'w')

  dev = comedi.open(device)

  # set up the command
  cmd = comedi.cmd()
  cmd.chanlist = (c_uint * 1)(CR_PACK(channel, rng=0, aref=aref))
  cmd.chanlist_len = 1
  cmd.flags &= ~comedi.CMDF_WRITE
  if subdevice < 0:
    subdevice = comedi.find_subdevice_by_type(dev, comedi.SUBD_AO, 0)
  cmd.subdev = subdevice

  if trigger is None:
    cmd.start_src = comedi.TRIG_NOW
    cmd.start_arg = 0
  else:
    cmd.start_src = comedi.TRIG_EXT
    cmd.start_arg = comedi.CR_EDGE | trigger

  if clock == 'timer':
    cmd.scan_begin_src = comedi.TRIG_TIMER
    cmd.scan_begin_arg = int(1e9 / frequency)
  else:
    cmd.scan_begin_src = comedi.TRIG_EXT
    cmd.scan_begin_arg = comedi.CR_EDGE | clock

  cmd.convert_src = comedi.TRIG_TIMER
  cmd.convert_arg = 1

  cmd.scan_end_src = comedi.TRIG_COUNT
  cmd.scan_end_arg = 1 # == number of channels

  cmd.stop_src = comedi.TRIG_COUNT
  cmd.stop_arg = n_samples

  # test the command
  err = comedi.command_test(dev, cmd)
  if err < 0:
    raise RuntimeError('comedi.command_test: {}'
                       .format(comedi.strerror(comedi.errno())))
  elif err:
    raise RuntimeError('comedi.command_test:  non-zero value {}'.format(err))


  # set up the memory mapping
  # kind of memory we need to map...
  status = get_subdev_status(dev, subdevice)
  sampl_t = comedi.sampl_t if status.sample_16bit else comedi.lsampl_t

  # do the mapping
  size = comedi.get_buffer_size(dev, subdevice)
  mapped = mmap(comedi.fileno(dev), size, prot=PROT_READ, flags=MAP_SHARED,
                offset=0)
  if not mapped:
    raise OSError('mmap: error!') # probably will already be raised
  shape = (n_samples,) # mapping to simple 1-D array
  data = np.ndarray(shape=shape, dtype=sampl_t, buffer=mapped, order='C')



  # initiate command
  err = comedi.command(dev, cmd)
  if err < 0:
    raise RuntimeError('comedi.command: {}'
                       .format(comedi.strerror(comedi.errno())))

  if cmd.start_src != comedi.TRIG_NOW:
    print 'ready for external trigger...'

  # record data until the end...
  try:
    end = begin = 0
    ssize = size / sizeof(sampl_t)
    while get_subdev_status(dev, cmd.subdev).running:
      end += int(comedi.get_buffer_contents(dev,subdevice) / sizeof(sampl_t))

      I, F = int(begin / ssize), int(end / ssize)
      i, f = int(begin % ssize), int(end % ssize)
      if I < F:
        np.savetxt(outf, data[i:ssize])
        i = 0
      if i < f:
        np.savetxt(outf, data[i:f])

      ret = comedi.mark_buffer_read(dev, subdevice,
                                    (end - begin) * sizeof(sampl_t))
      if ret < 0:
        raise "error mark_buffer_read"
      begin = end

      time.sleep(.01)
  except KeyboardInterrupt:
    pass

  # finally, close the device and output file:
  comedi.close(dev)
  outf.close()



if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    '-f', '--device', default='/dev/comedi0', help='path to comedi device file')
  parser.add_argument(
    '-s', '--subdevice', type=int, default=-1,
    help='subdevice for analog input [Default=-1].  If <0, find ai subdevice')
  parser.add_argument(
    '-c', '--channel', type=int, default=0,
    help='channel for analog input')
  parser.add_argument('--aref', choices=arefs, default='ground',
    help='reference for analog input')
  parser.add_argument('--trigger', type=str, default=None,
    help='Select trigger [Default: None].  '
         'These can be any item that is reasonable (better know your hardware) '
         'and resolvable using the comedi module namespace.  For example, '
         'NI_PFI(0), TRIGGER_LINE(1), ... are valid for NI devices.')
  parser.add_argument('--clock', type=str, default='timer', help='[timer]')
  parser.add_argument('--clock_rate', type=float, default=1000., help='[1000.]')
  parser.add_argument('-N', '--n_samples', type=int, default=1000, help='[1000]')
  parser.add_argument('-o', '--output', default='output.txt',
    help='path to output file')

  O = parser.parse_args()

  try:
    if O.trigger:
      O.trigger = eval(O.trigger, globals(), comedi.__dict__)

    if O.clock != 'timer':
      O.clock = eval(O.clock, globals(), comedi.__dict__)
  except NameError as n:
    print 'Name Error: ', n

  main(**O.__dict__)
