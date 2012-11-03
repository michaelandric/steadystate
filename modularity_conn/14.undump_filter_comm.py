#!/usr/bin/python

import os
import sys
import commands

ss = sys.argv[1]
Cond = sys.argv[2]
treeNum = sys.argv[3]
filt_pass = sys.argv[4]

print ss
print Cond
print filt_pass

os.chdir(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR")
print os.getcwd()

if filt_pass == "1":
    commands.getoutput("paste -d ' ' ../ijk_coords_"+ss+" "+ss+"."+Cond+".comm.tree"+treeNum+"_filt.txt > "+ss+"."+Cond+".comm.tree"+treeNum+"_filt.ijk.txt")
    commands.getoutput("3dUndump -prefix "+ss+"."+Cond+".tree"+treeNum+"_filt.ijk -ijk -datum float -master ../blur.3."+ss+".steadystate.TRIM+orig. "+ss+"."+Cond+".comm.tree"+treeNum+"_filt.ijk.txt")
elif filt_pass == "2":
    commands.getoutput("paste -d ' ' ../ijk_coords_"+ss+" "+ss+"."+Cond+".comm.tree"+treeNum+"_filt2conv.txt > "+ss+"."+Cond+".comm.tree"+treeNum+"_filt2conv.ijk.txt")
    commands.getoutput("3dUndump -prefix "+ss+"."+Cond+".tree"+treeNum+"_filt2conv.ijk -ijk -datum float -master ../blur.3."+ss+".steadystate.TRIM+orig. "+ss+"."+Cond+".comm.tree"+treeNum+"_filt2conv.ijk.txt")


