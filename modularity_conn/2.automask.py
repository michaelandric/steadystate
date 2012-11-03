#!/usr/bin/python

import os
import commands


def automask(i,ss):
    print commands.getoutput("3dAutomask -dilate "+`i`+" -prefix automask_d"+`i`+"_"+ss+" '/mnt/tier2/urihas/Andric/steadystate/"+ss+"/blur.1."+ss+".steadystate+orig[99]'")


subjs = ["MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"]
#subjs = ["LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS"]

for ss in subjs:
    for i in range(1,4):
        os.chdir(os.environ["state"]+"/"+ss)
        print os.getcwd()
        automask(i,ss)
