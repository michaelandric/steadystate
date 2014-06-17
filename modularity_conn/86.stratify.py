#!/usr/bin/python

"""
Assign bin identifiers to SNSC values
"""

import os
from itertools import dropwhile
import numpy as np


def iscomment(s):
    return s.startswith('#')


def assigner(inputname, outname):
    vertvals = []
    f = open(inputname, "r")

    for line in dropwhile(iscomment, f):
        vertvals.append(line.split()[1])

    vertvals = map(float, vertvals)
    verts = range(len(vertvals))

    binvals = np.zeros(len(vertvals))

    for i, v in enumerate(vertvals):
        if v == 777:
            binvals[i] = 4
        elif v < .2:
            binvals[i] = 5
        elif v > .2 and v <= .30:
            binvals[i] = 6
        elif v > .3 and v <= .35:
            binvals[i] = 7
        elif v > .35 and v <= .4:
            binvals[i] = 8
        elif v > .4 and v <= .45:
            binvals[i] = 9
        elif v > .45:
            binvals[i] = 10

    binvals = map(int, binvals)     

    outdat = ""
    for i, v in enumerate(binvals):
        outdat += `i`+" "+`v`+"\n"

    outf = open(outname, 'w')
    outf.write(outdat)
    outf.close()



if __name__ == "__main__":

    os.chdir("/mnt/lnif-storage/urihas/uhproject/suma_tlrc")
    for h in ['lh', 'rh']:
        inname = "preserved_group_median5p__20vxFltr_warped_median.out_"+h+".pn2.0.tlrc.1D"
        outname = "stratified_preserved_group_median5p__20vxFltr_warped_median.out_"+h+".pn2.0.tlrc.1D"
        assigner(inname, outname)


