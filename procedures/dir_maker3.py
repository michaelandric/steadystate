#!/usr/bin/python

import os

subjects = ["ANGO", "MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"]
#densities = ["5p", "8p", "12p", "15p"]
densities = ["5p"]

def mk(ss, de):
    newdir = os.environ["state"]+"/"+ss+"/modularity"+de+"/similarity_measures"
    if not os.path.exists(newdir):
        os.makedirs(newdir)

def main():
    for ss in subjects:
        for de in densities:
            mk(ss, de)

if __name__ == "__main__":
    main()
