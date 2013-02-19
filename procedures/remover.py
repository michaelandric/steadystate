#!/usr/bin/python

import os
from glob import glob 
from optparse import OptionParser

class Remover:

    def get_opts(self):
        desc = """simple program for removing CorrTask* files after building them as a matrix binary files."""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Dec.2012")
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

    def remover2(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/masking/")
        print os.getcwd()
        for filename in glob(self.options.subject+"_graymattermask+tlrc.*"):
            os.remove(filename)

    def remover3(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/")
        print os.getcwd()
        for filename in glob(self.options.subject+"*.node_roles_tlrc_dump.txt"):
            os.remove(filename)

    def remover4(self):
        """
        This is to remove the old *noijk_dump* files.
        These files included white matter in the cortical mask.
        Need to make more space on the filesystem.
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/")
        print os.getcwd()
        for filename in glob("*"+self.options.subject+".noijk_dump*"):
            os.remove(filename)



RM = Remover()
RM.get_opts()
RM.remover4()


