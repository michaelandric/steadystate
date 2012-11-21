#!/usr/bin/python

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
        factor_combos += "-dset "+`i`+" "+`j`+" '"+os.environ["state"]+"/"+subjects[j-1]+"/corrTRIM_BLUR/"+subjects[j-1]+"."+`i`+".degrees_gray+tlrc.' "

print "factor combinations: \n"+factor_combos

os.chdir(os.environ["state"]+"/groupstats/")
print os.getcwd()
print "NOW RUNNING THE ANOVA\n"
print call("3dANOVA2 -type 3 -alevels 4 -blevels "+`len(subjects)`+" -mask "+os.environ["state"]+"/groupstats/automask_d1_TTavg152T1+tlrc. \
            "+factor_combos+" -fa H_fstat -amean 1 H1_mean -amean 2 H2_mean -amean 3 H3_mean -amean 4 H4_mean \
            -acontr -0.75 -0.059 0.63 0.178 poslincorrect \
            -acontr 0.42 -0.57 0.56 -0.41 Ushapecorrect \
            -acontr -1 -1 1 1 stepupcorrect \
            -bucket degrees_gray.anova_contrasts", shell=True)
