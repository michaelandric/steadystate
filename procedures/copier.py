#!/usr/bin/python

import os
import shutil


subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]
#subjects = ["EZCR"]


def cmdHB():
    """
    simple copy function
    """
    print "subject: "+ss
    shutil.copy2(os.environ["state"]+"/"+ss+"/"+ss+"voxel_index.ijk+tlrc.txt", os.environ["state"]+"/tal_coords")
    


for ss in subjects:
    cmdHB()

