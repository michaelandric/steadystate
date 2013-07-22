#!/usr/bin/python

import os
from subprocess import call
from optparse import OptionParser

class BCT_Corr:

    def get_opts(self):
        desc = """
        This is for doing N x N correlation.
        """
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Nov.2012")
        self.parser.add_option("--subject", dest="subj",
                          help="specify subject identifier")
        self.parser.add_option("--source_directory", dest="sourceD",
                               help="directory where the source files are")
        self.parser.add_option("--output_directory", dest="outD",
                               help="directory where you want the output to go")
        self.parser.add_option("--mask", dest="dumpmask",
                               help="what mask do you want to use in 3dmaskdump. Must give full path.")
        self.parser.add_option("--condition", dest="cc",
                               help="Give the condition identifier, e.g., '1'")


        (self.options, args) = self.parser.parse_args()


    def maskdump(self):
    	"""
    	Used to dump the AFNI time series to a next file, ready for fcorr to a text file.
    	"""
        print "The out directory is: "+self.options.outD
        os.chdir(self.options.outD)
        print "Working in :"+os.getcwd()
        print call("3dmaskdump -mask /mnt/tier2/urihas/Andric/steadystate/groupstats/automask_d1_TTavg152T1+tlrc -noijk "+self.options.outD+"cleanTS.masked.Cond"+self.options.cc+"."+self.options.subj+"+tlrc.BRIK  > "+self.options.outD+"cleanTS."+self.options.cc+"."+self.options.subj+"_graymask_dump_tlrc", shell=True)

    def callR(self):
    	"""
    	This calls the R script with fcorr.
    	"""
        inputf = self.options.outD+"cleanTS."+self.options.cc+"."+self.options.subj+"_graymask_dump_tlrc"
        f = open(inputf,'r')
        lines = f.readlines()
        nvox = len([l for l in lines if l.strip(' \n') != ''])
        print os.getcwd()
        os.environ["R_ARGS"] = inputf+" "+`nvox`
        print call("R CMD BATCH --vanilla "+os.environ["state"]+"/codebase/modularity_conn/bct_fcorr.R", shell=True)


def main():
    """
    Not going to re-run 3dDeconvolve
    Only need to dump that output via the new graymatter mask
    """
    bct = BCT_Corr()
    bct.get_opts()
    bct.maskdump()
    bct.callR()

if __name__ == "__main__":
    main()

