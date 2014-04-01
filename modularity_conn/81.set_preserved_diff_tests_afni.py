#!/usr/bin/python

"""
This does a one sample ttest in AFNI
"""

from subprocess import call
import os

"""
Not using EZCR - couldn't get graymatter mask for this subj.
Not using BARS - wasn't included in Sam/Uri's analyses, too much motion
"""

subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","ANGO","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"]
factor_combos = ""

for j in range(1,len(subjects)+1):
    factor_combos +=  os.environ["state"]+"/"+subjects[j-1]+"/corrTRIM_BLUR/preserved_diff_"+subjects[j-1]+"_median5p_warped+tlrc. "

print "factor combinations: \n"+factor_combos

os.chdir(os.environ["state"]+"/groupstats/")
print os.getcwd()
print "NOW RUNNING THE TEST\n"
print call("3dttest++ -setA "+factor_combos+" -prefix preserved_diff_group_median5p_warped_fromafni", shell=True)   # adding that I did this in AFNI to the output name because I did another vesion in R

