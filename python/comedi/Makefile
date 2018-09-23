TOP=../..

clib.py : $(TOP)/include/comedi.h $(TOP)/include/comedilib.h
	ctypesgen -lcomedi --compile-libdir $(TOP)/lib/.libs/ -I $(TOP)/include \
		$(TOP)/include/comedi.h $(TOP)/include/comedilib.h -o $@
