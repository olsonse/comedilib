# vim: ts=2:sw=2:tw=80:nowrap

from .. import clib

#### comedi_route_pair ####
def comedi_route_pair_to_dict(self):
  D = {
    i:getattr(self,i) for i in dir(self)
      if i[0] != '_' and not callable(getattr(self,i))
  }
  return D

def comedi_route_pair_repr(self):
  return repr( self.dict() )

clib.comedi_route_pair.dict     = comedi_route_pair_to_dict
clib.comedi_route_pair.__repr__ = comedi_route_pair_repr
