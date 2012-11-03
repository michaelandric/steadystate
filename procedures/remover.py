#!/usr/bin/python

import os
import glob
from optparse import OptionParser

class Remover:

    def get_opts(self):
        desc = """simple program for removing CorrTask* files after building them as a matrix binary files."""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 13.October.2012")
        self.parser.add_option("--WorkDir", dest="workdir",
                               help="specify the working directory")
#        self.parser.add_option("--Condition", dest="Cond",
#                               help="specify the condition number")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def removeFiles(self):
        for filename in glob.glob(self.options.workdir+"/CorrTask*."+self.options.subject+"noijk.txt"):
            os.remove(filename)



RM = Remover()
RM.get_opts()
RM.removeFiles()


