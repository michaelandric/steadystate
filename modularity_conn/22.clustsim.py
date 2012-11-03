#!/usr/bin/python

import os

os.chdir(os.environ["state"]+"/groupstats")
print os.getcwd()
print os.system("3dClustSim -nxyz 91 109 91 -dxyz 2 2 2 -fwhm 6 -NN 123")
