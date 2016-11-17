#!/usr/bin/env python

"""
Asynchronous Analog Output Example
Part of Comedilib

Copyright (c) 1999,2000 David A. Schleef <ds@schleef.org>
Public domain contributions 2016 Spencer E Olson <olsonse@umich.edu>

This file may be freely modified, distributed, and combined with
other software, as long as proper attribution is given in the
source code.



Requirements: Analog output device capable of asynchronous commands.

This demo uses an analog output subdevice with an asynchronous command to
generate a waveform.  The default waveform is a sine wave (surprise!).  Other
waveforms include ramp_up, ramp_down, triangle, square, cycloid, and blancmange.
Various output options, including the output waveform, may be selected using
command line arguments (parsed with the argparse module).

The DDS portion of this code was ported from David Schleef's c-code example.

The function generation algorithm is the same as what is typically used in
digital function generators.  A 32-bit accumulator is incremented by a phase
factor, which is the amount (in radians) that the generator advances each time
step.  The accumulator is then shifted right by 20 bits, to get a 12 bit offset
into a lookup table.  The value in the lookup table at that offset is then put
into a buffer for output to the DAC.

[ Actually, the accumulator is only 26 bits, for some reason.  I'll fix this
sometime. ]
"""

import os, sys, time
from os import path
sys.path.append( path.join( path.dirname(__file__), path.pardir ) )

import comedi
import numpy as np
from ctypes import c_uint, c_ubyte, sizeof
from mmap import mmap, PROT_WRITE, MAP_SHARED
from itertools import izip

import argparse


arefs = dict(
  common = comedi.AREF_COMMON,
  ground = comedi.AREF_GROUND,
)


