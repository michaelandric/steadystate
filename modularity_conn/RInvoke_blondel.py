#!/usr/bin/python

"""
This uses a different RInvoke because we want to keep the *Rout file. 
So we copy the script as unique names to keep unique *Rout files.
The Rout files show the number of hierarchical levels -- needed for the community organization at each level, done in next script
"""
import os
import sys
from subprocess import call
import shutil


R_SCRIPT_PREF = sys.argv[1]
ss = sys.argv[2]
Cond = sys.argv[3]
Thresh = sys.argv[4]
os.environ["R_ARGS"] = ss+" "+Cond+" "+Thresh

print os.environ["R_ARGS"]
print R_SCRIPT_PREF


#WORKDIR = os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/"
WORKDIR = os.environ["state"]+"/links_files/modularity/"
R_SCRIPT = R_SCRIPT_PREF+".R"
#R_SCRIPT_NEW = R_SCRIPT_PREF+"_gray_"+ss+Cond+"_thresh_"+Thresh+".R"
R_SCRIPT_NEW = R_SCRIPT_PREF+"_gray_"+ss+Cond+"median_linksthresh_"+Thresh+".R"
shutil.copy2(R_SCRIPT,WORKDIR+R_SCRIPT_NEW)
os.chdir(WORKDIR)

print os.getcwd()
print call("R CMD BATCH --vanilla "+R_SCRIPT_NEW, shell=True)

