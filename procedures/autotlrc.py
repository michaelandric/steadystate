#!/usr/bin/python

import os
from optparse import OptionParser

class AutoTLRC:

    def get_opts(self):
        desc = """simple program for doing trimming the time series"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 10.October.2012")
        self.parser.add_option("--tlrc_brain", dest="tlrcT1",
                               help="specify the talairach anat")
        self.parser.add_option("--input", dest="input",
                               help="specify the input")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def auto_tlrc_ex(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/")
        for cc in range(1,5):
            print os.system("@auto_tlrc -apar "+self.options.tlrcT1+" -input "+self.options.subject+"."+`cc`+".degrees.ijkSHORT+orig -dxyz 2")

    def index_auto_tlrc(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject)
        print os.system("@auto_tlrc -apar corrTRIM_BLUR/"+self.options.tlrcT1+" -input "+self.options.subject+"voxel_index.ijk+orig -dxyz 2")


atlrc = AutoTLRC()
atlrc.get_opts()
atlrc.index_auto_tlrc()

