#!/usr/bin/python

import os
import shutil
from glob import glob

#subjects = ["TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]
subjects = ["MYTP"]


def cmdCP():
    """
    simple copy function
    """
    print "subject: "+ss
    #shutil.copy2(os.environ["state"]+"/"+ss+"/masking/ijk_coords_graymattermask_"+ss, os.environ["state"]+"/graymask_coords/")
    for filename in glob("cleanTS.*."+ss+"_graymask_dump.bin.corr.thresh.tree*.justcomm"):
        shutil.copy2(filename, os.environ["state"]+"/module_files")
    


for ss in subjects:
    os.chdir(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/")
    cmdCP()

