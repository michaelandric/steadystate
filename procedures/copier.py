#!/usr/bin/python

import os
import shutil


subjects = ["TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]
#subjects = ["MYTP"]


def cmdCP():
    """
    simple copy function
    """
    print "subject: "+ss
    shutil.copy2(os.environ["state"]+"/"+ss+"/masking/ijk_coords_graymattermask_"+ss, os.environ["state"]+"/graymask_coords/")
    


for ss in subjects:
    cmdCP()

