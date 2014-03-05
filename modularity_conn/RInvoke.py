#!/usr/bin/python

"""
This performs same function as 'RInvoke.sh' but in python. (Whoopty-doo)
"""

import os
import sys
from subprocess import call


os.environ["R_ARGS"] = ' '.join(sys.argv[2:])

call("R CMD BATCH --vanilla "+sys.argv[1], shell = True)

