#!/usr/bin/python

import os
from glob import glob
from subprocess import call
import numpy as np


subjects = ["ANGO", "MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"]
conditions = range(1,5)
densities = ["5p", "8p", "12p", "15p"]

for de in densities:
    print de
    for ss in subjects:
        #call("cat *"+ss+"."+`cc`+"*.Qval > qvals."+ss+"."+`cc`+".txt", shell = True)
        os.chdir(os.environ["state"]+"/"+ss+"/modularity"+de+"/")
        print os.getcwd()
        for cc in conditions:
            Qvals_ss = np.array(map(float, [open(f).read().split('\n')[0] for f in glob("*"+ss+"."+`cc`+"*.Qval")]))
            np.savetxt("qvals_sort."+ss+"."+`cc`+"."+de+".txt", np.sort(Qvals_ss), fmt = "%f")


