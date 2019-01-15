#!/usr/bin/env python

"""
Show some various bits of information about the given comedi device.

Public domain contributions 2016 Spencer E Olson <olsonse@umich.edu>
"""

import comedi

subdevice_types = {
  comedi.SUBD_UNUSED  : "unused",
  comedi.SUBD_AI      : "analog input",
  comedi.SUBD_AO      : "analog output",
  comedi.SUBD_DI      : "digital input",
  comedi.SUBD_DO      : "digital output",
  comedi.SUBD_DIO     : "digital I/O",
  comedi.SUBD_COUNTER : "counter",
  comedi.SUBD_SERIAL  : "serial",
  comedi.SUBD_PWM     : "pulse width modulation",
  comedi.SUBD_TIMER   : "timer",
  comedi.SUBD_MEMORY  : "memory",
  comedi.SUBD_CALIB   : "calibration",
  comedi.SUBD_PROC    : "processor",
}

def main(devfile = '/dev/comedi0'):
  #open a comedi device
  dev = comedi.open(devfile)
  if not dev:
    raise RuntimeError('Error openning Comedi device')

  version_code = comedi.get_version_code(dev)
  if not version_code:
    raise RuntimeError('Error reading version_code')
  print "version code is: ", version_code

  driver_name = comedi.get_driver_name(dev)
  if not driver_name:
    raise RuntimeError('Error reading driver_name')
  print "driver name is: ", driver_name

  board_name = comedi.get_board_name(dev)
  if not board_name:
    raise RuntimeError('Error reading board_name')
  print "board name is: ", board_name

  n_subdevices = comedi.get_n_subdevices(dev)
  if not n_subdevices:
    raise RuntimeError('Error reading n_subdevices')
  print "number of subdevices is: ", n_subdevices

  print "-----subdevice characteristics-----"
  for i in range(n_subdevices):
    print "subdevice %d:" % (i)
    type = comedi.get_subdevice_type(dev,i)
    print "\ttype: %d (%s)" % (type,subdevice_types[type])
    if type == comedi.SUBD_UNUSED:
      continue
    n_chans = comedi.get_n_channels(dev,i)
    print "\tnumber of channels: %d" % ( n_chans)
    if not(comedi.maxdata_is_chan_specific(dev,i)):
        print "\tmax data value: %d" % (comedi.get_maxdata(dev,i,0))
    else:
      print "max data value is channel specific"
      for j in range(n_chans):
        print "\tchan: %d: %d" % (j,comedi.get_maxdata(dev,i,j))
    print "\tranges: "
    if not(comedi.range_is_chan_specific(dev,i)):
      n_ranges = comedi.get_n_ranges(dev,i,0)
      print "\t\tall chans:"
      for j in range(n_ranges):
        rng = comedi.get_range(dev,i,0,j).contents
        print "\t\t[%g,%g]" % (rng.min, rng.max)
    else:
      for chan in range(n_chans):
        n_ranges = comedi.get_n_ranges(dev,i,chan)
        print "\t\tchan: %d" % (chan)
        for j in range(n_ranges):
          rng = comedi.get_range(dev,i,chan,j).contents
          print "\t\t[%g,%g]" % (rng.min, rng.max)
    print "\tcommand:"
    get_command_stuff(dev,i)



def comedi_get_cmd_fast_1chan(dev,s,cmd):
  ret = comedi.get_cmd_src_mask(dev,s,cmd)
  if ret<0:
    return ret
  cmd.chanlist_len = 1
  cmd.scan_end_src = comedi.TRIG_COUNT
  cmd.scan_end_arg = 1
  if cmd.convert_src & comedi.TRIG_TIMER:
    if cmd.scan_begin_src & comedi.TRIG_FOLLOW:
      cmd.convert_src=comedi.TRIG_TIMER
      cmd.scan_begin=comedi.TRIG_FOLLOW
    else:
      cmd.convert_src=comedi.TRIG_TIMER
      cmd.scan_begin=comedi.TRIG_TIMER
  else:
    print "can't do timed!?!"
    return -1
  if cmd.stop_src & comedi.TRIG_COUNT:
    cmd.stop_src=comedi.TRIG_COUNT
    cmd.stop_arg=2
  elif cmd.stop_src & comedi.TRIG_NONE:
    cmd.stop_src=comedi.TRING_NONE
    cmd.stop_arg=0
  else:
    print "can't find a good stop_src"
    return -1
  ret = comedi.command_test(dev,cmd)
  if ret==3:
    ret = comedi.command_test(dev,cmd)
  if ret==4 or ret==0:
    return 0
  return -1

def probe_max_1chan(dev,s):
  buf=""
  cmd=comedi.cmd()
  print "\tcommand fast 1chan:"
  if comedi.get_cmd_generic_timed(dev,s,cmd,1,1) < 0:
    print "\t\tnot supported"
  else:
    print "\tstart: %s %d" % (cmd_src(cmd.start_src,buf),cmd.start_arg)
    print "\tscan_begin: %s %d" % (cmd_src(cmd.scan_begin_src,buf),cmd.scan_begin_arg)
    print "\tconvert begin: %s %d" % (cmd_src(cmd.convert_src,buf),cmd.convert_arg)
    print "\tscan_end: %s %d" % (cmd_src(cmd.scan_end_src,buf),cmd.scan_end_arg)
    print "\tstop: %s %d" % (cmd_src(cmd.stop_src,buf),cmd.stop_arg)

def cmd_src(src,buf):
  buf=""
  if src & comedi.TRIG_NONE:    buf=buf+"none|"
  if src & comedi.TRIG_NOW:     buf=buf+"now|"
  if src & comedi.TRIG_FOLLOW:  buf=buf+"follow|"
  if src & comedi.TRIG_TIME:    buf=buf+"time|"
  if src & comedi.TRIG_TIMER:   buf=buf+"timer|"
  if src & comedi.TRIG_COUNT:   buf=buf+"count|"
  if src & comedi.TRIG_EXT:     buf=buf+"ext|"
  if src & comedi.TRIG_INT:     buf=buf+"int|"
  if len(buf)==0:
    print "unknown"
  else:
    buf = buf[:-1] # trim trailing "|"
    return buf

def get_command_stuff(dev,s):
  buf = ""
  cmd = comedi.cmd()
  if comedi.get_cmd_src_mask(dev,s,cmd) < 0:
    print "\tnot supported"
  else:
    print "\tstart: %s" % (cmd_src(cmd.start_src,buf))
    print "\tscan_begin: %s" % (cmd_src(cmd.scan_begin_src,buf))
    print "\tconvert begin: %s" % (cmd_src(cmd.convert_src,buf))
    print "\tscan_end: %s" % (cmd_src(cmd.scan_end_src,buf))
    print "\tstop: %s" % (cmd_src(cmd.stop_src,buf))
    probe_max_1chan(dev,s)



if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('--devfile', type=str, default='/dev/comedi0',
    help='Select the comedi device file [Default /dev/comedi0]')
  O = parser.parse_args()
  try:
    main(O.devfile)
  except RuntimeError, e:
    print('error: {}'.format(e))
