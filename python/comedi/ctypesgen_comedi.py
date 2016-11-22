'''Wrapper for comedi.h

Generated with:
/home/olsonse/src/ctypesgen/ctypesgen.py -lcomedi -R ../../lib/.libs/ ../../include/comedi.h ../../include/comedilib.h -o ctypesgen_comedi.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char*len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes,errcheck):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
        if errcheck:
          self.func.errcheck = errcheck
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = ['../../lib/.libs/']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    THIS_DIR = os.path.dirname(__file__)
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(os.path.join(THIS_DIR,F))
        loader.other_dirs.append(F)

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs(['../../lib/.libs/'])

# Begin libraries

_libs["comedi"] = load_library("comedi")

# 1 libraries
# End libraries

# No modules

lsampl_t = c_uint # /home/olsonse/src/comedi/comedilib/include/comedi.h: 74

sampl_t = c_ushort # /home/olsonse/src/comedi/comedilib/include/comedi.h: 75

enum_comedi_subdevice_type = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_UNUSED = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_AI = (COMEDI_SUBD_UNUSED + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_AO = (COMEDI_SUBD_AI + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_DI = (COMEDI_SUBD_AO + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_DO = (COMEDI_SUBD_DI + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_DIO = (COMEDI_SUBD_DO + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_COUNTER = (COMEDI_SUBD_DIO + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_TIMER = (COMEDI_SUBD_COUNTER + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_MEMORY = (COMEDI_SUBD_TIMER + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_CALIB = (COMEDI_SUBD_MEMORY + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_PROC = (COMEDI_SUBD_CALIB + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_SERIAL = (COMEDI_SUBD_PROC + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

COMEDI_SUBD_PWM = (COMEDI_SUBD_SERIAL + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 244

enum_comedi_io_direction = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 272

COMEDI_INPUT = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 272

COMEDI_OUTPUT = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 272

COMEDI_OPENDRAIN = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 272

enum_configuration_ids = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_DIO_INPUT = COMEDI_INPUT # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_DIO_OUTPUT = COMEDI_OUTPUT # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_DIO_OPENDRAIN = COMEDI_OPENDRAIN # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_ANALOG_TRIG = 16 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_ALT_SOURCE = 20 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_DIGITAL_TRIG = 21 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_BLOCK_SIZE = 22 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_TIMER_1 = 23 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_FILTER = 24 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_CHANGE_NOTIFY = 25 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_SERIAL_CLOCK = 26 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_BIDIRECTIONAL_DATA = 27 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_DIO_QUERY = 28 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_PWM_OUTPUT = 29 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_PWM_OUTPUT = 30 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_ARM = 31 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_DISARM = 32 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_COUNTER_STATUS = 33 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_RESET = 34 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GPCT_SINGLE_PULSE_GENERATOR = 1001 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GPCT_PULSE_TRAIN_GENERATOR = 1002 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GPCT_QUADRATURE_ENCODER = 1003 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_SET_GATE_SRC = 2001 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_GATE_SRC = 2002 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_SET_CLOCK_SRC = 2003 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_CLOCK_SRC = 2004 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_SET_OTHER_SRC = 2005 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_HARDWARE_BUFFER_SIZE = 2006 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_SET_COUNTER_MODE = 4097 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_8254_SET_MODE = INSN_CONFIG_SET_COUNTER_MODE # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_8254_READ_STATUS = 4098 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_SET_ROUTING = 4099 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_ROUTING = 4109 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_PWM_SET_PERIOD = 5000 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_PWM_GET_PERIOD = 5001 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_PWM_STATUS = 5002 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_PWM_SET_H_BRIDGE = 5003 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_PWM_GET_H_BRIDGE = 5004 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

INSN_CONFIG_GET_CMD_TIMING_CONSTRAINTS = 5005 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 331

enum_device_config_route_ids = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 387

INSN_DEVICE_CONFIG_TEST_ROUTE = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 387

INSN_DEVICE_CONFIG_CONNECT_ROUTE = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 387

INSN_DEVICE_CONFIG_DISCONNECT_ROUTE = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 387

INSN_DEVICE_CONFIG_GET_ROUTES = 3 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 387

enum_comedi_digital_trig_op = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 444

COMEDI_DIGITAL_TRIG_DISABLE = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 444

COMEDI_DIGITAL_TRIG_ENABLE_EDGES = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 444

COMEDI_DIGITAL_TRIG_ENABLE_LEVELS = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 444

enum_comedi_support_level = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 456

COMEDI_UNKNOWN_SUPPORT = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 456

COMEDI_SUPPORTED = (COMEDI_UNKNOWN_SUPPORT + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 456

COMEDI_UNSUPPORTED = (COMEDI_SUPPORTED + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 456

enum_comedi_counter_status_flags = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 471

COMEDI_COUNTER_ARMED = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 471

COMEDI_COUNTER_COUNTING = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 471

COMEDI_COUNTER_TERMINAL_COUNT = 4 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 471

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 624
class struct_comedi_cmd_struct(Structure):
    pass

comedi_cmd = struct_comedi_cmd_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 501

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 526
class struct_comedi_insn_struct(Structure):
    pass

comedi_insn = struct_comedi_insn_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 502

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 542
class struct_comedi_insnlist_struct(Structure):
    pass

comedi_insnlist = struct_comedi_insnlist_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 503

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 668
class struct_comedi_chaninfo_struct(Structure):
    pass

comedi_chaninfo = struct_comedi_chaninfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 504

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 819
class struct_comedi_subdinfo_struct(Structure):
    pass

comedi_subdinfo = struct_comedi_subdinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 505

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 846
class struct_comedi_devinfo_struct(Structure):
    pass

comedi_devinfo = struct_comedi_devinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 506

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 869
class struct_comedi_devconfig_struct(Structure):
    pass

comedi_devconfig = struct_comedi_devconfig_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 507

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 693
class struct_comedi_rangeinfo_struct(Structure):
    pass

comedi_rangeinfo = struct_comedi_rangeinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 508

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 720
class struct_comedi_krange_struct(Structure):
    pass

comedi_krange = struct_comedi_krange_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 509

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 895
class struct_comedi_bufconfig_struct(Structure):
    pass

comedi_bufconfig = struct_comedi_bufconfig_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 510

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 922
class struct_comedi_bufinfo_struct(Structure):
    pass

comedi_bufinfo = struct_comedi_bufinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 511

struct_comedi_insn_struct.__slots__ = [
    'insn',
    'n',
    'data',
    'subdev',
    'chanspec',
    'unused',
]
struct_comedi_insn_struct._fields_ = [
    ('insn', c_uint),
    ('n', c_uint),
    ('data', POINTER(lsampl_t)),
    ('subdev', c_uint),
    ('chanspec', c_uint),
    ('unused', c_uint * 3),
]

struct_comedi_insnlist_struct.__slots__ = [
    'n_insns',
    'insns',
]
struct_comedi_insnlist_struct._fields_ = [
    ('n_insns', c_uint),
    ('insns', POINTER(comedi_insn)),
]

struct_comedi_cmd_struct.__slots__ = [
    'subdev',
    'flags',
    'start_src',
    'start_arg',
    'scan_begin_src',
    'scan_begin_arg',
    'convert_src',
    'convert_arg',
    'scan_end_src',
    'scan_end_arg',
    'stop_src',
    'stop_arg',
    'chanlist',
    'chanlist_len',
    'data',
    'data_len',
]
struct_comedi_cmd_struct._fields_ = [
    ('subdev', c_uint),
    ('flags', c_uint),
    ('start_src', c_uint),
    ('start_arg', c_uint),
    ('scan_begin_src', c_uint),
    ('scan_begin_arg', c_uint),
    ('convert_src', c_uint),
    ('convert_arg', c_uint),
    ('scan_end_src', c_uint),
    ('scan_end_arg', c_uint),
    ('stop_src', c_uint),
    ('stop_arg', c_uint),
    ('chanlist', POINTER(c_uint)),
    ('chanlist_len', c_uint),
    ('data', POINTER(sampl_t)),
    ('data_len', c_uint),
]

struct_comedi_chaninfo_struct.__slots__ = [
    'subdev',
    'maxdata_list',
    'flaglist',
    'rangelist',
    'unused',
]
struct_comedi_chaninfo_struct._fields_ = [
    ('subdev', c_uint),
    ('maxdata_list', POINTER(lsampl_t)),
    ('flaglist', POINTER(c_uint)),
    ('rangelist', POINTER(c_uint)),
    ('unused', c_uint * 4),
]

struct_comedi_rangeinfo_struct.__slots__ = [
    'range_type',
    'range_ptr',
]
struct_comedi_rangeinfo_struct._fields_ = [
    ('range_type', c_uint),
    ('range_ptr', POINTER(None)),
]

struct_comedi_krange_struct.__slots__ = [
    'min',
    'max',
    'flags',
]
struct_comedi_krange_struct._fields_ = [
    ('min', c_int),
    ('max', c_int),
    ('flags', c_uint),
]

struct_comedi_subdinfo_struct.__slots__ = [
    'type',
    'n_chan',
    'subd_flags',
    'timer_type',
    'len_chanlist',
    'maxdata',
    'flags',
    'range_type',
    'settling_time_0',
    'insn_bits_support',
    'unused',
]
struct_comedi_subdinfo_struct._fields_ = [
    ('type', c_uint),
    ('n_chan', c_uint),
    ('subd_flags', c_uint),
    ('timer_type', c_uint),
    ('len_chanlist', c_uint),
    ('maxdata', lsampl_t),
    ('flags', c_uint),
    ('range_type', c_uint),
    ('settling_time_0', c_uint),
    ('insn_bits_support', c_uint),
    ('unused', c_uint * 8),
]

struct_comedi_devinfo_struct.__slots__ = [
    'version_code',
    'n_subdevs',
    'driver_name',
    'board_name',
    'read_subdevice',
    'write_subdevice',
    'unused',
]
struct_comedi_devinfo_struct._fields_ = [
    ('version_code', c_uint),
    ('n_subdevs', c_uint),
    ('driver_name', c_char * 20),
    ('board_name', c_char * 20),
    ('read_subdevice', c_int),
    ('write_subdevice', c_int),
    ('unused', c_int * 30),
]

struct_comedi_devconfig_struct.__slots__ = [
    'board_name',
    'options',
]
struct_comedi_devconfig_struct._fields_ = [
    ('board_name', c_char * 20),
    ('options', c_int * 32),
]

struct_comedi_bufconfig_struct.__slots__ = [
    'subdevice',
    'flags',
    'maximum_size',
    'size',
    'unused',
]
struct_comedi_bufconfig_struct._fields_ = [
    ('subdevice', c_uint),
    ('flags', c_uint),
    ('maximum_size', c_uint),
    ('size', c_uint),
    ('unused', c_uint * 4),
]

struct_comedi_bufinfo_struct.__slots__ = [
    'subdevice',
    'bytes_read',
    'buf_write_ptr',
    'buf_read_ptr',
    'buf_write_count',
    'buf_read_count',
    'bytes_written',
    'unused',
]
struct_comedi_bufinfo_struct._fields_ = [
    ('subdevice', c_uint),
    ('bytes_read', c_uint),
    ('buf_write_ptr', c_uint),
    ('buf_read_ptr', c_uint),
    ('buf_write_count', c_uint),
    ('buf_read_count', c_uint),
    ('bytes_written', c_uint),
    ('unused', c_uint * 4),
]

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 944
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'source',
    'destination',
]
struct_anon_1._fields_ = [
    ('source', c_uint),
    ('destination', c_uint),
]

comedi_route_pair = struct_anon_1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 944

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 965
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'config_id',
    'n',
    'route_list',
]
struct_anon_2._fields_ = [
    ('config_id', c_uint),
    ('n', c_uint),
    ('route_list', POINTER(comedi_route_pair)),
]

comedi_get_routes_data = struct_anon_2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 965

enum_i8254_mode = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_MODE0 = (0 << 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_MODE1 = (1 << 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_MODE2 = (2 << 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_MODE3 = (3 << 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_MODE4 = (4 << 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_MODE5 = (5 << 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_BCD = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

I8254_BINARY = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1005

enum_ni_common_signal_names = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

PXI_Star = (((((((((((((((((((((((((1 << 15) + ((-1) & 63)) + 1) + ((-1) & 7)) + 1) + ((-1) & 3)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) + ((-1) & 7)) + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

PXI_Clk10 = (PXI_Star + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_SampleClock = (PXI_Clk10 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_SampleClockTimebase = (NI_AI_SampleClock + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_StartTrigger = (NI_AI_SampleClockTimebase + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_ReferenceTrigger = (NI_AI_StartTrigger + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_ConvertClock = (NI_AI_ReferenceTrigger + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_ConvertClockTimebase = (NI_AI_ConvertClock + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_HoldCompleteEvent = (NI_AI_ConvertClockTimebase + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_PauseTrigger = (NI_AI_HoldCompleteEvent + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AO_SampleClock = (NI_AI_PauseTrigger + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AO_SampleClockTimebase = (NI_AO_SampleClock + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AO_StartTrigger = (NI_AO_SampleClockTimebase + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AO_PauseTrigger = (NI_AO_StartTrigger + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_DI_SampleClock = (NI_AO_PauseTrigger + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_DO_SampleClock = (NI_DI_SampleClock + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_MasterTimebase = (NI_DO_SampleClock + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_20MHzTimebase = (NI_MasterTimebase + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_80MHzTimebase = (NI_20MHzTimebase + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_100kHzTimebase = (NI_80MHzTimebase + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_10MHzRefClock = (NI_100kHzTimebase + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_FrequencyOutput = (NI_10MHzRefClock + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_ChangeDetectionEvent = (NI_FrequencyOutput + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AnalogComparisonEvent = (NI_ChangeDetectionEvent + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AIHoldCompleteEvent = (NI_AnalogComparisonEvent + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AIHoldComplete = (NI_AIHoldCompleteEvent + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_SCXI_Trig1 = (NI_AIHoldComplete + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_LogicLow = (NI_SCXI_Trig1 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_LogicHigh = (NI_LogicLow + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_ExternalStrobe = (NI_LogicHigh + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_ExternalMUXClock = (NI_ExternalStrobe + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_PFI_DO = (NI_AI_ExternalMUXClock + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_CaseGround = (NI_PFI_DO + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_AI_STOP = (NI_CaseGround + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_RGOUT0 = (NI_AI_STOP + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

_NI_NAMES_MAX_PLUS_1 = (NI_RGOUT0 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

NI_NUM_NAMES = (_NI_NAMES_MAX_PLUS_1 - (1 << 15)) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1100

enum_ni_gpct_mode_bits = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_GATE_ON_BOTH_EDGES_BIT = 4 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_EDGE_GATE_MODE_MASK = 24 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_EDGE_GATE_STARTS_STOPS_BITS = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_EDGE_GATE_STOPS_STARTS_BITS = 8 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_EDGE_GATE_STARTS_BITS = 16 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_EDGE_GATE_NO_STARTS_NO_STOPS_BITS = 24 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_STOP_MODE_MASK = 96 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_STOP_ON_GATE_BITS = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_STOP_ON_GATE_OR_TC_BITS = 32 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_STOP_ON_GATE_OR_SECOND_TC_BITS = 64 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_LOAD_B_SELECT_BIT = 128 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_OUTPUT_MODE_MASK = 768 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_OUTPUT_TC_PULSE_BITS = 256 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_OUTPUT_TC_TOGGLE_BITS = 512 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_OUTPUT_TC_OR_GATE_TOGGLE_BITS = 768 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_HARDWARE_DISARM_MASK = 3072 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_NO_HARDWARE_DISARM_BITS = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_DISARM_AT_TC_BITS = 1024 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_DISARM_AT_GATE_BITS = 2048 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_DISARM_AT_TC_OR_GATE_BITS = 3072 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_LOADING_ON_TC_BIT = 4096 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_LOADING_ON_GATE_BIT = 16384 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_MODE_MASK = (7 << 16) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_MODE_NORMAL_BITS = (0 << 16) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_MODE_QUADRATURE_X1_BITS = (1 << 16) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_MODE_QUADRATURE_X2_BITS = (2 << 16) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_MODE_QUADRATURE_X4_BITS = (3 << 16) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_MODE_TWO_PULSE_BITS = (4 << 16) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_MODE_SYNC_SOURCE_BITS = (6 << 16) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_INDEX_PHASE_MASK = (3 << 20) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_INDEX_PHASE_LOW_A_LOW_B_BITS = (0 << 20) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_INDEX_PHASE_LOW_A_HIGH_B_BITS = (1 << 20) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_INDEX_PHASE_HIGH_A_LOW_B_BITS = (2 << 20) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_INDEX_PHASE_HIGH_A_HIGH_B_BITS = (3 << 20) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_INDEX_ENABLE_BIT = 4194304 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_DIRECTION_MASK = (3 << 24) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_DIRECTION_DOWN_BITS = (0 << 24) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_DIRECTION_UP_BITS = (1 << 24) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_DIRECTION_HW_UP_DOWN_BITS = (2 << 24) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_COUNTING_DIRECTION_HW_GATE_BITS = (3 << 24) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_RELOAD_SOURCE_MASK = 201326592 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_RELOAD_SOURCE_FIXED_BITS = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_RELOAD_SOURCE_SWITCHING_BITS = 67108864 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_RELOAD_SOURCE_GATE_SELECT_BITS = 134217728 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_OR_GATE_BIT = 268435456 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

NI_GPCT_INVERT_OUTPUT_BIT = 536870912 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1156

enum_ni_gpct_clock_source_bits = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_CLOCK_SRC_SELECT_MASK = 63 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_TIMEBASE_1_CLOCK_SRC_BITS = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_TIMEBASE_2_CLOCK_SRC_BITS = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_TIMEBASE_3_CLOCK_SRC_BITS = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_LOGIC_LOW_CLOCK_SRC_BITS = 3 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_NEXT_GATE_CLOCK_SRC_BITS = 4 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_NEXT_TC_CLOCK_SRC_BITS = 5 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_SOURCE_PIN_i_CLOCK_SRC_BITS = 6 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_PXI10_CLOCK_SRC_BITS = 7 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_PXI_STAR_TRIGGER_CLOCK_SRC_BITS = 8 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_ANALOG_TRIGGER_OUT_CLOCK_SRC_BITS = 9 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_PRESCALE_MODE_CLOCK_SRC_MASK = 805306368 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_NO_PRESCALE_CLOCK_SRC_BITS = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_PRESCALE_X2_CLOCK_SRC_BITS = 268435456 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_PRESCALE_X8_CLOCK_SRC_BITS = 536870912 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

NI_GPCT_INVERT_CLOCK_SRC_BIT = 2147483648 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1224

enum_ni_gpct_gate_select = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_TIMESTAMP_MUX_GATE_SELECT = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_AI_START2_GATE_SELECT = 18 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_PXI_STAR_TRIGGER_GATE_SELECT = 19 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_NEXT_OUT_GATE_SELECT = 20 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_AI_START1_GATE_SELECT = 28 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_NEXT_SOURCE_GATE_SELECT = 29 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_ANALOG_TRIGGER_OUT_GATE_SELECT = 30 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_LOGIC_LOW_GATE_SELECT = 31 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_SOURCE_PIN_i_GATE_SELECT = 256 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_GATE_PIN_i_GATE_SELECT = 257 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_UP_DOWN_PIN_i_GATE_SELECT = 513 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_SELECTED_GATE_GATE_SELECT = 542 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

NI_GPCT_DISABLED_GATE_SELECT = 32768 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1259

enum_ni_gpct_other_index = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1292

NI_GPCT_SOURCE_ENCODER_A = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1292

NI_GPCT_SOURCE_ENCODER_B = (NI_GPCT_SOURCE_ENCODER_A + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1292

NI_GPCT_SOURCE_ENCODER_Z = (NI_GPCT_SOURCE_ENCODER_B + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1292

enum_ni_gpct_other_select = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1298

NI_GPCT_DISABLED_OTHER_SELECT = 32768 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1298

enum_ni_gpct_arm_source = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1310

NI_GPCT_ARM_IMMEDIATE = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1310

NI_GPCT_ARM_PAIRED_IMMEDIATE = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1310

NI_GPCT_HW_ARM = 4096 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1310

NI_GPCT_ARM_UNKNOWN = NI_GPCT_HW_ARM # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1310

enum_ni_gpct_filter_select = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

NI_GPCT_FILTER_OFF = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

NI_GPCT_FILTER_TIMEBASE_3_SYNC = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

NI_GPCT_FILTER_100x_TIMEBASE_1 = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

NI_GPCT_FILTER_20x_TIMEBASE_1 = 3 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

NI_GPCT_FILTER_10x_TIMEBASE_1 = 4 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

NI_GPCT_FILTER_2x_TIMEBASE_1 = 5 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

NI_GPCT_FILTER_2x_TIMEBASE_3 = 6 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1329

enum_ni_pfi_filter_select = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1343

NI_PFI_FILTER_OFF = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1343

NI_PFI_FILTER_125ns = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1343

NI_PFI_FILTER_6425ns = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1343

NI_PFI_FILTER_2550us = 3 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1343

enum_ni_mio_clock_source = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1351

NI_MIO_INTERNAL_CLOCK = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1351

NI_MIO_RTSI_CLOCK = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1351

NI_MIO_PLL_PXI_STAR_TRIGGER_CLOCK = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1351

NI_MIO_PLL_PXI10_CLOCK = 3 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1351

NI_MIO_PLL_RTSI0_CLOCK = 4 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1351

enum_ni_rtsi_routing = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_ADR_START1 = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_ADR_START2 = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_SCLKG = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_DACUPDN = 3 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_DA_START1 = 4 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_G_SRC0 = 5 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_G_GATE0 = 6 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_RGOUT0 = 7 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_RTSI_BRD_0 = 8 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

NI_RTSI_OUTPUT_RTSI_OSC = 12 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1370

enum_ni_pfi_routing = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_PFI_DEFAULT = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_AI_START1 = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_AI_START2 = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_AI_CONVERT = 3 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_G_SRC1 = 4 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_G_GATE1 = 5 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_AO_UPDATE_N = 6 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_AO_START1 = 7 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_AI_START_PULSE = 8 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_G_SRC0 = 9 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_G_GATE0 = 10 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_EXT_STROBE = 11 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_AI_EXT_MUX_CLK = 12 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_GOUT0 = 13 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_GOUT1 = 14 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_FREQ_OUT = 15 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_PFI_DO = 16 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_I_ATRIG = 17 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_RTSI0 = 18 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_PXI_STAR_TRIGGER_IN = 26 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_SCXI_TRIG1 = 27 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_DIO_CHANGE_DETECT_RTSI = 28 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_CDI_SAMPLE = 29 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

NI_PFI_OUTPUT_CDO_UPDATE = 30 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1393

enum_ni_660x_pfi_routing = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1430

NI_660X_PFI_OUTPUT_COUNTER = 1 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1430

NI_660X_PFI_OUTPUT_DIO = 2 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1430

enum_ni_m_series_cdio_scan_begin_src = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_GROUND = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_AI_START = 18 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_AI_CONVERT = 19 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_PXI_STAR_TRIGGER = 20 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_G0_OUT = 28 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_G1_OUT = 29 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_ANALOG_TRIGGER = 30 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_AO_UPDATE = 31 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_FREQ_OUT = 32 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

NI_CDIO_SCAN_BEGIN_SRC_DIO_CHANGE_DETECT_IRQ = 33 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1448

enum_ni_freq_out_clock_source_bits = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1476

NI_FREQ_OUT_TIMEBASE_1_DIV_2_CLOCK_SRC = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1476

NI_FREQ_OUT_TIMEBASE_2_CLOCK_SRC = (NI_FREQ_OUT_TIMEBASE_1_DIV_2_CLOCK_SRC + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1476

enum_amplc_dio_clock_source = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_CLKN = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_10MHZ = (AMPLC_DIO_CLK_CLKN + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_1MHZ = (AMPLC_DIO_CLK_10MHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_100KHZ = (AMPLC_DIO_CLK_1MHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_10KHZ = (AMPLC_DIO_CLK_100KHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_1KHZ = (AMPLC_DIO_CLK_10KHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_OUTNM1 = (AMPLC_DIO_CLK_1KHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_EXT = (AMPLC_DIO_CLK_OUTNM1 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_VCC = (AMPLC_DIO_CLK_EXT + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_GND = (AMPLC_DIO_CLK_VCC + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_PAT_PRESENT = (AMPLC_DIO_CLK_GND + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

AMPLC_DIO_CLK_20MHZ = (AMPLC_DIO_CLK_PAT_PRESENT + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1485

enum_amplc_dio_ts_clock_src = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1520

AMPLC_DIO_TS_CLK_1GHZ = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1520

AMPLC_DIO_TS_CLK_1MHZ = (AMPLC_DIO_TS_CLK_1GHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1520

AMPLC_DIO_TS_CLK_1KHZ = (AMPLC_DIO_TS_CLK_1MHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1520

enum_amplc_dio_gate_source = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_VCC = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_GND = (AMPLC_DIO_GAT_VCC + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_GATN = (AMPLC_DIO_GAT_GND + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_NOUTNM2 = (AMPLC_DIO_GAT_GATN + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_RESERVED4 = (AMPLC_DIO_GAT_NOUTNM2 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_RESERVED5 = (AMPLC_DIO_GAT_RESERVED4 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_RESERVED6 = (AMPLC_DIO_GAT_RESERVED5 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_RESERVED7 = (AMPLC_DIO_GAT_RESERVED6 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_NGATN = 6 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_OUTNM2 = (AMPLC_DIO_GAT_NGATN + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_PAT_PRESENT = (AMPLC_DIO_GAT_OUTNM2 + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_PAT_OCCURRED = (AMPLC_DIO_GAT_PAT_PRESENT + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_PAT_GONE = (AMPLC_DIO_GAT_PAT_OCCURRED + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_NPAT_PRESENT = (AMPLC_DIO_GAT_PAT_GONE + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_NPAT_OCCURRED = (AMPLC_DIO_GAT_NPAT_PRESENT + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

AMPLC_DIO_GAT_NPAT_GONE = (AMPLC_DIO_GAT_NPAT_OCCURRED + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1530

enum_ke_counter_clock_source = c_int # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1562

KE_CLK_20MHZ = 0 # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1562

KE_CLK_4MHZ = (KE_CLK_20MHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1562

KE_CLK_EXT = (KE_CLK_4MHZ + 1) # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1562

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1590
class struct_comedi_trig_struct(Structure):
    pass

struct_comedi_trig_struct.__slots__ = [
    'subdev',
    'mode',
    'flags',
    'n_chan',
    'chanlist',
    'data',
    'n',
    'trigsrc',
    'trigvar',
    'trigvar1',
    'data_len',
    'unused',
]
struct_comedi_trig_struct._fields_ = [
    ('subdev', c_uint),
    ('mode', c_uint),
    ('flags', c_uint),
    ('n_chan', c_uint),
    ('chanlist', POINTER(c_uint)),
    ('data', POINTER(sampl_t)),
    ('n', c_uint),
    ('trigsrc', c_uint),
    ('trigvar', c_uint),
    ('trigvar1', c_uint),
    ('data_len', c_uint),
    ('unused', c_uint * 3),
]

comedi_trig = struct_comedi_trig_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1605

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 50
class struct_comedi_t_struct(Structure):
    pass

comedi_t = struct_comedi_t_struct # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 50

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 56
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'min',
    'max',
    'unit',
]
struct_anon_8._fields_ = [
    ('min', c_double),
    ('max', c_double),
    ('unit', c_uint),
]

comedi_range = struct_anon_8 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 56

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 71
class struct_comedi_sv_struct(Structure):
    pass

struct_comedi_sv_struct.__slots__ = [
    'dev',
    'subdevice',
    'chan',
    'range',
    'aref',
    'n',
    'maxdata',
]
struct_comedi_sv_struct._fields_ = [
    ('dev', POINTER(comedi_t)),
    ('subdevice', c_uint),
    ('chan', c_uint),
    ('range', c_int),
    ('aref', c_int),
    ('n', c_int),
    ('maxdata', lsampl_t),
]

comedi_sv_t = struct_comedi_sv_struct # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 71

enum_comedi_oor_behavior = c_int # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 73

COMEDI_OOR_NUMBER = 0 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 73

COMEDI_OOR_NAN = (COMEDI_OOR_NUMBER + 1) # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 73

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 81
if hasattr(_libs['comedi'], 'comedi_open'):
    comedi_open = _libs['comedi'].comedi_open
    comedi_open.argtypes = [String]
    comedi_open.restype = POINTER(comedi_t)

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 82
if hasattr(_libs['comedi'], 'comedi_close'):
    comedi_close = _libs['comedi'].comedi_close
    comedi_close.argtypes = [POINTER(comedi_t)]
    comedi_close.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 85
if hasattr(_libs['comedi'], 'comedi_loglevel'):
    comedi_loglevel = _libs['comedi'].comedi_loglevel
    comedi_loglevel.argtypes = [c_int]
    comedi_loglevel.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 86
if hasattr(_libs['comedi'], 'comedi_perror'):
    comedi_perror = _libs['comedi'].comedi_perror
    comedi_perror.argtypes = [String]
    comedi_perror.restype = None

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 87
if hasattr(_libs['comedi'], 'comedi_strerror'):
    comedi_strerror = _libs['comedi'].comedi_strerror
    comedi_strerror.argtypes = [c_int]
    comedi_strerror.restype = c_char_p

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 88
if hasattr(_libs['comedi'], 'comedi_errno'):
    comedi_errno = _libs['comedi'].comedi_errno
    comedi_errno.argtypes = []
    comedi_errno.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 89
if hasattr(_libs['comedi'], 'comedi_fileno'):
    comedi_fileno = _libs['comedi'].comedi_fileno
    comedi_fileno.argtypes = [POINTER(comedi_t)]
    comedi_fileno.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 92
if hasattr(_libs['comedi'], 'comedi_set_global_oor_behavior'):
    comedi_set_global_oor_behavior = _libs['comedi'].comedi_set_global_oor_behavior
    comedi_set_global_oor_behavior.argtypes = [enum_comedi_oor_behavior]
    comedi_set_global_oor_behavior.restype = enum_comedi_oor_behavior

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 95
if hasattr(_libs['comedi'], 'comedi_get_n_subdevices'):
    comedi_get_n_subdevices = _libs['comedi'].comedi_get_n_subdevices
    comedi_get_n_subdevices.argtypes = [POINTER(comedi_t)]
    comedi_get_n_subdevices.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 97
if hasattr(_libs['comedi'], 'comedi_get_version_code'):
    comedi_get_version_code = _libs['comedi'].comedi_get_version_code
    comedi_get_version_code.argtypes = [POINTER(comedi_t)]
    comedi_get_version_code.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 98
if hasattr(_libs['comedi'], 'comedi_get_driver_name'):
    comedi_get_driver_name = _libs['comedi'].comedi_get_driver_name
    comedi_get_driver_name.argtypes = [POINTER(comedi_t)]
    comedi_get_driver_name.restype = c_char_p

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 99
if hasattr(_libs['comedi'], 'comedi_get_board_name'):
    comedi_get_board_name = _libs['comedi'].comedi_get_board_name
    comedi_get_board_name.argtypes = [POINTER(comedi_t)]
    comedi_get_board_name.restype = c_char_p

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 100
if hasattr(_libs['comedi'], 'comedi_get_read_subdevice'):
    comedi_get_read_subdevice = _libs['comedi'].comedi_get_read_subdevice
    comedi_get_read_subdevice.argtypes = [POINTER(comedi_t)]
    comedi_get_read_subdevice.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 101
if hasattr(_libs['comedi'], 'comedi_get_write_subdevice'):
    comedi_get_write_subdevice = _libs['comedi'].comedi_get_write_subdevice
    comedi_get_write_subdevice.argtypes = [POINTER(comedi_t)]
    comedi_get_write_subdevice.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 104
if hasattr(_libs['comedi'], 'comedi_get_subdevice_type'):
    comedi_get_subdevice_type = _libs['comedi'].comedi_get_subdevice_type
    comedi_get_subdevice_type.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_subdevice_type.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 105
if hasattr(_libs['comedi'], 'comedi_find_subdevice_by_type'):
    comedi_find_subdevice_by_type = _libs['comedi'].comedi_find_subdevice_by_type
    comedi_find_subdevice_by_type.argtypes = [POINTER(comedi_t), c_int, c_uint]
    comedi_find_subdevice_by_type.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 106
if hasattr(_libs['comedi'], 'comedi_get_subdevice_flags'):
    comedi_get_subdevice_flags = _libs['comedi'].comedi_get_subdevice_flags
    comedi_get_subdevice_flags.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_subdevice_flags.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 107
if hasattr(_libs['comedi'], 'comedi_get_n_channels'):
    comedi_get_n_channels = _libs['comedi'].comedi_get_n_channels
    comedi_get_n_channels.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_n_channels.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 108
if hasattr(_libs['comedi'], 'comedi_range_is_chan_specific'):
    comedi_range_is_chan_specific = _libs['comedi'].comedi_range_is_chan_specific
    comedi_range_is_chan_specific.argtypes = [POINTER(comedi_t), c_uint]
    comedi_range_is_chan_specific.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 109
if hasattr(_libs['comedi'], 'comedi_maxdata_is_chan_specific'):
    comedi_maxdata_is_chan_specific = _libs['comedi'].comedi_maxdata_is_chan_specific
    comedi_maxdata_is_chan_specific.argtypes = [POINTER(comedi_t), c_uint]
    comedi_maxdata_is_chan_specific.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 112
if hasattr(_libs['comedi'], 'comedi_get_maxdata'):
    comedi_get_maxdata = _libs['comedi'].comedi_get_maxdata
    comedi_get_maxdata.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_get_maxdata.restype = lsampl_t

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 114
if hasattr(_libs['comedi'], 'comedi_get_n_ranges'):
    comedi_get_n_ranges = _libs['comedi'].comedi_get_n_ranges
    comedi_get_n_ranges.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_get_n_ranges.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 116
if hasattr(_libs['comedi'], 'comedi_get_range'):
    comedi_get_range = _libs['comedi'].comedi_get_range
    comedi_get_range.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint]
    comedi_get_range.restype = POINTER(comedi_range)

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 118
if hasattr(_libs['comedi'], 'comedi_find_range'):
    comedi_find_range = _libs['comedi'].comedi_find_range
    comedi_find_range.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_double, c_double]
    comedi_find_range.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 122
if hasattr(_libs['comedi'], 'comedi_get_buffer_size'):
    comedi_get_buffer_size = _libs['comedi'].comedi_get_buffer_size
    comedi_get_buffer_size.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_buffer_size.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 123
if hasattr(_libs['comedi'], 'comedi_get_max_buffer_size'):
    comedi_get_max_buffer_size = _libs['comedi'].comedi_get_max_buffer_size
    comedi_get_max_buffer_size.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_max_buffer_size.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 124
if hasattr(_libs['comedi'], 'comedi_set_buffer_size'):
    comedi_set_buffer_size = _libs['comedi'].comedi_set_buffer_size
    comedi_set_buffer_size.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_set_buffer_size.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 131
if hasattr(_libs['comedi'], 'comedi_do_insnlist'):
    comedi_do_insnlist = _libs['comedi'].comedi_do_insnlist
    comedi_do_insnlist.argtypes = [POINTER(comedi_t), POINTER(comedi_insnlist)]
    comedi_do_insnlist.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 132
if hasattr(_libs['comedi'], 'comedi_do_insn'):
    comedi_do_insn = _libs['comedi'].comedi_do_insn
    comedi_do_insn.argtypes = [POINTER(comedi_t), POINTER(comedi_insn)]
    comedi_do_insn.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 133
if hasattr(_libs['comedi'], 'comedi_lock'):
    comedi_lock = _libs['comedi'].comedi_lock
    comedi_lock.argtypes = [POINTER(comedi_t), c_uint]
    comedi_lock.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 134
if hasattr(_libs['comedi'], 'comedi_unlock'):
    comedi_unlock = _libs['comedi'].comedi_unlock
    comedi_unlock.argtypes = [POINTER(comedi_t), c_uint]
    comedi_unlock.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 143
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_set_read_subdevice'):
        continue
    comedi_set_read_subdevice = _lib.comedi_set_read_subdevice
    comedi_set_read_subdevice.argtypes = [POINTER(comedi_t), c_uint]
    comedi_set_read_subdevice.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 144
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_set_write_subdevice'):
        continue
    comedi_set_write_subdevice = _lib.comedi_set_write_subdevice
    comedi_set_write_subdevice.argtypes = [POINTER(comedi_t), c_uint]
    comedi_set_write_subdevice.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 147
if hasattr(_libs['comedi'], 'comedi_to_phys'):
    comedi_to_phys = _libs['comedi'].comedi_to_phys
    comedi_to_phys.argtypes = [lsampl_t, POINTER(comedi_range), lsampl_t]
    comedi_to_phys.restype = c_double

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 148
if hasattr(_libs['comedi'], 'comedi_from_phys'):
    comedi_from_phys = _libs['comedi'].comedi_from_phys
    comedi_from_phys.argtypes = [c_double, POINTER(comedi_range), lsampl_t]
    comedi_from_phys.restype = lsampl_t

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 149
if hasattr(_libs['comedi'], 'comedi_sampl_to_phys'):
    comedi_sampl_to_phys = _libs['comedi'].comedi_sampl_to_phys
    comedi_sampl_to_phys.argtypes = [POINTER(c_double), c_int, POINTER(sampl_t), c_int, POINTER(comedi_range), lsampl_t, c_int]
    comedi_sampl_to_phys.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 151
if hasattr(_libs['comedi'], 'comedi_sampl_from_phys'):
    comedi_sampl_from_phys = _libs['comedi'].comedi_sampl_from_phys
    comedi_sampl_from_phys.argtypes = [POINTER(sampl_t), c_int, POINTER(c_double), c_int, POINTER(comedi_range), lsampl_t, c_int]
    comedi_sampl_from_phys.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 155
if hasattr(_libs['comedi'], 'comedi_data_read'):
    comedi_data_read = _libs['comedi'].comedi_data_read
    comedi_data_read.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, POINTER(lsampl_t)]
    comedi_data_read.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 157
if hasattr(_libs['comedi'], 'comedi_data_read_n'):
    comedi_data_read_n = _libs['comedi'].comedi_data_read_n
    comedi_data_read_n.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, POINTER(lsampl_t), c_uint]
    comedi_data_read_n.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 159
if hasattr(_libs['comedi'], 'comedi_data_read_hint'):
    comedi_data_read_hint = _libs['comedi'].comedi_data_read_hint
    comedi_data_read_hint.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint]
    comedi_data_read_hint.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 161
if hasattr(_libs['comedi'], 'comedi_data_read_delayed'):
    comedi_data_read_delayed = _libs['comedi'].comedi_data_read_delayed
    comedi_data_read_delayed.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, POINTER(lsampl_t), c_uint]
    comedi_data_read_delayed.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 163
if hasattr(_libs['comedi'], 'comedi_data_write'):
    comedi_data_write = _libs['comedi'].comedi_data_write
    comedi_data_write.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, lsampl_t]
    comedi_data_write.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 165
if hasattr(_libs['comedi'], 'comedi_dio_config'):
    comedi_dio_config = _libs['comedi'].comedi_dio_config
    comedi_dio_config.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint]
    comedi_dio_config.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 167
if hasattr(_libs['comedi'], 'comedi_dio_get_config'):
    comedi_dio_get_config = _libs['comedi'].comedi_dio_get_config
    comedi_dio_get_config.argtypes = [POINTER(comedi_t), c_uint, c_uint, POINTER(c_uint)]
    comedi_dio_get_config.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 169
if hasattr(_libs['comedi'], 'comedi_dio_read'):
    comedi_dio_read = _libs['comedi'].comedi_dio_read
    comedi_dio_read.argtypes = [POINTER(comedi_t), c_uint, c_uint, POINTER(c_uint)]
    comedi_dio_read.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 171
if hasattr(_libs['comedi'], 'comedi_dio_write'):
    comedi_dio_write = _libs['comedi'].comedi_dio_write
    comedi_dio_write.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint]
    comedi_dio_write.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 173
if hasattr(_libs['comedi'], 'comedi_dio_bitfield2'):
    comedi_dio_bitfield2 = _libs['comedi'].comedi_dio_bitfield2
    comedi_dio_bitfield2.argtypes = [POINTER(comedi_t), c_uint, c_uint, POINTER(c_uint), c_uint]
    comedi_dio_bitfield2.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 177
if hasattr(_libs['comedi'], 'comedi_dio_bitfield'):
    comedi_dio_bitfield = _libs['comedi'].comedi_dio_bitfield
    comedi_dio_bitfield.argtypes = [POINTER(comedi_t), c_uint, c_uint, POINTER(c_uint)]
    comedi_dio_bitfield.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 181
if hasattr(_libs['comedi'], 'comedi_sv_init'):
    comedi_sv_init = _libs['comedi'].comedi_sv_init
    comedi_sv_init.argtypes = [POINTER(comedi_sv_t), POINTER(comedi_t), c_uint, c_uint]
    comedi_sv_init.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 182
if hasattr(_libs['comedi'], 'comedi_sv_update'):
    comedi_sv_update = _libs['comedi'].comedi_sv_update
    comedi_sv_update.argtypes = [POINTER(comedi_sv_t)]
    comedi_sv_update.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 183
if hasattr(_libs['comedi'], 'comedi_sv_measure'):
    comedi_sv_measure = _libs['comedi'].comedi_sv_measure
    comedi_sv_measure.argtypes = [POINTER(comedi_sv_t), POINTER(c_double)]
    comedi_sv_measure.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 187
if hasattr(_libs['comedi'], 'comedi_get_cmd_src_mask'):
    comedi_get_cmd_src_mask = _libs['comedi'].comedi_get_cmd_src_mask
    comedi_get_cmd_src_mask.argtypes = [POINTER(comedi_t), c_uint, POINTER(comedi_cmd)]
    comedi_get_cmd_src_mask.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 189
if hasattr(_libs['comedi'], 'comedi_get_cmd_generic_timed'):
    comedi_get_cmd_generic_timed = _libs['comedi'].comedi_get_cmd_generic_timed
    comedi_get_cmd_generic_timed.argtypes = [POINTER(comedi_t), c_uint, POINTER(comedi_cmd), c_uint, c_uint]
    comedi_get_cmd_generic_timed.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 191
if hasattr(_libs['comedi'], 'comedi_cancel'):
    comedi_cancel = _libs['comedi'].comedi_cancel
    comedi_cancel.argtypes = [POINTER(comedi_t), c_uint]
    comedi_cancel.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 192
if hasattr(_libs['comedi'], 'comedi_command'):
    comedi_command = _libs['comedi'].comedi_command
    comedi_command.argtypes = [POINTER(comedi_t), POINTER(comedi_cmd)]
    comedi_command.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 193
if hasattr(_libs['comedi'], 'comedi_command_test'):
    comedi_command_test = _libs['comedi'].comedi_command_test
    comedi_command_test.argtypes = [POINTER(comedi_t), POINTER(comedi_cmd)]
    comedi_command_test.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 194
if hasattr(_libs['comedi'], 'comedi_poll'):
    comedi_poll = _libs['comedi'].comedi_poll
    comedi_poll.argtypes = [POINTER(comedi_t), c_uint]
    comedi_poll.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 198
if hasattr(_libs['comedi'], 'comedi_set_max_buffer_size'):
    comedi_set_max_buffer_size = _libs['comedi'].comedi_set_max_buffer_size
    comedi_set_max_buffer_size.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_set_max_buffer_size.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 200
if hasattr(_libs['comedi'], 'comedi_get_buffer_contents'):
    comedi_get_buffer_contents = _libs['comedi'].comedi_get_buffer_contents
    comedi_get_buffer_contents.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_buffer_contents.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 201
if hasattr(_libs['comedi'], 'comedi_mark_buffer_read'):
    comedi_mark_buffer_read = _libs['comedi'].comedi_mark_buffer_read
    comedi_mark_buffer_read.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_mark_buffer_read.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 203
if hasattr(_libs['comedi'], 'comedi_mark_buffer_written'):
    comedi_mark_buffer_written = _libs['comedi'].comedi_mark_buffer_written
    comedi_mark_buffer_written.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_mark_buffer_written.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 205
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_get_buffer_read_offset'):
        continue
    comedi_get_buffer_read_offset = _lib.comedi_get_buffer_read_offset
    comedi_get_buffer_read_offset.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_buffer_read_offset.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 206
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_get_buffer_write_offset'):
        continue
    comedi_get_buffer_write_offset = _lib.comedi_get_buffer_write_offset
    comedi_get_buffer_write_offset.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_buffer_write_offset.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 207
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_get_buffer_read_count'):
        continue
    comedi_get_buffer_read_count = _lib.comedi_get_buffer_read_count
    comedi_get_buffer_read_count.argtypes = [POINTER(comedi_t), c_uint, POINTER(c_uint)]
    comedi_get_buffer_read_count.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 209
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_get_buffer_write_count'):
        continue
    comedi_get_buffer_write_count = _lib.comedi_get_buffer_write_count
    comedi_get_buffer_write_count.argtypes = [POINTER(comedi_t), c_uint, POINTER(c_uint)]
    comedi_get_buffer_write_count.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 213
if hasattr(_libs['comedi'], 'comedi_get_buffer_offset'):
    comedi_get_buffer_offset = _libs['comedi'].comedi_get_buffer_offset
    comedi_get_buffer_offset.argtypes = [POINTER(comedi_t), c_uint]
    comedi_get_buffer_offset.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 242
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'subdevice',
    'channel',
    'value',
]
struct_anon_9._fields_ = [
    ('subdevice', c_uint),
    ('channel', c_uint),
    ('value', c_uint),
]

comedi_caldac_t = struct_anon_9 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 242

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 249
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'coefficients',
    'expansion_origin',
    'order',
]
struct_anon_10._fields_ = [
    ('coefficients', c_double * 4),
    ('expansion_origin', c_double),
    ('order', c_uint),
]

comedi_polynomial_t = struct_anon_10 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 249

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 254
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'to_phys',
    'from_phys',
]
struct_anon_11._fields_ = [
    ('to_phys', POINTER(comedi_polynomial_t)),
    ('from_phys', POINTER(comedi_polynomial_t)),
]

comedi_softcal_t = struct_anon_11 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 254

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 268
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'subdevice',
    'channels',
    'num_channels',
    'ranges',
    'num_ranges',
    'arefs',
    'num_arefs',
    'caldacs',
    'num_caldacs',
    'soft_calibration',
]
struct_anon_12._fields_ = [
    ('subdevice', c_uint),
    ('channels', POINTER(c_uint)),
    ('num_channels', c_uint),
    ('ranges', POINTER(c_uint)),
    ('num_ranges', c_uint),
    ('arefs', c_uint * 4),
    ('num_arefs', c_uint),
    ('caldacs', POINTER(comedi_caldac_t)),
    ('num_caldacs', c_uint),
    ('soft_calibration', comedi_softcal_t),
]

comedi_calibration_setting_t = struct_anon_12 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 268

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 276
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'driver_name',
    'board_name',
    'settings',
    'num_settings',
]
struct_anon_13._fields_ = [
    ('driver_name', String),
    ('board_name', String),
    ('settings', POINTER(comedi_calibration_setting_t)),
    ('num_settings', c_uint),
]

comedi_calibration_t = struct_anon_13 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 276

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 278
if hasattr(_libs['comedi'], 'comedi_parse_calibration_file'):
    comedi_parse_calibration_file = _libs['comedi'].comedi_parse_calibration_file
    comedi_parse_calibration_file.argtypes = [String]
    comedi_parse_calibration_file.restype = POINTER(comedi_calibration_t)

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 279
if hasattr(_libs['comedi'], 'comedi_apply_parsed_calibration'):
    comedi_apply_parsed_calibration = _libs['comedi'].comedi_apply_parsed_calibration
    comedi_apply_parsed_calibration.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, POINTER(comedi_calibration_t)]
    comedi_apply_parsed_calibration.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 281
if hasattr(_libs['comedi'], 'comedi_get_default_calibration_path'):
    comedi_get_default_calibration_path = _libs['comedi'].comedi_get_default_calibration_path
    comedi_get_default_calibration_path.argtypes = [POINTER(comedi_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        comedi_get_default_calibration_path.restype = ReturnString
    else:
        comedi_get_default_calibration_path.restype = String
        comedi_get_default_calibration_path.errcheck = ReturnString

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 282
if hasattr(_libs['comedi'], 'comedi_cleanup_calibration'):
    comedi_cleanup_calibration = _libs['comedi'].comedi_cleanup_calibration
    comedi_cleanup_calibration.argtypes = [POINTER(comedi_calibration_t)]
    comedi_cleanup_calibration.restype = None

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 283
if hasattr(_libs['comedi'], 'comedi_apply_calibration'):
    comedi_apply_calibration = _libs['comedi'].comedi_apply_calibration
    comedi_apply_calibration.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, String]
    comedi_apply_calibration.restype = c_int

enum_comedi_conversion_direction = c_int # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 288

COMEDI_TO_PHYSICAL = 0 # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 288

COMEDI_FROM_PHYSICAL = (COMEDI_TO_PHYSICAL + 1) # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 288

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 293
if hasattr(_libs['comedi'], 'comedi_get_softcal_converter'):
    comedi_get_softcal_converter = _libs['comedi'].comedi_get_softcal_converter
    comedi_get_softcal_converter.argtypes = [c_uint, c_uint, c_uint, enum_comedi_conversion_direction, POINTER(comedi_calibration_t), POINTER(comedi_polynomial_t)]
    comedi_get_softcal_converter.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 297
if hasattr(_libs['comedi'], 'comedi_get_hardcal_converter'):
    comedi_get_hardcal_converter = _libs['comedi'].comedi_get_hardcal_converter
    comedi_get_hardcal_converter.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, enum_comedi_conversion_direction, POINTER(comedi_polynomial_t)]
    comedi_get_hardcal_converter.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 300
if hasattr(_libs['comedi'], 'comedi_to_physical'):
    comedi_to_physical = _libs['comedi'].comedi_to_physical
    comedi_to_physical.argtypes = [lsampl_t, POINTER(comedi_polynomial_t)]
    comedi_to_physical.restype = c_double

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 302
if hasattr(_libs['comedi'], 'comedi_from_physical'):
    comedi_from_physical = _libs['comedi'].comedi_from_physical
    comedi_from_physical.argtypes = [c_double, POINTER(comedi_polynomial_t)]
    comedi_from_physical.restype = lsampl_t

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 305
if hasattr(_libs['comedi'], 'comedi_internal_trigger'):
    comedi_internal_trigger = _libs['comedi'].comedi_internal_trigger
    comedi_internal_trigger.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_internal_trigger.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 307
if hasattr(_libs['comedi'], 'comedi_arm'):
    comedi_arm = _libs['comedi'].comedi_arm
    comedi_arm.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_arm.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 308
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_arm_channel'):
        continue
    comedi_arm_channel = _lib.comedi_arm_channel
    comedi_arm_channel.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint]
    comedi_arm_channel.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 310
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_disarm'):
        continue
    comedi_disarm = _lib.comedi_disarm
    comedi_disarm.argtypes = [POINTER(comedi_t), c_uint]
    comedi_disarm.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 311
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_disarm_channel'):
        continue
    comedi_disarm_channel = _lib.comedi_disarm_channel
    comedi_disarm_channel.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_disarm_channel.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 313
if hasattr(_libs['comedi'], 'comedi_reset'):
    comedi_reset = _libs['comedi'].comedi_reset
    comedi_reset.argtypes = [POINTER(comedi_t), c_uint]
    comedi_reset.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 314
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_reset_channel'):
        continue
    comedi_reset_channel = _lib.comedi_reset_channel
    comedi_reset_channel.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_reset_channel.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 316
if hasattr(_libs['comedi'], 'comedi_get_clock_source'):
    comedi_get_clock_source = _libs['comedi'].comedi_get_clock_source
    comedi_get_clock_source.argtypes = [POINTER(comedi_t), c_uint, c_uint, POINTER(c_uint), POINTER(c_uint)]
    comedi_get_clock_source.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 317
if hasattr(_libs['comedi'], 'comedi_get_gate_source'):
    comedi_get_gate_source = _libs['comedi'].comedi_get_gate_source
    comedi_get_gate_source.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, POINTER(c_uint)]
    comedi_get_gate_source.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 319
if hasattr(_libs['comedi'], 'comedi_get_routing'):
    comedi_get_routing = _libs['comedi'].comedi_get_routing
    comedi_get_routing.argtypes = [POINTER(comedi_t), c_uint, c_uint, POINTER(c_uint)]
    comedi_get_routing.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 320
if hasattr(_libs['comedi'], 'comedi_set_counter_mode'):
    comedi_set_counter_mode = _libs['comedi'].comedi_set_counter_mode
    comedi_set_counter_mode.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint]
    comedi_set_counter_mode.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 321
if hasattr(_libs['comedi'], 'comedi_set_clock_source'):
    comedi_set_clock_source = _libs['comedi'].comedi_set_clock_source
    comedi_set_clock_source.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint]
    comedi_set_clock_source.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 322
if hasattr(_libs['comedi'], 'comedi_set_filter'):
    comedi_set_filter = _libs['comedi'].comedi_set_filter
    comedi_set_filter.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint]
    comedi_set_filter.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 323
if hasattr(_libs['comedi'], 'comedi_set_gate_source'):
    comedi_set_gate_source = _libs['comedi'].comedi_set_gate_source
    comedi_set_gate_source.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint]
    comedi_set_gate_source.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 324
if hasattr(_libs['comedi'], 'comedi_set_other_source'):
    comedi_set_other_source = _libs['comedi'].comedi_set_other_source
    comedi_set_other_source.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint]
    comedi_set_other_source.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 326
if hasattr(_libs['comedi'], 'comedi_set_routing'):
    comedi_set_routing = _libs['comedi'].comedi_set_routing
    comedi_set_routing.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint]
    comedi_set_routing.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 327
if hasattr(_libs['comedi'], 'comedi_get_hardware_buffer_size'):
    comedi_get_hardware_buffer_size = _libs['comedi'].comedi_get_hardware_buffer_size
    comedi_get_hardware_buffer_size.argtypes = [POINTER(comedi_t), c_uint, enum_comedi_io_direction]
    comedi_get_hardware_buffer_size.restype = c_int

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 328
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_digital_trigger_disable'):
        continue
    comedi_digital_trigger_disable = _lib.comedi_digital_trigger_disable
    comedi_digital_trigger_disable.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_digital_trigger_disable.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 330
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_digital_trigger_enable_edges'):
        continue
    comedi_digital_trigger_enable_edges = _lib.comedi_digital_trigger_enable_edges
    comedi_digital_trigger_enable_edges.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, c_uint]
    comedi_digital_trigger_enable_edges.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 333
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_digital_trigger_enable_levels'):
        continue
    comedi_digital_trigger_enable_levels = _lib.comedi_digital_trigger_enable_levels
    comedi_digital_trigger_enable_levels.argtypes = [POINTER(comedi_t), c_uint, c_uint, c_uint, c_uint, c_uint]
    comedi_digital_trigger_enable_levels.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 371
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_get_cmd_timing_constraints'):
        continue
    comedi_get_cmd_timing_constraints = _lib.comedi_get_cmd_timing_constraints
    comedi_get_cmd_timing_constraints.argtypes = [POINTER(comedi_t), c_uint, c_uint, POINTER(c_uint), c_uint, POINTER(c_uint), POINTER(c_uint), c_uint]
    comedi_get_cmd_timing_constraints.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 398
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_test_route'):
        continue
    comedi_test_route = _lib.comedi_test_route
    comedi_test_route.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_test_route.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 418
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_connect_route'):
        continue
    comedi_connect_route = _lib.comedi_connect_route
    comedi_connect_route.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_connect_route.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 430
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_disconnect_route'):
        continue
    comedi_disconnect_route = _lib.comedi_disconnect_route
    comedi_disconnect_route.argtypes = [POINTER(comedi_t), c_uint, c_uint]
    comedi_disconnect_route.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 451
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'comedi_get_routes'):
        continue
    comedi_get_routes = _lib.comedi_get_routes
    comedi_get_routes.argtypes = [POINTER(comedi_t), POINTER(comedi_route_pair), c_size_t]
    comedi_get_routes.restype = c_int
    break

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 35
try:
    COMEDI_MAJOR = 98
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 42
try:
    COMEDI_NDEVICES = 16
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 45
try:
    COMEDI_NDEVCONFOPTS = 32
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 61
try:
    COMEDI_DEVCONF_AUX_DATA3_LENGTH = 25
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 62
try:
    COMEDI_DEVCONF_AUX_DATA2_LENGTH = 26
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 63
try:
    COMEDI_DEVCONF_AUX_DATA1_LENGTH = 27
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 64
try:
    COMEDI_DEVCONF_AUX_DATA0_LENGTH = 28
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 66
try:
    COMEDI_DEVCONF_AUX_DATA_HI = 29
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 68
try:
    COMEDI_DEVCONF_AUX_DATA_LO = 30
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 69
try:
    COMEDI_DEVCONF_AUX_DATA_LENGTH = 31
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 72
try:
    COMEDI_NAMELEN = 20
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 79
def CR_PACK(chan, rng, aref):
    return ((((aref & 3) << 24) | ((rng & 255) << 16)) | chan)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 81
def CR_PACK_FLAGS(chan, range, aref, flags):
    return ((CR_PACK (chan, range, aref)) | (flags & CR_FLAGS_MASK))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 84
def CR_CHAN(a):
    return (a & 65535)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 85
def CR_RANGE(a):
    return ((a >> 16) & 255)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 86
def CR_AREF(a):
    return ((a >> 24) & 3)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 88
try:
    CR_FLAGS_MASK = 4227858432
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 89
try:
    CR_ALT_FILTER = 67108864
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 90
try:
    CR_DITHER = CR_ALT_FILTER
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 91
try:
    CR_DEGLITCH = CR_ALT_FILTER
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 92
try:
    CR_ALT_SOURCE = 134217728
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 93
try:
    CR_EDGE = 1073741824
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 94
try:
    CR_INVERT = 2147483648
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 96
try:
    AREF_GROUND = 0
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 97
try:
    AREF_COMMON = 1
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 98
try:
    AREF_DIFF = 2
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 99
try:
    AREF_OTHER = 3
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 102
try:
    GPCT_RESET = 1
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 103
try:
    GPCT_SET_SOURCE = 2
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 104
try:
    GPCT_SET_GATE = 4
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 105
try:
    GPCT_SET_DIRECTION = 8
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 106
try:
    GPCT_SET_OPERATION = 16
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 107
try:
    GPCT_ARM = 32
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 108
try:
    GPCT_DISARM = 64
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 109
try:
    GPCT_GET_INT_CLK_FRQ = 128
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 111
try:
    GPCT_INT_CLOCK = 1
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 112
try:
    GPCT_EXT_PIN = 2
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 113
try:
    GPCT_NO_GATE = 4
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 114
try:
    GPCT_UP = 8
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 115
try:
    GPCT_DOWN = 16
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 116
try:
    GPCT_HWUD = 32
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 117
try:
    GPCT_SIMPLE_EVENT = 64
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 118
try:
    GPCT_SINGLE_PERIOD = 128
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 119
try:
    GPCT_SINGLE_PW = 256
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 120
try:
    GPCT_CONT_PULSE_OUT = 512
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 121
try:
    GPCT_SINGLE_PULSE_OUT = 1024
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 125
try:
    INSN_MASK_WRITE = 134217728
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 126
try:
    INSN_MASK_READ = 67108864
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 127
try:
    INSN_MASK_SPECIAL = 33554432
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 129
try:
    INSN_READ = (0 | INSN_MASK_READ)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 130
try:
    INSN_WRITE = (1 | INSN_MASK_WRITE)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 131
try:
    INSN_BITS = ((2 | INSN_MASK_READ) | INSN_MASK_WRITE)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 132
try:
    INSN_CONFIG = ((3 | INSN_MASK_READ) | INSN_MASK_WRITE)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 133
try:
    INSN_DEVICE_CONFIG = (INSN_CONFIG | INSN_MASK_SPECIAL)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 134
try:
    INSN_GTOD = ((4 | INSN_MASK_READ) | INSN_MASK_SPECIAL)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 135
try:
    INSN_WAIT = ((5 | INSN_MASK_WRITE) | INSN_MASK_SPECIAL)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 136
try:
    INSN_INTTRIG = ((6 | INSN_MASK_WRITE) | INSN_MASK_SPECIAL)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 141
try:
    CMDF_BOGUS = 1
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 144
try:
    CMDF_PRIORITY = 8
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 147
try:
    CMDF_WAKE_EOS = 32
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 149
try:
    CMDF_WRITE = 64
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 151
try:
    CMDF_RAWDATA = 128
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 154
try:
    CMDF_ROUND_MASK = 196608
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 155
try:
    CMDF_ROUND_NEAREST = 0
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 156
try:
    CMDF_ROUND_DOWN = 65536
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 157
try:
    CMDF_ROUND_UP = 131072
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 158
try:
    CMDF_ROUND_UP_NEXT = 196608
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 160
try:
    COMEDI_EV_START = 262144
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 161
try:
    COMEDI_EV_SCAN_BEGIN = 524288
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 162
try:
    COMEDI_EV_CONVERT = 1048576
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 163
try:
    COMEDI_EV_SCAN_END = 2097152
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 164
try:
    COMEDI_EV_STOP = 4194304
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 167
try:
    TRIG_BOGUS = CMDF_BOGUS
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 168
try:
    TRIG_RT = CMDF_PRIORITY
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 169
try:
    TRIG_WAKE_EOS = CMDF_WAKE_EOS
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 170
try:
    TRIG_WRITE = CMDF_WRITE
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 171
try:
    TRIG_ROUND_MASK = CMDF_ROUND_MASK
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 172
try:
    TRIG_ROUND_NEAREST = CMDF_ROUND_NEAREST
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 173
try:
    TRIG_ROUND_DOWN = CMDF_ROUND_DOWN
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 174
try:
    TRIG_ROUND_UP = CMDF_ROUND_UP
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 175
try:
    TRIG_ROUND_UP_NEXT = CMDF_ROUND_UP_NEXT
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 179
try:
    TRIG_ANY = 4294967295
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 180
try:
    TRIG_INVALID = 0
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 182
try:
    TRIG_NONE = 1
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 183
try:
    TRIG_NOW = 2
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 184
try:
    TRIG_FOLLOW = 4
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 185
try:
    TRIG_TIME = 8
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 186
try:
    TRIG_TIMER = 16
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 187
try:
    TRIG_COUNT = 32
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 188
try:
    TRIG_EXT = 64
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 189
try:
    TRIG_INT = 128
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 190
try:
    TRIG_OTHER = 256
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 194
try:
    SDF_BUSY = 1
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 195
try:
    SDF_BUSY_OWNER = 2
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 196
try:
    SDF_LOCKED = 4
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 197
try:
    SDF_LOCK_OWNER = 8
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 198
try:
    SDF_MAXDATA = 16
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 199
try:
    SDF_FLAGS = 32
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 200
try:
    SDF_RANGETYPE = 64
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 201
try:
    SDF_PWM_COUNTER = 128
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 202
try:
    SDF_PWM_HBRIDGE = 256
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 203
try:
    SDF_CMD = 4096
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 204
try:
    SDF_SOFT_CALIBRATED = 8192
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 205
try:
    SDF_CMD_WRITE = 16384
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 206
try:
    SDF_CMD_READ = 32768
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 209
try:
    SDF_READABLE = 65536
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 211
try:
    SDF_WRITABLE = 131072
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 212
try:
    SDF_WRITEABLE = SDF_WRITABLE
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 214
try:
    SDF_INTERNAL = 262144
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 215
try:
    SDF_GROUND = 1048576
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 216
try:
    SDF_COMMON = 2097152
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 217
try:
    SDF_DIFF = 4194304
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 218
try:
    SDF_OTHER = 8388608
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 219
try:
    SDF_DITHER = 16777216
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 220
try:
    SDF_DEGLITCH = 33554432
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 221
try:
    SDF_MMAP = 67108864
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 222
try:
    SDF_RUNNING = 134217728
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 223
try:
    SDF_LSAMPL = 268435456
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 224
try:
    SDF_PACKED = 536870912
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 479
try:
    CIO = 'd'
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 485
try:
    COMEDI_LOCK = (_IO (CIO, 5))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 486
try:
    COMEDI_UNLOCK = (_IO (CIO, 6))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 487
try:
    COMEDI_CANCEL = (_IO (CIO, 7))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 495
try:
    COMEDI_POLL = (_IO (CIO, 15))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 496
try:
    COMEDI_SETRSUBD = (_IO (CIO, 16))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 497
try:
    COMEDI_SETWSUBD = (_IO (CIO, 17))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 969
def __RANGE(a, b):
    return (((a & 65535) << 16) | (b & 65535))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 971
def RANGE_OFFSET(a):
    return ((a >> 16) & 65535)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 972
def RANGE_LENGTH(b):
    return (b & 65535)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 974
def RF_UNIT(flags):
    return (flags & 255)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 975
try:
    RF_EXTERNAL = 256
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 977
try:
    UNIT_volt = 0
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 978
try:
    UNIT_mA = 1
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 979
try:
    UNIT_none = 2
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 981
try:
    COMEDI_MIN_SPEED = 4294967295
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1071
try:
    NI_NAMES_BASE = (1 << 15)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1075
def NI_PFI(x):
    return (NI_NAMES_BASE + (x & 63))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1077
def TRIGGER_LINE(x):
    return (((NI_PFI ((-1))) + 1) + (x & 7))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1079
def NI_RTSI_BRD(x):
    return (((TRIGGER_LINE ((-1))) + 1) + (x & 3))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1082
try:
    NI_COUNTER_NAMES_BASE = ((NI_RTSI_BRD ((-1))) + 1)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1083
try:
    NI_MAX_COUNTERS = 7
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1084
def NI_CtrSource(x):
    return (NI_COUNTER_NAMES_BASE + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1086
try:
    NI_GATES_NAMES_BASE = ((NI_CtrSource ((-1))) + 1)
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1087
def NI_CtrGate(x):
    return (NI_GATES_NAMES_BASE + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1088
def NI_CtrAux(x):
    return (((NI_CtrGate ((-1))) + 1) + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1089
def NI_CtrA(x):
    return (((NI_CtrAux ((-1))) + 1) + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1090
def NI_CtrB(x):
    return (((NI_CtrA ((-1))) + 1) + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1091
def NI_CtrZ(x):
    return (((NI_CtrB ((-1))) + 1) + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1092
try:
    NI_GATES_NAMES_MAX = (NI_CtrZ ((-1)))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1093
def NI_CtrArmStartTrigger(x):
    return (((NI_CtrZ ((-1))) + 1) + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1094
def NI_CtrInternalOutput(x):
    return (((NI_CtrArmStartTrigger ((-1))) + 1) + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1097
def NI_CtrOut(x):
    return (((NI_CtrInternalOutput ((-1))) + 1) + (x & NI_MAX_COUNTERS))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1098
try:
    NI_COUNTER_NAMES_MAX = (NI_CtrOut ((-1)))
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1146
def NI_USUAL_PFI_SELECT(x):
    return (x < 10) and (1 + x) or (11 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1147
def NI_USUAL_RTSI_SELECT(x):
    return (x < 7) and (11 + x) or 27

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1153
try:
    NI_GPCT_COUNTING_MODE_SHIFT = 16
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1154
try:
    NI_GPCT_INDEX_PHASE_BITSHIFT = 20
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1155
try:
    NI_GPCT_COUNTING_DIRECTION_SHIFT = 24
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1247
def NI_GPCT_SOURCE_PIN_CLOCK_SRC_BITS(x):
    return (16 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1249
def NI_GPCT_RTSI_CLOCK_SRC_BITS(x):
    return (24 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1252
def NI_GPCT_PFI_CLOCK_SRC_BITS(x):
    return (32 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1283
def NI_GPCT_GATE_PIN_GATE_SELECT(x):
    return (258 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1284
def NI_GPCT_RTSI_GATE_SELECT(x):
    return (NI_USUAL_RTSI_SELECT (x))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1285
def NI_GPCT_PFI_GATE_SELECT(x):
    return (NI_USUAL_PFI_SELECT (x))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1286
def NI_GPCT_UP_DOWN_PIN_GATE_SELECT(x):
    return (514 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1304
def NI_GPCT_PFI_OTHER_SELECT(x):
    return (NI_USUAL_PFI_SELECT (x))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1363
def NI_MIO_PLL_RTSI_CLOCK(x):
    return (NI_MIO_PLL_RTSI0_CLOCK + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1384
def NI_RTSI_OUTPUT_RTSI_BRD(x):
    return (NI_RTSI_OUTPUT_RTSI_BRD_0 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1420
def NI_PFI_OUTPUT_RTSI(x):
    return (NI_PFI_OUTPUT_RTSI0 + x)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1440
def NI_EXT_PFI(x):
    return ((NI_USUAL_PFI_SELECT (x)) - 1)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1441
def NI_EXT_RTSI(x):
    return ((NI_USUAL_RTSI_SELECT (x)) - 1)

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1461
def NI_CDIO_SCAN_BEGIN_SRC_PFI(x):
    return (NI_USUAL_PFI_SELECT (x))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1462
def NI_CDIO_SCAN_BEGIN_SRC_RTSI(x):
    return (NI_USUAL_RTSI_SELECT (x))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1469
def NI_AO_SCAN_BEGIN_SRC_PFI(x):
    return (NI_USUAL_PFI_SELECT (x))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1470
def NI_AO_SCAN_BEGIN_SRC_RTSI(x):
    return (NI_USUAL_RTSI_SELECT (x))

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1576
try:
    SDF_MODE0 = 128
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1577
try:
    SDF_MODE1 = 256
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1578
try:
    SDF_MODE2 = 512
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1579
try:
    SDF_MODE3 = 1024
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1580
try:
    SDF_MODE4 = 2048
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1581
try:
    SDF_RT = 524288
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1586
try:
    TRIG_DITHER = 2
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1587
try:
    TRIG_DEGLITCH = 4
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedi.h: 1588
try:
    TRIG_CONFIG = 16
except:
    pass

# /usr/include/asm-generic/ioctl.h: 22
try:
    _IOC_NRBITS = 8
except:
    pass

# /usr/include/asm-generic/ioctl.h: 23
try:
    _IOC_TYPEBITS = 8
except:
    pass

# /usr/include/asm-generic/ioctl.h: 31
try:
    _IOC_SIZEBITS = 14
except:
    pass

# /usr/include/asm-generic/ioctl.h: 43
try:
    _IOC_NRSHIFT = 0
except:
    pass

# /usr/include/asm-generic/ioctl.h: 44
try:
    _IOC_TYPESHIFT = (_IOC_NRSHIFT + _IOC_NRBITS)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 45
try:
    _IOC_SIZESHIFT = (_IOC_TYPESHIFT + _IOC_TYPEBITS)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 46
try:
    _IOC_DIRSHIFT = (_IOC_SIZESHIFT + _IOC_SIZEBITS)
except:
    pass

# /usr/include/asm-generic/ioctl.h: 54
try:
    _IOC_NONE = 0
except:
    pass

# /usr/include/asm-generic/ioctl.h: 65
def _IOC(dir, type, nr, size):
    return ((((dir << _IOC_DIRSHIFT) | (type << _IOC_TYPESHIFT)) | (nr << _IOC_NRSHIFT)) | (size << _IOC_SIZESHIFT))

# /usr/include/asm-generic/ioctl.h: 74
def _IO(type, nr):
    return (_IOC (_IOC_NONE, type, nr, 0))

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 45
def SWIG_OUTPUT(x):
    return x

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 46
def SWIG_INPUT(x):
    return x

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 47
def SWIG_INOUT(x):
    return x

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 96
def COMEDI_VERSION_CODE(a, b, c):
    return (((a << 16) | (b << 8)) | c)

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 243
try:
    COMEDI_MAX_NUM_POLYNOMIAL_COEFFICIENTS = 4
except:
    pass

# /home/olsonse/src/comedi/comedilib/include/comedilib.h: 255
try:
    CS_MAX_AREFS_LENGTH = 4
except:
    pass

comedi_cmd_struct = struct_comedi_cmd_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 624

comedi_insn_struct = struct_comedi_insn_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 526

comedi_insnlist_struct = struct_comedi_insnlist_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 542

comedi_chaninfo_struct = struct_comedi_chaninfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 668

comedi_subdinfo_struct = struct_comedi_subdinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 819

comedi_devinfo_struct = struct_comedi_devinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 846

comedi_devconfig_struct = struct_comedi_devconfig_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 869

comedi_rangeinfo_struct = struct_comedi_rangeinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 693

comedi_krange_struct = struct_comedi_krange_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 720

comedi_bufconfig_struct = struct_comedi_bufconfig_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 895

comedi_bufinfo_struct = struct_comedi_bufinfo_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 922

comedi_trig_struct = struct_comedi_trig_struct # /home/olsonse/src/comedi/comedilib/include/comedi.h: 1590

comedi_t_struct = struct_comedi_t_struct # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 50

comedi_sv_struct = struct_comedi_sv_struct # /home/olsonse/src/comedi/comedilib/include/comedilib.h: 71

# No inserted files

