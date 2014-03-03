#!/usr/bin/python

import os
from optparse import OptionParser

class Transform:

    def get_opts(self):
        desc = """simple program for doing trimming the time series"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 8.Nov.2012")
        self.parser.add_option("--tlrc_brain", dest="tlrcT1",
                               help="specify the talairach anat")
        self.parser.add_option("--input", dest="input",
                               help="specify the input")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def transform_indv(self):
        os.chdir(os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/"))
        nn = ""
        for i in range(self.options.nvox):
            nn += `i`+"\n"

        tal_coords = open("","r")
