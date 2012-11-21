#!/usr/bin/python

import os
from subprocess import call
from optparse import OptionParser

class AutoTLRC:

    def get_opts(self):
        desc = """
        simple program for doing trimming the time series
        """
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Nov.2012")
        self.parser.add_option("--tlrc_brain", dest="tlrcT1",
                               help="specify the talairach anat")
        self.parser.add_option("--input", dest="input",
                               help="specify the input")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def auto_tlrc_ex(self):
        """
        This is the main function that iterates across the 4 conditions
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/")
        for cc in range(1,5):
            print call("@auto_tlrc -apar "+self.options.tlrcT1+" -input "+self.options.subject+"."+`cc`+".degrees_gray+orig -dxyz 2", shell=True)

    def index_auto_tlrc(self):
        """
        This was used to get index values, i.e., correspond voxel number in orig to tlrc space.
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject)
        print call("@auto_tlrc -apar corrTRIM_BLUR/"+self.options.tlrcT1+" -input "+self.options.subject+"voxel_index.ijk+orig -dxyz 2", shell=True)


def main():
    atlrc = AutoTLRC()
    atlrc.get_opts()
    atlrc.auto_tlrc_ex()

if __name__ == "__main__":
    main()

