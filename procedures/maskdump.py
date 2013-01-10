#!/usr/bin/python

import os
from subprocess import call
from optparse import OptionParser
from adwarp_mask import adwarp_call

class Maskdump:

    def get_opts(self):
        desc = """simple program for doing 3dmaskdump"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Nov.2012")
        self.parser.add_option("--ijk", dest="ijk",
                               help="specify 'yes' or 'no' whether to use 'ijk'")
        self.parser.add_option("--mask", dest="inputmask",
                               help="mask to be used")
        self.parser.add_option("--inputfile", dest="input",
                               help="input file")
        self.parser.add_option("--outputname", dest="outname",
                               help="output name")
        self.parser.add_option("--subject", dest="subject",
                               help="Subject identifier")

        (self.options, args) = self.parser.parse_args()
        

    def dump(self):
        print call("3dmaskdump -mask "+self.options.inputmask+" "+self.options.input+" > "+self.options.outname, shell=True)


def main():
    Md = Maskdump()
    Md.get_opts()
    #adwarp_call(Md.options.subject)
    Md.dump()

if __name__ == "__main__":
    main()
