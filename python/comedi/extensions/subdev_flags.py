# vim: ts=2:sw=2:tw=80:nowrap

from .. import clib

def to_dict( flags ):
  class Dict(dict):
    def __init__(self, *a, **kw):
      super(Dict,self).__init__(*a, **kw)
      self.__dict__ = self

  D = Dict(
    busy                  =     bool(flags & clib.SDF_BUSY),
    busy_owner            =     bool(flags & clib.SDF_BUSY_OWNER),
    locked                =     bool(flags & clib.SDF_LOCKED),
    lock_owner            =     bool(flags & clib.SDF_LOCK_OWNER),
    maxdata_per_channel   =     bool(flags & clib.SDF_MAXDATA),
    flags_per_channel     =     bool(flags & clib.SDF_FLAGS),
    rangetype_per_channel =     bool(flags & clib.SDF_RANGETYPE),
    async_cmd_supported   =     bool(flags & clib.SDF_CMD),
    soft_calibrated       =     bool(flags & clib.SDF_SOFT_CALIBRATED),
    readable              =     bool(flags & clib.SDF_READABLE),
    writeable             =     bool(flags & clib.SDF_WRITEABLE),
    internal              =     bool(flags & clib.SDF_INTERNAL),
    aref_ground_supported =     bool(flags & clib.SDF_GROUND),
    aref_common_supported =     bool(flags & clib.SDF_COMMON),
    aref_diff_supported   =     bool(flags & clib.SDF_DIFF),
    aref_other_supported  =     bool(flags & clib.SDF_OTHER),
    dither_supported      =     bool(flags & clib.SDF_DITHER),
    deglitch_supported    =     bool(flags & clib.SDF_DEGLITCH),
    running               =     bool(flags & clib.SDF_RUNNING),
    sample_32bit          =     bool(flags & clib.SDF_LSAMPL),
    sample_16bit          = not bool(flags & clib.SDF_LSAMPL),
    sample_bitwise        =     bool(flags & clib.SDF_PACKED),
  )
  return D

#clib.subdev_flags_to_dict = to_dict
