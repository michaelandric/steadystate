#!/usr/bin/python

"""
This does a Friedman test
"""

from subprocess import call
import os

"""
Not using EZCR - couldn't get graymatter mask for this subj.
Not using BARS - wasn't included in Sam/Uri's analyses, too much motion
"""
subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","ANGO","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"]
factor_combos = ""
for i in range(1,5):
    for j in range(1,len(subjects)+1):
        factor_combos += "-dset "+`i`+" '"+os.environ["state"]+"/"+subjects[j-1]+"/corrTRIM_BLUR/"+subjects[j-1]+"."+`i`+".degrees_gray+tlrc.' "

print "factor combinations: \n"+factor_combos

os.chdir(os.environ["state"]+"/groupstats/")
print os.getcwd()
print "NOW RUNNING THE FRIEDMAN TEST\n"
print call("3dFriedman -levels 4 "+factor_combos+" -out degrees_gray.friedman_out", shell=True)
