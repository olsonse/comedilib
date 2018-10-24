# vim: ts=2:sw=2:tw=80:nowrap

from .. import clib

#### comedi_cmd ####
def comedi_cmd_to_dict(self):
  D = {
    i:getattr(self,i) for i in dir(self)
      if i[0] != '_' and not callable(getattr(self,i))
  }

  D.update(dict(
    chanlist = tuple(
      dict( channel = clib.CR_CHAN(self.chanlist[i]),
               aref = clib.CR_AREF(self.chanlist[i]),
              range = clib.CR_RANGE(self.chanlist[i]) )
      for i in range( self.chanlist_len )
    ),
    data = None if not self.data else self.data.contents
  ))

  return D

def comedi_cmd_diff(self, other):
  setI = lambda L : set([(i[0], repr(i[1])) for i in L])
  old = setI(self.dict().items()) - setI(other.dict().items())
  new = setI(other.dict().items()) - setI(self.dict().items())
  return dict(old=dict(old), new=dict(new))

def comedi_cmd_repr(self):
  return repr( self.dict() )

clib.comedi_cmd.dict = comedi_cmd_to_dict
clib.comedi_cmd.diff = comedi_cmd_diff
clib.comedi_cmd.__repr__ = comedi_cmd_repr