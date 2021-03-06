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
            print call("@auto_tlrc -apar "+self.options.tlrcT1+" -input "+self.options.subject+"."+`cc`+".node_roles+orig -dxyz 2", shell=True)

    def index_auto_tlrc_ex(self):
        """
        This was used to get index values, i.e., correspond voxel number in orig to tlrc space.
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/masking/")
        apar = os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/"+self.options.tlrcT1
        input = self.options.subject+"graymatter_voxel_index.ijk+orig"
        print call("@auto_tlrc -apar "+apar+" -input "+input+" -dxyz 2", shell=True)

    def mask_auto_tlrc_ex(self):
        """
        This is used to talairach the graymatter mask
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/masking/")
        graymask = self.options.subject+"_graymattermask_resampled+orig"
        tlrcbrain = os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/"+self.options.tlrcT1
        print call("@auto_tlrc -apar "+tlrcbrain+" -input "+graymask+" -dxyz 2", shell=True)

    def TS_tlrc(self):
        """
        Use this to auto_tlrc the time series
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/")
        for cc in range(1,5):
            print call("@auto_tlrc -apar "+self.options.tlrcT1+" -input cleanTS.masked.Cond"+`cc`+"."+self.options.subject+"+orig -dxyz 2", shell=True)

    def pres_tlrc_ex(self):
        """
        Mapping the preserved files (that index Within Module Set Consistency)
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/")
        tlrcbrain = os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/"+self.options.tlrcT1
        presbrain = "preserved_"+self.options.subject+"+orig"
        print call("@auto_tlrc -apar "+tlrcbrain+" -input "+presbrain+" -dxyz 2", shell=True)


def main():
    atlrc = AutoTLRC()
    atlrc.get_opts()
    atlrc.pres_tlrc_ex()

if __name__ == "__main__":
    main()

