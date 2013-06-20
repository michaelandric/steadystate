#!/usr/bin/python

"""
XYZ are spatial indices. 
"""

import os
from optparse import OptionParser
from subprocess import call

class XYZproc:

    def get_opts(self):
        desc = """simple program for doing 3dUndump"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Sep.2012")
        self.parser.add_option("--automask", dest="amask",
                               help="set the automask")
        self.parser.add_option("--xyzmaster", dest="xyzmstr",
                               help="file with xyz functional coordinates")
        self.parser.add_option("--xyzoutputname", dest="xyzout",
                               help="output name")

        (self.options, args) = self.parser.parse_args()

    def get_xyz(self):
        """Grab the xyz coords"""
        print call("3dmaskdump -xyz -noijk -mask "+self.options.amask+" "+self.options.xyzmstr+" | awk '{print $1, $2, $3}' > "+self.options.xyzout, shell=True)



XYZ = XYZproc()
XYZ.get_opts()
XYZ.get_xyz()
