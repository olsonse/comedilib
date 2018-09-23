# vim: ts=2:sw=2:tw=80:nowrap

from .. import clib

#### comedi_range ####
def comedi_range_to_dict(self):
  D = {
    i:getattr(self,i) for i in dir(self)
      if i[0] != '_' and not callable(getattr(self,i))
  }

  D['unit'] = {
    clib.UNIT_mA: 'mA',
    clib.UNIT_none: None,
    clib.UNIT_volt: 'V',
  }[ self.unit ]
  return D

def comedi_range_repr(self):
  return repr( self.dict() )

clib.comedi_range.dict = comedi_range_to_dict
clib.comedi_range.__repr__ = comedi_range_repr
