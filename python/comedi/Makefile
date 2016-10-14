TOP=../..

ctypesgen_comedi.py : $(TOP)/include/comedi.h $(TOP)/include/comedilib.h
	ctypesgen.py -lcomedi -R $(TOP)/lib/.libs/ \
		$(TOP)/include/comedi.h $(TOP)/include/comedilib.h -o $@
