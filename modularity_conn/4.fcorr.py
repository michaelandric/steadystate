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

    def deconvolve(self):
		"""
		This is used to clean the time series. Here, I regress against the motion series. The 'error' time series is then the cleaned.
		""" 
        print "The out directory is: "+self.options.outD
        os.chdir(self.options.self.options.outD)
        print "Working in :"+os.getcwd()
        print call("3dDeconvolve -input "+self.options.sourceD+"blur."+self.options.cc+"."+self.options.subj+".steadystate.TRIM+orig. -polort A -num_stimts 6 \
                        -stim_file 1 "+self.options.sourceD+"motion."+self.options.cc+"."+self.options.subj+".steadystate.TRIM'[1]' -stim_base 1 -stim_label 2 roll \
                        -stim_file 2 "+self.options.sourceD+"motion."+self.options.cc+"."+self.options.subj+".steadystate.TRIM'[2]' -stim_base 2 -stim_label 3 pitch \
                        -stim_file 3 "+self.options.sourceD+"motion."+self.options.cc+"."+self.options.subj+".steadystate.TRIM'[3]' -stim_base 4 -stim_label 3 yaw \
                        -stim_file 4 "+self.options.sourceD+"motion."+self.options.cc+"."+self.options.subj+".steadystate.TRIM'[4]' -stim_base 5 -stim_label 4 dS \
                        -stim_file 5 "+self.options.sourceD+"motion."+self.options.cc+"."+self.options.subj+".steadystate.TRIM'[5]' -stim_base 6 -stim_label 5 dL \
                        -stim_file 6 "+self.options.sourceD+"motion."+self.options.cc+"."+self.options.subj+".steadystate.TRIM'[6]' -stim_base 7 -stim_label 6 dP \
                        -rout -bucket "+self.options.outD+"corr."+self.options.cc+"."+self.options.subj+".steadystate -errts "+self.options.outD+"cleanTS.masked.Cond"+self.options.cc+"."+self.options.subj, shell=True)

    def maskdump(self):
    	"""
    	Used to dump the AFNI time series to a next file, ready for fcorr to a text file.
    	"""
        print "The out directory is: "+self.options.outD
        os.chdir(self.options.outD)
        print "Working in :"+os.getcwd()
        print call("3dmaskdump -mask "+self.options.dumpmask+" -noijk "+self.options.outD+"cleanTS.masked.Cond"+self.options.cc+"."+self.options.subj+"+orig.BRIK  > "+self.options.outD+"cleanTS."+self.options.cc+"."+self.options.subj+"_graymask_dump", shell=True)

    def callR(self):
    	"""
    	This calls the R script with fcorr.
    	"""
        inputf = self.options.outD+"cleanTS."+self.options.cc+"."+self.options.subj+"_graymask_dump"
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

