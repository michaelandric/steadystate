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

def get_linkcount(ss,cc):
    try:
        fname = os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/cleanTS."+`cc`+"."+ss+"_graymask_dump.bin.corr.thresh.links"
        textf = open(fname, 'r')
    except IOError:
        print "cannot open file %s for reading" % fname
        import sys
        sys.exit(0)

    num_lines = sum(1 for line in open(fname))
    return num_lines


#subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]
subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]

cntr = ""
os.chdir(os.environ["state"]+"/groupstats/")
print os.getcwd()
for ss in subjects:
    for cc in range(1,5):
        cntr += ss+" "+" "+`cc`+" "+`get_linkcount(ss,cc)`+"\n"


outf = open('link_count_0.5thresh.txt','w')
outf.write(cntr)
outf.close()

## below two lines were for older version of this code -- see github repos 
#nvox_dict = dict(zip(subjects,nvox))
#print nvox_dict
