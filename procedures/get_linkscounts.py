#!/usr/bin/python 

import os

"""
Get number of links for *links_corval ("/mnt/tier2/urihas/Andric/steadystate/links_corval")
"""

os.chdir("/mnt/tier2/urihas/Andric/steadystate/graymask_links")
subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]

count_file = ""
for ss in subjects:
    for i in range(1,5):
        count_file += `len(open(ss+"."+`i`+".links_corval").readlines())`+" "+ss+" "+`i`+"\n"

outfname = "linkscount0.5rval.txt"
outf = open(outfname, "w")
outf.write(count_file)
outf.close()


