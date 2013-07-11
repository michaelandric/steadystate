#!/usr/bin/python

import os
import shutil
from glob import glob


subjects = ["TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANGO"]
#subjects = ["MYTP"]

def cmdCP(ss):
    """
    simple copy function
    """
    print "subject: "+ss
    print os.getcwd()
    for filename in glob("blur*TRIM_graymask_dump"):
        shutil.copy2(filename, os.environ["state"]+"/TSfiles")

    for filename in glob("masking/xyz_coords_graymattermask_*"):
        shutil.copy2(filename, os.environ["state"]+"/TSfiles")
    

def main():
    for ss in subjects:
        os.chdir(os.environ["state"]+"/"+ss)
        cmdCP(ss)


if __name__ == "__main__":
    main()


