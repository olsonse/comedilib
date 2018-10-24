# SPDX-License-Identifier: GPL-2.0+
# vim: ts=2:sw=2:et:tw=80:nowrap
"""
This file helps to extract string names of NI signals as included in comedi.h
between NI_NAMES_BASE and NI_NAMES_BASE+NI_NUM_NAMES.

This file could be extended to provide a similar functionality for other
drivers.
"""

# This file is a version of the kernel staging file at:
#   drivers/staging/comedi/drivers/ni_routing/tools/ni_names.py
# This is simply to aide in creating the entries in the order of the value of
# the device-global NI signal/terminal constants defined in comedi.h
from . import clib


ni_macros = (
  'NI_PFI',
  'TRIGGER_LINE',
  'NI_RTSI_BRD',
  'NI_CtrSource',
  'NI_CtrGate',
  'NI_CtrAux',
  'NI_CtrA',
  'NI_CtrB',
  'NI_CtrZ',
  'NI_CtrArmStartTrigger',
  'NI_CtrInternalOutput',
  'NI_CtrOut',
  'NI_CtrSampleClock',
)

def get_ni_names():
  name_dict = dict()

  # load all the static names; start with those that do not begin with NI_
  name_dict['PXI_Star'] = clib.PXI_Star
  name_dict['PXI_Clk10'] = clib.PXI_Clk10

  #load all macro values
  for fun in ni_macros:
    f = getattr(clib, fun)
    name_dict.update({
      '{}({})'.format(fun,i):f(i) for i in range(1 + f(-1) - f(0))
    })

  #load everything else in ni_common_signal_names enum
  name_dict.update({
    k:v for k,v in clib.__dict__.items()
    if k.startswith('NI_') and (not callable(v)) and
       clib.NI_COUNTER_NAMES_MAX < v < (clib.NI_NAMES_BASE + clib.NI_NUM_NAMES)
  })

  # now create reverse lookup (value -> name)

  val_dict = {v:k for k,v in name_dict.items()}

  return name_dict, val_dict

to_value, from_value = get_ni_names()
