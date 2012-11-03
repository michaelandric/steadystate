#!/usr/bin/python

import os
from optparse import OptionParser

class IJKproc:

    def get_opts(self):
        desc = """simple program for doing 3dUndump"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Sep.2012")
        self.parser.add_option("--automask", dest="amask",
                               help="set the automask")
        self.parser.add_option("--ijkmaster", dest="ijkmstr",
                               help="file with ijk functional coordinates")
        self.parser.add_option("--ijkoutputname", dest="ijkout",
                               help="output name")

        (self.options, args) = self.parser.parse_args()

    def get_ijk(self):
        print os.system("3dmaskdump -mask "+self.options.amask+" "+self.options.ijkmstr+" | awk '{print $1, $2, $3}' > "+self.options.ijkout)



IJK = IJKproc()
IJK.get_opts()
IJK.get_ijk()
