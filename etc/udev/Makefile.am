EXTRA_DIST = 90-comedi.rules 90-comedi-rules-group.in z99_comedi.rules

if INSTALL_UDEVHOTPLUG

if USE_UDEV_GROUP
udevrules_DATA = 90-comedi-group.rules
else
udevrules_DATA = 90-comedi.rules
endif

udevscripts_SCRIPTS =

else

udevrules_SCRIPTS =

udevscripts_SCRIPTS =

endif
