# vim: ts=2:sw=2:tw=80:nowrap

from .. import ctypes_comedi as comedi

insn_map = { i:getattr(comedi,i) for i in dir(comedi) if i.startswith('INSN') }
insn_rmap= { v:k for k,v in insn_map.items() }

#### comedi_insn ####
def comedi_insn_to_dict(self):
  D = {
    i:getattr(self,i) for i in dir(self)
      if i[0] != '_' and not callable(getattr(self,i))
  }

  D['insn'] = insn_rmap[ self.insn ]
  D['data'] = self.data[:self.n]
  D['unused'] = self.unused[:]
  D['chanspec'] = \
    dict( channel = comedi.CR_CHAN(self.chanspec),
             aref = comedi.CR_AREF(self.chanspec),
            range = comedi.CR_RANGE(self.chanspec) )

  return D

def comedi_insn_repr(self):
  return repr( self.dict() )

def comedi_insn_copy_members(self, other):
  self.insn       = other.insn
  self.n          = other.n
  self.data       = other.data
  self.subdev     = other.subdev
  self.chanspec   = other.chanspec
  self.unused[:]  = other.unused[:]


comedi.comedi_insn.dict = comedi_insn_to_dict
comedi.comedi_insn.__repr__ = comedi_insn_repr
comedi.comedi_insn.copy_members = comedi_insn_copy_members




#### comedi_insnlist ####
def comedi_insnlist_to_dict(self):
  return dict(
    insns = self.insns[:self.n_insns],
    n_insns = self.n_insns,
  )

def comedi_insnlist_repr(self):
  return repr( self.dict() )

def comedi_insnlist_getitem(self, i):
  return self.insns[i]

def comedi_insnlist_iter(self):
  return iter( self.insns[:self.n_insns] )

def comedi_insnlist_set_length(self, length):
  """
  Allocate the memory of the instruction list and set the n_insns member.

  This is mostly a convenience function.  It is not necessary to use this
  function.  One could do this manually instead:
  old_insns = L.insns
  L.insns = (comedi.insn * length)()
  L.n_insns = length
  if old_insns:
    del old_insns

  This function only deletes the old data if this function was used to create
  it.

  The one other thing this function does do is to copy the old data to the new
  list (for where the lengths overlap).  Note that this copy does only do
  assignment.  In other words, if a data ptr of one insn structure pointed to
  some memory, the new data ptr will point to the same memory location (i.e. new
  data will not be allocated).
  """
  old_insns = None
  old_n_insns = 0
  if hasattr(self, '_self_made') and getattr(self,'_self_made'):
    old_insns = self.insns
    old_n_insns = self.n_insns

  self.n_insns = length
  self.insns = (comedi.comedi_insn * length)()
  self._self_made = True

  # copy over the old data
  for i in xrange( min(old_n_insns, self.n_insns) ):
    self.insns[i].copy_members( old_insns[i] )

  if old_insns:
    # free the old memory
    del old_insns


comedi.comedi_insnlist.dict = comedi_insnlist_to_dict
comedi.comedi_insnlist.__repr__ = comedi_insnlist_repr
comedi.comedi_insnlist.__getitem__ = comedi_insnlist_getitem
comedi.comedi_insnlist.__iter__ = comedi_insnlist_iter
comedi.comedi_insnlist.set_length = comedi_insnlist_set_length
