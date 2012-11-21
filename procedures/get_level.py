#!/usr/bin/python

import os
import re

"""
This is to get the highest hierarchical level
"""

subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"] ## EZCR not in here

def get_hier(subject,cc):
    ll = []
    fp = open("8.blondel_gray_"+subject+`cc`+".Rout")
    for line in fp:
        if re.match("(level*)", line):
            ll.append(line)

    level = int(ll[len(ll)-1].split()[1][0])
    return level


subj_hiers = []
for ss in subjects:
    os.chdir(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/")
    print os.getcwd()
    levs = []
    for cc in range(1,5):
        levs.append(get_hier(ss,cc))

    print levs

    subj_hiers.append(tuple(levs))
    print subj_hiers
    

hier_dict = dict(zip(subjects,subj_hiers))
