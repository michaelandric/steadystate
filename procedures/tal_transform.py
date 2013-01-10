#!/usr/bin/python

import os
from subprocess import call
from optparse import OptionParser

class Transform:

    def get_opts(self):
        desc = """for removing transforming functional files to tlrc from orig space."""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Dec.2012")
        self.parser.add_option("--WorkDir", dest="workdir",
                               help="specify the working directory")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def adwarp_call(self,cc):
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/")
        print os.getcwd()
        apar = self.options.subject+"tlrc+tlrc"
        print call("adwarp -apar "+apar+" -dpar "+self.options.subject+"."+`cc`+".node_roles+orig -dxyz 2 -resam NN", shell=True)


def main():
    TAL = Transform()
    TAL.get_opts()
    for cc in range(1,5):
        TAL.adwarp_call(cc)


if __name__ == "__main__":
    main()
