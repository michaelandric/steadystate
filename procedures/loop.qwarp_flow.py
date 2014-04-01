#!/usr/bin/python
"""
Running this in a loop because when run through condor multiple Qwarps slogs down the machine (load avgs > 100).
When run individiually, it only takes a couple minutes
"""
from subprocess import call

#subjects = ["ANGO"]
#subjects = ["EEPA", "DNLN", "CRFO", "ANMS", "MRZM", "MRVV", "MRMK", "MRMC", "MRAG", "MNGO", "LRVN", "MYTP"]
subjects = ["CLFR", "TRCO", "PIGL", "SNNW", "LDMW", "FLTM"]

for ss in subjects: 
    print call("./qwarp_flow.py --Subject "+ss, shell = True)


