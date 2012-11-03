#!/usr/bin/python

import os
from optparse import OptionParser

class SpliceTS:

    def get_opts(self):
        desc = """simple program for doing trimming the time series"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 10.October.2012")
        self.parser.add_option("--OutDir", dest="outdir",
                               help="specify the output directory")
        self.parser.add_option("--Condition", dest="Cond",
                               help="specify the condition number")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def splicer(self):
        print os.system("3dTcat -prefix "+self.options.outdir+"/blur."+self.options.Cond+"."+self.options.subject+".steadystate.TRIM \
                        -verb "+self.options.outdir+"/'blur."+self.options.Cond+"."+self.options.subject+".steadystate+orig.BRIK[10-99]'")

    def motion_splicer(self):
        print os.system("cat "+self.options.outdir+"/motion."+self.options.Cond+"."+self.options.subject+".steadystate | tail -n 90 > "+self.options.outdir+"/motion."+self.options.Cond+"."+self.options.subject+".steadystate.TRIM")


Sp = SpliceTS()
Sp.get_opts()
Sp.splicer()
Sp.motion_splicer()

