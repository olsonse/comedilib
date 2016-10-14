# vim: ts=2:sw=2:tw=80:nowrap
"""
a ctypes wrapper for comedi that provides an interface that is compatible with
the c-library (and for which the c-library manuals still work).
"""

from ctypes_comedi import *

# Add entries in module dictionary to strip comedi_/COMEDI_ prefix
import re
for k,v in globals().items():
  if re.match('^comedi_', k, flags=re.IGNORECASE):
    globals()[k[7:]] = v
    # uncommenting following line removes compatibility with old code using
    # comedi_ prefix:
    # globals().pop(k)
del re, k, v

import extensions
