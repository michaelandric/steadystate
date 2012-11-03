#!/usr/bin/python

import os
import commands
from optparse import OptionParser

#def get_opts():
desc = """simple program for doing 3dmaskdump"""
usage = "usage: %prog [options]"
parser = OptionParser(description=desc, version="%prog Sept.2012")
parser.add_option("--subject", dest="ss",
                  help="specify subject identifier")
parser.add_option("--source_directory", dest="sourcedir",
                  help="directory where the source files are")
parser.add_option("--output_directory", dest="outdir",
                  help="directory where you want the output to go")

options, args = parser.parse_args()


def DeconCor(subj,sourceD,outD,i):
    print commands.getoutput("3dDeconvolve -input "+sourceD+"reg."+`i`+"."+subj+".steadystate+orig. -polort 1 -num_stimts 7 \
                             -stim_file 1 /mnt/tier2/urihas/sam.steadystate/ANGO/seed17."+`i`+"."+subj+".steadystate.1D -stim_label 1 lhipp \
                             -stim_file 2 "+sourceD+"motion."+`i`+"."+subj+".steadystate'[1]' -stim_base 2 -stim_label 2 roll \
                             -stim_file 3 "+sourceD+"motion."+`i`+"."+subj+".steadystate'[2]' -stim_base 3 -stim_label 3 pitch \
                             -stim_file 4 "+sourceD+"motion."+`i`+"."+subj+".steadystate'[3]' -stim_base 4 -stim_label 4 yaw \
                             -stim_file 5 "+sourceD+"motion."+`i`+"."+subj+".steadystate'[4]' -stim_base 5 -stim_label 5 dS \
                             -stim_file 6 "+sourceD+"motion."+`i`+"."+subj+".steadystate'[5]' -stim_base 6 -stim_label 6 dL \
                             -stim_file 7 "+sourceD+"motion."+`i`+"."+subj+".steadystate'[6]' -stim_base 7 -stim_label 7 dP \
                             -rout -bucket "+outD+"corr."+`i`+"."+subj+".steadystate")


#get_opts()
print options
print options.ss
print options.sourcedir
subj = options.ss
sourceD = options.sourcedir
outD = options.outdir

for i in range(1,5):
    DeconCor(subj,sourceD,outD,i)
