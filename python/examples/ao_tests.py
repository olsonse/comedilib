#!/usr/bin/env python3

"""
Asynchronous Analog Output Example
Part of Comedilib

Public domain contributions 2016 Spencer E Olson <olsonse@umich.edu>

This file may be freely modified, distributed, and combined with
other software, as long as proper attribution is given in the
source code.

Requirements: Analog output device capable of asynchronous commands.

This demo simply writes a sine wave (2*cycles) onto channel 0.  Using command
line arguments (parsed with argparse module), one can select the trigger and
clock sources, whether the output is generated continuously, and the number of
points in the sine wave.

The point of this example was to show a simple method of writing to an analog
output channel using the os.write data interface.
"""

import os, sys, time
import comedi
from comedi import CR_PACK
from ctypes import c_uint, c_ubyte, sizeof

import numpy as np
import argparse

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


def run(device='/dev/comedi0', trigger=None, clock='timer',
        frequency=1000., continuous=True,
        samples_per_channel = 1000):
  dev = comedi.open(device)

  cmd = comedi.cmd()
  # only channel 0
  cmd.chanlist = (c_uint * 1)(CR_PACK(0, rng=0, aref=comedi.AREF_GROUND))
  cmd.chanlist_len = 1
  cmd.flags = comedi.CMDF_WRITE
  cmd.subdev = comedi.find_subdevice_by_type(dev, comedi.SUBD_AO, 0)
  comedi.set_write_subdevice(dev, cmd.subdev)

  if trigger is None:
    cmd.start_src = comedi.TRIG_INT
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

  cmd.convert_src = comedi.TRIG_NOW
  cmd.convert_arg = 0

  cmd.scan_end_src = comedi.TRIG_COUNT
  cmd.scan_end_arg = 1 # == number of channels

  cmd.stop_src = comedi.TRIG_NONE if continuous else comedi.TRIG_COUNT
  cmd.stop_arg = samples_per_channel

  # test the command
  i = comedi.cmd.from_buffer_copy(cmd)
  err = comedi.command_test(dev, cmd)
  if err < 0:
    comedi.perror("comedi.command_test")
    raise RuntimeError()
  if err in [1, 2, 3, 5]:
    if repr(i) != repr(cmd):
      E = 'differences: {}'.format(i.diff(cmd))
    else:
      E = 'no differences ???\n{}'.format(cmd)
    raise RuntimeError(command_test_errors[err] + ':\n\t' + E)

  # initiate command
  err = comedi.command(dev, cmd)
  if err < 0:
    comedi.perror("comedi.command")
    raise RuntimeError()


  # generate the data
  status = get_subdev_status(dev, cmd.subdev)
  sampl_t = comedi.sampl_t if status.sample_16bit else comedi.lsampl_t
  data = generate_data(samples_per_channel, num_channels=1, sampl_t=sampl_t)

  # and finally write the data
  buf = (c_ubyte * (sizeof(sampl_t) * samples_per_channel)).from_buffer(data)
  L = os.write(comedi.fileno(dev), buf)
  if L != len(buf):
    raise OSError('could only write {} out of {} bytes'.format(L, len(buf)))

  # trigger the command start
  if cmd.start_src == comedi.TRIG_INT:
    ret = comedi.internal_trigger(dev, cmd.subdev, 0)
    if ret < 0:
      comedi.perror('comedi.internal_trigger error')
      raise OSError('comedi.internal_trigger error: ')
  else:
    print('ready for external trigger...')

  # wait for end
  try:
    while get_subdev_status(dev, cmd.subdev).running:
      time.sleep(.2)
  except KeyboardInterrupt:
    pass

  # finally, close the device:
  comedi.cancel(dev, cmd.subdev)
  comedi.close(dev)


def generate_data(samples_per_channel, num_channels, sampl_t, mx=4*np.pi):
  shape = ( samples_per_channel, num_channels )
  data = np.zeros( shape, dtype=sampl_t )
  t = np.r_[0:mx:1j*samples_per_channel]
  for i in range(num_channels):
    data[:,i] = np.sin(t + .1 * i)
  return data


def process_args(arglist):
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument( '-f', '--filename', nargs='?', default='/dev/comedi0',
    help='Comedi device file [Default /dev/comedi0]' )
  parser.add_argument('--trigger', type=str, default=None,
    help='Select trigger [Default None].  '
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
  parser.add_argument('--continuous', action='store_true', help='[False]',
    help='Select continuous operation')
  parser.add_argument('--waveform_len', type=int, default=1000,
    help='Specify the number of samples of the sinusoid for the output '
         '[Default 1000]')

  return parser.parse_args(arglist)

def main(arglist):
  O = process_args(arglist)

  try:
    if O.trigger:
      O.trigger = eval(O.trigger, globals(), comedi.__dict__)

    if O.clock != 'timer':
      O.clock = eval(O.clock, globals(), comedi.__dict__)
  except NameError as n:
    print('Name Error: ', n)

  run(O.filename, O.trigger, O.clock, O.clock_rate, O.continuous,
      O.waveform_len)

if __name__ == '__main__':
  main(sys.argv[1:])
