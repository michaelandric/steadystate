#!/usr/bin/python

import os


def getwc():
    try:
        fname = os.environ["state"]+"/"+ss+"/blur.4."+ss+".steadystate.TRIM.noijk_dump"
        textf = open(fname, 'r')
    except IOError:
        print "cannot open file %s for reading" % fname
        import sys
        sys.exit(0)

    num_lines = sum(1 for line in open(fname))
    return ss+" "+`num_lines`+"\n"




subjects = ["ANGO","MYTP","CLFR","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"]

cntr = ""
for ss in subjects:
    cntr += getwc()

outf = open('subject_blurTSwordcounts.txt','w')
outf.write(cntr)
outf.close()

