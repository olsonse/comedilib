# vim: ts=2:sw=2:tw=80:nowrap
"""
When loaded, this package automatically injects some modifications to the comedi
(made mostly for convenience of viewing/printing) classes provided for the
ctypes library.
"""

from . import cmd
from . import insn
from . import crange
from . import subdev_flags
from . import route_pair
