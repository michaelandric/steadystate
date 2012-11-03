#!/usr/bin/python

import os
from optparse import OptionParser

class Maker:

    def get_opts(self):
        desc = """simple program to make directories"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog October.2012")
        self.parser.add_option("--OutDir", dest="outdir",
                               help="specify the output directory")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def make_dir(self):
        newdir = os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR"
        if not os.path.exists(newdir):
            os.makedirs(newdir)



M = Maker()
M.get_opts()
M.make_dir()

