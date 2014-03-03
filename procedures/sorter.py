#!/usr/bin/python

import os
from subprocess import call


def sortem(cc):
    call("cat *Cond"+cc+"major* | sort -g > tmp_Cond"+cc+"_nodroles.txt", shell=True)


for cc in range(1,5):
    os.chdir(os.environ["state"]+"/groupstats/")
    print os.getcwd()
    sortem(`cc`)
