#!/usr/bin/python

import os
from subprocess import call


def getFWHMx(ss, cc):
    mask = os.environ['state']+'/%(ss)s/masking/%(ss)s_graymattermask_resampled+orig.' % locals()
    input = os.environ['state']+'/%(ss)s/blur.%(cc)d.%(ss)s.steadystate.TRIM+orig.' % locals()
    call('3dFWHMx -mask '+mask+' -input '+input+' -detrend -out '+os.environ['state']+'/%(ss)s/%(ss)s.Cond%(cc)d_fwhm_estimates' % locals(), shell = True)


if __name__ == "__main__":
    
    subjects = ["ANGO", "MYTP", "TRCO", "PIGL", "SNNW", "LDMW", "FLTM", "CLFR", "EEPA", "DNLN", "CRFO", "ANMS", "MRZM", "MRVV", "MRMK", "MRMC", "MRAG", "MNGO", "LRVN"]

    for ss in subjects:
        for cc in xrange(1,5):
            getFWHMx(ss, cc)