class Test(object):
  #/* peak-to-peak amplitude, in DAC units (i.e., 0-4095) */
  amplitude    = 4000

  #/* offset, in DAC units */
  offset      = 2048


  def __init__(self, options):
    self.options = options
    self.cmd = comedi.cmd()
    self.chanlist = ( c_uint * 16 )()

    #/* Use extra to select waveform */
    fn = options.waveform
    if fn < 0 or fn >= len( dds_list ):
      print "Use the option '-w' to select another waveform."
      fn = 0
    dds_klass = dds_list[fn]

    options.waveform_freq = float( options.waveform_freq )
    options.freq = float( options.freq )

    self.dev = comedi.open(options.filename)
    if not self.dev:
      raise OSError( "error opening " + options.filename )


    if options.subdevice < 0:
      options.subdevice = \
        comedi.find_subdevice_by_type(self.dev, comedi.SUBD_AO, 0)

    # ret = comedi.reset( self.dev, options.subdevice )
    # if ret < 0:
    #   comedi.perror('comedi.reset')
    #   raise OSError('comedi.reset failed')


    self.subdevice_flags = \
      comedi.get_subdevice_flags(self.dev, options.subdevice)
    self.sampl_t = comedi.sampl_t
    if self.subdevice_flags & comedi.SDF_LSAMPL:
      self.sampl_t = comedi.lsampl_t

    assert not (self.subdevice_flags & comedi.SDF_FLAGS), 'flags per channel!'
    assert not (self.subdevice_flags & comedi.SDF_MAXDATA), 'maxdata per channel!'
    assert not (self.subdevice_flags & comedi.SDF_RANGETYPE), 'range per channel!'

    maxdata = comedi.get_maxdata(self.dev, options.subdevice, options.channels[0])
    rng = comedi.get_range(self.dev, options.subdevice, options.channels[0], options.range)

    self.offset = float( comedi.from_phys(0.0, rng, maxdata) )
    self.amplitude = float( comedi.from_phys(1.0, rng, maxdata) ) - self.offset

    #memset(&self.cmd,0,sizeof(self.cmd));
    self.cmd.subdev = options.subdevice
    self.cmd.flags = comedi.CMDF_WRITE
    self.cmd.start_src = comedi.TRIG_INT
    self.cmd.start_arg = 0
    if self.options.update_source == 'timer':
      self.cmd.scan_begin_src = comedi.TRIG_TIMER
      self.cmd.scan_begin_arg = int(1e9 / options.freq)
    else:
      self.cmd.scan_begin_src = comedi.TRIG_EXT
      arg = eval(self.options.update_source, globals(), comedi.__dict__)
      self.cmd.scan_begin_arg = comedi.CR_EDGE | arg

    self.cmd.convert_src = comedi.TRIG_NOW
    self.cmd.convert_arg = 0
    self.cmd.scan_end_src = comedi.TRIG_COUNT
    self.cmd.scan_end_arg = len(options.channels)
    self.cmd.stop_src = comedi.TRIG_NONE if options.continuous else comedi.TRIG_COUNT
    self.cmd.stop_arg = 0

    self.cmd.chanlist = self.chanlist
    self.cmd.chanlist_len = len(options.channels)

    aref = arefs[ options.aref ]
    for i,c in izip( xrange(len(options.channels)), options.channels ):
      self.chanlist[i] = comedi.CR_PACK(c, options.range, aref)
  
    self.dds = dds_klass(
      self.amplitude, self.offset, options.waveform_freq, options.freq, options.waveform_len )

    if options.verbose:
      print 'cmd: ', self.cmd

    err = comedi.command_test(self.dev, self.cmd)
    if err < 0:
      comedi.perror("comedi.command_test")
      raise RuntimeError()

    err = comedi.command_test(self.dev, self.cmd)
    if err < 0:
      comedi.perror("comedi.command_test")
      raise RuntimeError()

    if err:
      raise RuntimeError('Comedi Test returns: ' + str(err))

    size = comedi.get_buffer_size( self.dev, options.subdevice )
    if options.verbose:
      print "buffer size is:", size

    # the following two integer projections are really unecessary, at least for
    # python 2.7, but are still written for clarity.  Probably necessar for
    # python3
    self.samples_per_channel \
      = int( int(size / sizeof(self.sampl_t)) / len(options.channels) )

    if options.n_samples:
      if options.n_samples > self.samples_per_channel:
        raise RuntimeError('Not enough memory for requested n_samples')
      self.samples_per_channel = options.n_samples

    self.cmd.stop_arg = self.samples_per_channel

    shape = ( self.samples_per_channel, len(options.channels) )
    if self.options.verbose:
      print 'shape: ', shape

    #print 'BUF_LEN, samples_per_channel, n_chan, shape: ', \
    #  self.BUF_LEN, self.samples_per_channel, len(options.channels), shape

    if options.oswrite:
      self.data = np.zeros( shape, dtype=self.sampl_t )

      def write_data( data, n ):
        buf = ( c_ubyte * n ).from_buffer( data )
        m = os.write( comedi.fileno(self.dev), buf )
        if self.options.verbose:
          print "wrote {} out of {}".format(m, n)
        if m < 0:
          raise OSError('os write error')
        return m

    else:
      # The c version; we can cast directly
      #data = mmap(NULL, size, PROT_WRITE, MAP_SHARED, fileno(dev), 0)

      # the python version;  we must cast using ctypes
      self.mapped = mmap(comedi.fileno(self.dev), size, prot=PROT_WRITE, flags=MAP_SHARED, offset=0)
      if not self.mapped:
        raise OSError( 'mmap: error!' ) # probably will already be raised
      self.data = np.ndarray( shape=shape, dtype=self.sampl_t,
                              buffer=self.mapped, order='C' )
      self.data[:] = 0

      def write_data( data, n ):
        m = comedi.mark_buffer_written(self.dev, options.subdevice, n)
        if self.options.verbose:
          print "Marked {} out of {}".format(m, n)
        if m < 0:
          comedi.perror("comedi.mark_buffer_written")
          raise OSError('mark_buffer error')
        return m

    self.write_data = write_data


  def close(self):
    if hasattr( self, 'dev' ):
      if self.options.verbose:
        print 'closing comedi driver...'
      del self.data
      if not self.options.oswrite:
        self.mapped.close()
        del self.mapped
      comedi.close(self.dev)
      del self.dev

  def __del__(self):
    self.close()


  @property
  def output_size(self):
    return ( self.samples_per_channel
           * len(self.options.channels)
           * sizeof(self.sampl_t) )

  def trigger(self):
    ret = comedi.internal_trigger(self.dev, self.options.subdevice, 0)
    if ret < 0:
      comedi.perror('comedi.internal_trigger error')
      raise OSError('comedi.internal_trigger error: ')

  def _dds(self):
    for i in xrange( len(self.options.channels) ):
      self.dds(self.data[:,i], self.samples_per_channel)

  def start(self):
    """
    Start the waveform
    """
    if self.options.verbose:
      print 'cmd: ', self.cmd
    err = comedi.command(self.dev, self.cmd)
    if err < 0:
      comedi.perror("comedi.command");
      return 1

    self._dds()
    if self.options.show_waveform:
      import pylab
      for i in xrange( len(self.options.channels) ):
        pylab.plot( self.data[:,i] )
      pylab.show()

    n = self.output_size
    m = self.write_data( self.data, n )
    if m < n:
      print "failed to preload output buffer with", n, "bytes, is it too small?"
      print "See the --write-buffer option of comedi_config"
      raise OSError('--write-buffer ?')

    if self.options.verbose:
      print "m=",m

    self.trigger()

  @property
  def status(self):
    self.subdevice_flags = \
      comedi.get_subdevice_flags(self.dev, self.options.subdevice)
    return comedi.extensions.subdev_flags.to_dict( self.subdevice_flags )

  def wait(self):
    """
    wait while the waveform executes
    """
    try:
      if not self.options.write_more:
        while self.status.running:
          time.sleep(1)
      elif self.options.oswrite:
        # FIXME: this is not quite generic for both enough yet.  Need to call
        #   comedi.get_buffer_contents also.
        total = 0
        while True:
          self._dds()
          N = n = self.output_size
          while n>0:
            next_chunk = self.data[(N-n):]
            m=self.write_data(next_chunk,n)
            if self.options.verbose:
              print "m=",m
            n-=m
          total+=self.samples_per_channel
          #print 'total: ', total
      else:
        while True:
          N = n = self.output_size
          unmarked = N - comedi.get_buffer_contents(self.dev, self.options.subdevice)
          if unmarked > 0:
            comedi.mark_buffer_written(self.dev, self.options.subdevice, unmarked)
    except KeyboardInterrupt:
      pass


  def stop(self):
    """
    stop the waveform
    """
    if self.options.verbose:
      self.subdevice_flags = \
        comedi.get_subdevice_flags(self.dev, self.options.subdevice)
      print 'before cancel flags:'
      print comedi.extensions.subdev_flags.to_dict( self.subdevice_flags )

    # now cleanup
    comedi.cancel( self.dev, self.options.subdevice )

    if self.options.verbose:
      self.subdevice_flags = \
        comedi.get_subdevice_flags(self.dev, self.options.subdevice)
      print 'after cancel flags:'
      print comedi.extensions.subdev_flags.to_dict( self.subdevice_flags )




