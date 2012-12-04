#!/usr/bin/python

import os
import shutil


subjects = ["TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]
#subjects = ["MYTP"]


def cmdCP():
    """
    simple copy function
    """
    print "subject: "+ss+"; Condition: "+`i`
    shutil.copy2(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/cleanTS."+`i`+"."+ss+"_graymask_dump.bin.corr.thresh.links", os.environ["state"]+"/graymask_links")
    


for ss in subjects:
    for i in range(1,5):
        cmdCP()

