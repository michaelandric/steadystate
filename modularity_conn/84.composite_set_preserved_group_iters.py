#!/usr/bin/python
"""
This is a python port of R script by the same name
"""
import sys
import os
import numpy as np
from time import ctime

def fltmedian(nr):
    if len(nr[nr==777.]) / float(len(nr)) >= .5:
        return 777
    else:
        return np.median(nr[nr!=777])

def fltmean(nr):
    if len(nr[nr==777.]) / float(len(nr)) >= .5:
        return 777
    else:
        return np.mean(nr[nr!=777]) 



if __name__ == "__main__":

    subjects = ["ANGO", "MYTP", "TRCO", "PIGL", "SNNW", "LDMW", "FLTM", "CLFR", "EEPA", "DNLN", "CRFO", "ANMS", "MRZM", "MRVV", "MRMK", "MRMC", "MRAG", "MNGO", "LRVN"]
    nvoxels = 231203
    null_mat = np.array(np.zeros(nvoxels*len(subjects))).reshape(nvoxels, len(subjects))

    for i in xrange(len(subjects)):
        print subjects[i]+" // "+ctime()
        #ss_nullfname = os.environ['state']+'/%s/corrTRIM_BLUR/iters_%s_median5p_20vxFltr_warped_tlrc_dump.txt' % (subjects[i], subjects[i])
        ss_nullfname = os.environ['state']+'/%s/corrTRIM_BLUR/preserved_%s_median5p_20vxFltr_warped_tlrc_dump.txt' % (subjects[i], subjects[i])
        ss_nullf = open(''.join(ss_nullfname))
        ss_null = (line.split()[3] for line in ss_nullf)
        null_mat[:,i] = map(float, ss_null)

    outmedian = np.apply_along_axis(fltmedian, axis = 1, arr = null_mat)
    outmean = np.apply_along_axis(fltmean, axis = 1, arr = null_mat)

    os.chdir(os.environ['state']+'/groupstats')
    #np.savetxt('iters_group_median5p_20vxFltr_warped_median.out', outmedian, fmt='%.4f')
    #np.savetxt('iters_group_median5p_20vxFltr_warped_average.out', outmean, fmt='%.4f')
    np.savetxt('preserved_group_median5p_20vxFltr_warped_median.out', outmedian, fmt='%.4f')
    np.savetxt('preserved_group_median5p_20vxFltr_warped_average.out', outmean, fmt='%.4f')

    m1 = "Voxels in median group that are 777: %s" % round((len(outmedian[outmedian==777]) / nvoxels) * 100, 4)
    m2 = "Voxels in mean group that are 777: %s" % round((len(outmean[outmean==777]) / nvoxels) * 100, 4)
    fsummary = open('preserved_group_median5p_20vxFltr_warped_summary.out', 'w')
    fsummary.write(m1+'\n'+m2+'\n')
    fsummary.close()

