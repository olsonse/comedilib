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

import comedi, sys, time
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

command_test_errors = {
  1: 'unsupported trigger in ..._src setting of comedi command, setting zeroed',
  2: '..._src setting not supported by driver',
  3: 'TRIG argument of comedi command outside accepted range',
  4: 'adjusted TRIG argument in comedi command',
  5: 'chanlist not supported by board',
}

def get_subdev_status(dev, subdev):
  flags = comedi.get_subdevice_flags(dev,subdev)
  return comedi.extensions.subdev_flags.to_dict(flags)


def run(device='/dev/comedi0', subdevice=-1, channel=0, trigger=None,
         aref='ground', clock='timer', clock_rate=1000., settling_time_ns=10000,
         n_samples = 1000, output='output.txt'):
  outf = open(output, 'w')

  dev = comedi.open(device)

  # set up the command
  cmd = comedi.cmd()
  aref = arefs[ aref ]
  cmd.chanlist = (c_uint * 1)(CR_PACK(channel, rng=0, aref=aref))
  cmd.chanlist_len = 1
  cmd.flags &= ~comedi.CMDF_WRITE
  if subdevice < 0:
    subdevice = comedi.find_subdevice_by_type(dev, comedi.SUBD_AI, 0)
  cmd.subdev = subdevice
  comedi.set_read_subdevice(dev, cmd.subdev)

  if trigger is None:
    cmd.start_src = comedi.TRIG_NOW
    cmd.start_arg = 0
  else:
    cmd.start_src = comedi.TRIG_EXT
    cmd.start_arg = comedi.CR_EDGE | trigger

  if clock == 'timer':
    cmd.scan_begin_src = comedi.TRIG_TIMER
    cmd.scan_begin_arg = int(1e9 / clock_rate)
  else:
    cmd.scan_begin_src = comedi.TRIG_EXT
    cmd.scan_begin_arg = comedi.CR_EDGE | clock

  cmd.convert_src = comedi.TRIG_TIMER
  cmd.convert_arg = int(settling_time_ns)

  cmd.scan_end_src = comedi.TRIG_COUNT
  cmd.scan_end_arg = 1 # == number of channels

  cmd.stop_src = comedi.TRIG_COUNT
  cmd.stop_arg = n_samples

  # test the command
  i = comedi.cmd.from_buffer_copy(cmd)
  err = comedi.command_test(dev, cmd)
  if err < 0:
    raise RuntimeError('comedi.command_test: {}'
                       .format(comedi.strerror(comedi.errno())))
  if err in [1, 2, 3, 5]:
    if repr(i) != repr(cmd):
      E = 'differences: {}'.format(i.diff(cmd))
    else:
      E = 'no differences ???\n{}'.format(cmd)
    raise RuntimeError(command_test_errors[err] + ':\n\t' + E)

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
    while get_subdev_status(dev, cmd.subdev).busy:
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



def process_args(arglist):
  import argparse

  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    '-f', '--device', default='/dev/comedi0',
    help='path to comedi device file [Default /dev/comedi0]')
  parser.add_argument(
    '-s', '--subdevice', type=int, default=-1,
    help='subdevice for analog input [Default -1].  If <0, find ai subdevice')
  parser.add_argument(
    '-c', '--channel', type=int, default=0,
    help='channel for analog input [Default 0]')
  parser.add_argument('--aref', choices=arefs, default='ground',
    help='reference for analog input [Default ground]')
  parser.add_argument('--trigger', type=str, default=None,
    help='Select trigger [Default: None].  '
         'These can be any item that is reasonable (better know your hardware) '
         'and resolvable using the comedi module namespace.  For example, '
         'NI_PFI(0), TRIGGER_LINE(1), ... are valid for NI devices.')
  parser.add_argument('--clock', type=str, default='timer',
    help='The sample clock source.  Valid values for this option include: '
         '(a) `timer` to indicate that the internal timing circuitry should be '
         'used, (b) any symbolic name for a signal as defined in comedi '
         'library (such as `NI_PFI(1)` or `TRIGGER_LINE(2)`) that evaluates to '
         'a valid clock input, or (c) any numeric value representing a valid '
         'clock input for the particular device. [Default timer]')
  parser.add_argument('--clock_rate', type=float, default=1000.,
    help='Rate of sample clock timer in Hz (if timer is used) [Default 1000]')
  parser.add_argument('--settling_time_ns', type=int, default=10000,
    help='Specify the settling time for each conversion in ns [Default 10000].  '
         'Note that the minimum time used for allowing the ADC to settle is '
         'limited by the actual hardware.  In other words, if you select an '
         'invalid value, a runtime exception will be thrown.')
  parser.add_argument('-N', '--n_samples', type=int, default=1000,
    help='Number of samples to collect [Default 1000]')
  parser.add_argument('-o', '--output', default='output.txt',
    help='Path to output file [Default output.txt]')

  return parser.parse_args(arglist)

def main(arglist):
  O = process_args(arglist)

  try:
    if O.trigger:
      O.trigger = eval(O.trigger, globals(), comedi.__dict__)

    if O.clock != 'timer':
      O.clock = eval(O.clock, globals(), comedi.__dict__)
  except NameError as n:
    print 'Name Error: ', n

  run(**O.__dict__)

if __name__ == '__main__':
  main(sys.argv[1:])
