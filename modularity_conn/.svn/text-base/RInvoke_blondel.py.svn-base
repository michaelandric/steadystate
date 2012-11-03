#!/usr/bin/python

import os
import sys
import commands
import shutil


R_SCRIPT_PREF = sys.argv[1]
ss = sys.argv[2]
Cond = sys.argv[3]
os.environ["R_ARGS"] = ss+" "+Cond

print os.environ["R_ARGS"]
print R_SCRIPT_PREF


WORKDIR = os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/"
R_SCRIPT = R_SCRIPT_PREF+".R"
R_SCRIPT_NEW = R_SCRIPT_PREF+"_"+ss+Cond+".R"
shutil.copy2(R_SCRIPT,WORKDIR+R_SCRIPT_NEW)
os.chdir(WORKDIR)

print os.getcwd()
print commands.getoutput("R CMD BATCH --vanilla "+R_SCRIPT_NEW)

