#!/usr/bin/python

import os


def getwc():
    try:
        fname = os.environ["state"]+"/"+ss+"/masking/ijk_coords_graymattermask_"+ss
        textf = open(fname, 'r')
    except IOError:
        print "cannot open file %s for reading" % fname
        import sys
        sys.exit(0)

    num_lines = sum(1 for line in open(fname))
    return num_lines


subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]


cntr = ""
nvox = []
for ss in subjects:
    cntr += ss+" "+`getwc()`+"\n"
    nvox.append(getwc())

outf = open('subject_graymattermask_voxnum.txt','w')
outf.write(cntr)
outf.close()

nvox_dict = dict(zip(subjects,nvox))
print nvox_dict
