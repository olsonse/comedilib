#!/usr/bin/env python

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

import comedi
from comedi import CR_PACK, TRIG_EXT
from ctypes import c_uint

import numpy as np
import argparse

def get_subdev_status(dev, subdev):
  flags = comedi.get_subdevice_flags(dev,subdev)
  return comedi.extensions.subdev_flags.to_dict(flags)


def main(trigger=None, clock='timer', frequency=1000., continuous=True,
         samples_per_channel = 1000):
  dev = comedi.open('/dev/comedi1')

  cmd = comedi.cmd()
  # only channel 0
  cmd.chanlist = (c_uint * 1)(CR_PACK(0, rng=0, aref=comedi.AREF_GROUND))
  cmd.chanlist_len = 1
  cmd.flags = comedi.CMDF_WRITE
  cmd.subdev = comedi.find_subdevice_by_type(dev, comedi.SUBD_AO, 0)

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

  cmd.scan_end_src = comedi.TRIG_COUNT
  cmd.scan_end_arg = 1 # == number of channels

  cmd.stop_src = comedi.TRIG_NONE if continuous else comedi.TRIG_COUNT
  cmd.stop_arg = samples_per_channel

  # test the command
  err = comedi.command_test(dev, cmd)
  if err < 0:
    comedi.perror("comedi.command_test")
    raise RuntimeError()
  elif err:
    raise RuntimeError('comedi.command_test:  non-zero value {}'.format(err))

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
  buf = (c_ubyte * samples_per_channel).from_buffer(data)
  os.write(comedi.fileno(dev), buf)

  # trigger the command start
  if cmd.start_src == TRIG_INT:
    ret = comedi.internal_trigger(dev, cmd.subdev, 0)
    if ret < 0:
      comedi.perror('comedi.internal_trigger error')
      raise OSError('comedi.internal_trigger error: ')
  else:
    print 'ready for external trigger...'

  # wait for end
  try:
    while get_subdev_status(dev, cmd.subdev).running:
      time.sleep(.2)
  except KeyboardInterrupt:
    pass

  # finally, close the device:
  comedi.close(dev)


def generate_data(samples_per_channel, num_channels, sampl_t, mx=4*np.pi):
  shape = ( self.samples_per_channel, len(options.channels) )
  data = np.zeros( shape, dtype=sampl_t )
  t = np.r_[0:mx:1j*samples_per_channel]
  for i in xrange(num_channels):
    data[:,i] = np.sin(t + .1 * i)
  return data


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('--trigger', type=str, default=None,
    help='Select trigger [Default: None].  '
         'These can be any item that is reasonable (better know your hardware) '
         'and resolvable using the comedi module namespace.  For example, '
         'NI_PFI(0), TRIGGER_LINE(1), ... are valid for NI devices.')
  parser.add_argument('--clock', type=str, default='timer', help='[timer]')
  parser.add_argument('--clock_rate', type=float, default=1000., help='[1000.]')
  parser.add_argument('--continuous', action='store_true', help='[False]')
  parser.add_argument('--waveform_len', type=int, default=1000, help='[1000]')

  O = parser.parse_args()

  try:
    if O.trigger:
      O.trigger = eval(O.trigger, globals(), comedi.__dict__)

    if O.clock != 'timer':
      O.clock = eval(O.clock, globals(), comedi.__dict__)
  except NameError as n:
    print 'Name Error: ', n

  main(O.trigger, O.clock, O.clock_rate, O.continuous, O.waveform_len)