class DDS(object):
  name            = None

  def __init__(self, amplitude, offset, waveform_frequency, update_frequency, waveform_len = 1<<16):
    self.amplitude = amplitude
    self.offset = offset
    self.WAVEFORM_SHIFT = int( round( np.log(waveform_len) / np.log(2) ) )
    self.WAVEFORM_LEN = 1 << self.WAVEFORM_SHIFT
    self.adder = int( waveform_frequency / update_frequency
                      * (1 << 16) * (1 << self.WAVEFORM_SHIFT) )
    self.acc = 0;
    self.waveform = [0] * self.WAVEFORM_LEN
    self.init()

  def __call__(self, buf, n):
    WAVEFORM_MASK   = (self.WAVEFORM_LEN-1)
    for i in xrange( n ):
      buf[i] = int( self.waveform[(self.acc >> 16) & WAVEFORM_MASK] )
      self.acc += self.adder;

  def __str__(self):
    return self.name


class DDS_sine(DDS):
  name = 'sine'
  def init(self):
    ofs = self.offset
    amp = 0.5 * self.amplitude

    if(ofs < amp):
      # Probably a unipolar range.  Bump up the offset.
      ofs = amp
    xt = np.r_[:self.WAVEFORM_LEN] * 2 * np.pi/self.WAVEFORM_LEN
    self.waveform = (ofs + amp*np.cos(xt)).round().astype(int)


def triangle(x):
  """Defined for x in [0,1]"""
  return (1.0 - x) if (x > 0.5) else x


class DDS_pseudocycloid(DDS):
  """
  Yes, I know this is not the proper equation for a cycloid.  Fix it.
  """
  name = 'pseudocycloid'
  def init(self):
    for i in xrange( self.WAVEFORM_LEN/2 ):
      t=2*float(i)/self.WAVEFORM_LEN
      self.waveform[i]=round(self.offset+self.amplitude*np.sqrt(1-4*t*t))
    for i in xrange( self.WAVEFORM_LEN/2, self.WAVEFORM_LEN ):
      t=2*(1-float(i)/self.WAVEFORM_LEN)
      self.waveform[i]=round(self.offset+self.amplitude*np.sqrt(1-t*t))

class DDS_cycloid(DDS):
  name = 'cycloid'
  def init(self):
    SUBSCALE = 2 # Needs to be >= 2.

    i = -1;
    for h in xrange( self.WAVEFORM_LEN* SUBSCALE ):
      t = (h * (2 * np.pi)) / (self.WAVEFORM_LEN * SUBSCALE)
      x = t - np.sin(t)
      ni = int((x * self.WAVEFORM_LEN) / (2 * np.pi))
      if ni > i:
        i = ni
        y = 1 - np.cos(t)
        self.waveform[i] = round(self.offset + (self.amplitude * y / 2))

