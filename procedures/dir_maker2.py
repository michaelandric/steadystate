#!/usr/bin/python

import os
import shutil
from glob import glob

subjects = ["PIGL","SNNW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","ANGO"]


def mk_and_cp(ss):
    newdir = os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/another"
    if not os.path.exists(newdir):
        os.makedirs(newdir)

    for f in glob(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/cleanTS.3.*.srcdst"):
        shutil.copy2(f, newdir)

def main():
    for ss in subjects:
        mk_and_cp(ss)

if __name__ == "__main__":
    main()
