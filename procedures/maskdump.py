#!/usr/bin/python

import os
from optparse import OptionParser

class Maskdump:

    def get_opts(self):
        desc = """simple program for doing 3dmaskdump"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Dec.2010")
        self.parser.add_option("--ijk", dest="ijk",
                               help="specify 'yes' or 'no' whether to use 'ijk'")
        self.parser.add_option("--automask", dest="amask",
                               help="automask file")
        self.parser.add_option("--inputfile", dest="input",
                               help="input file")
        self.parser.add_option("--outputname", dest="outname",
                               help="output name")

        (self.options, args) = self.parser.parse_args()
        

    def dump(self):
        print os.system("3dmaskdump -mask "+self.options.amask+" "+self.options.input+" > "+self.options.outname)



Md = Maskdump()
Md.get_opts()
Md.dump()