class DDS_ramp_up(DDS):
  name = 'ramp_up'
  def init(self):
    L = self.WAVEFORM_LEN
    self.waveform = ( self.offset + self.amplitude*np.r_[0:L]/float(L) ).round()

class DDS_ramp_down(DDS):
  name = 'ramp_down'
  def init(self):
    for i in xrange( self.WAVEFORM_LEN ):
      self.waveform[i]=round(self.offset+self.amplitude*float(self.WAVEFORM_LEN-1-i)/self.WAVEFORM_LEN)

class DDS_triangle(DDS):
  name = 'triangle'
  def init(self):
    for i in xrange( self.WAVEFORM_LEN ):
      self.waveform[i] = round(self.offset + self.amplitude * 2 * triangle(float(i) / self.WAVEFORM_LEN))

class DDS_square(DDS):
  name = 'square'
  def init(self):
    for i in xrange( self.WAVEFORM_LEN/2 ):
      self.waveform[i] = round(self.offset)
    for i in xrange( self.WAVEFORM_LEN/2, self.WAVEFORM_LEN ):
      self.waveform[i] = round(self.offset + self.amplitude)

class DDS_blancmange(DDS):
  name = 'blancmange'
  def init(self):
    for i in xrange( self.WAVEFORM_LEN ):
      b = 0;
      for n in xrange( 16 ):
        x = float(i) / self.WAVEFORM_LEN
        x *= (1 << n)
        x -= int(x)
        b += triangle(x) / (1 << n)
      self.waveform[i] = round(self.offset + self.amplitude * 1.5 * b)





dds_list = [
  DDS_sine,
  DDS_ramp_up,
  DDS_ramp_down,
  DDS_triangle,
  DDS_square,
  DDS_cycloid,
  DDS_blancmange,
]


def process_args(arglist):
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument( '-f', '--filename', nargs='?', default='/dev/comedi0',
    help='Comedi device file [Default: /dev/comedi0]' )
  parser.add_argument( '-s', '--subdevice', type=int, default=-1,
    help='Select analog output subdevice [Default:  <first AO>]' )
  parser.add_argument( '-c', '--channels', nargs='+', type=int, default=[0],
    help='Select output channels [Default: [0]]' )
  parser.add_argument( '-a', '--aref',  choices=['ground', 'common'],
    default='ground',
    help='Select analog reference [Default: ground]' )
  parser.add_argument( '-r', '--range', type=int, default=0,
    help='Select analog output range number [Default 0]' )
  parser.add_argument( '-N', '--n_samples', type=int, default=0,
    help='Specify number of output samples per channel [Default 0(all-memory)]' )
  parser.add_argument( '-W', '--waveform_freq', type=float, default=10.0,
    help='set waveform frequency in Hz [default 10.0]' )
  parser.add_argument( '-F', '--freq', type=float, default=1000.,
    help='set update frequency in Hz [default 1000.]' )
  parser.add_argument( '-U', '--update_source',
    default='timer',
    help='Select update signal source [Default: timer].  '
         'By specifying the word `timer`, the internal scan clock is used.  '
         'These can be any item that is reasonable (better know your hardware) '
         'and resolvable using the comedi module namespace.  For example, '
         'NI_PFI(0), TRIGGER_LINE(1), ... are valid for NI devices.  You can '
         'also specify a raw integer value if desired.')
  parser.add_argument( '-w', '--waveform', type=int, default=0,
    help='[Default 0]' + '\n\t'.join([ '{}: {}'.format(i,c.name)
           for i,c in zip(xrange(len(dds_list)), dds_list)]) )
  parser.add_argument( '-C', '--continuous', action='store_true',
    help='Select continuous operation')
  parser.add_argument( '-v', '--verbose', action='store_true' )
  parser.add_argument( '--oswrite', action='store_true' )
  parser.add_argument( '--write_more', action='store_true' )
  parser.add_argument( '-L', '--waveform_len', type=int, default=1<<16,
    help='Select the number of samples in the waveform to repeat' )
  parser.add_argument( '-S', '--show-waveform', action='store_true' )
  return parser.parse_args(arglist)

def main(arglist):
  t = Test( process_args(arglist) )
  t.start()
  t.wait()
  t.stop()
  t.close()

if __name__ == '__main__':
  main(sys.argv[1:])
