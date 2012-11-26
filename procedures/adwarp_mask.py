#!/usr/bin/python

from subprocess import call
import os


def adwarp_call(subject):
    print "subject is "+subject
    os.chdir("/mnt/tier2/urihas/Andric/steadystate/"+subject+"/masking/")
    print os.getcwd()
    apar = os.environ["state"]+"/"+subject+"/corrTRIM_BLUR/"+subject+"tlrc+tlrc"
    print call("adwarp -apar "+apar+" -dpar "+subject+"_graymattermask_resampled+orig -dxyz 2 -resam NN", shell=True)

