#!/usr/bin/python

import os
import commands
import shutil


#subjs = ["MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"]
subjs = ["LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS"]
steadystate = os.environ["state"]
parts = ["HEAD","BRIK"]


def cmdHB():
    shutil.copy2(origdir+"/blur."+`i`+"."+ss+".steadystate+orig."+HB,steadystate+"/"+ss)
    #shutil.copy2(origdir+"/reg."+`i`+"."+ss+".steadystate+orig."+HB,steadystate+"/"+ss)
    #shutil.copy2(origdir+"/"+ss+"avg_Alnd+orig."+HB,steadystate+"/"+ss)
    #shutil.copy2(origdir+"/"+ss+".SurfVol_Alnd_Exp+orig."+HB,steadystate+"/"+ss)
    
def cmdMotionFiles():
    shutil.copy2(origdir+"/motion."+`i`+"."+ss+".steadystate",steadystate+"/"+ss)


for ss in subjs:
    origdir = "/mnt/tier2/urihas/sam.steadystate/"+ss
    for i in range(1,5):
        for HB in parts:
            print `i`+" "
            cmdHB()

        cmdMotionFiles()
