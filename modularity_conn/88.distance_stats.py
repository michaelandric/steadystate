#!/usr/bin/python

"""
This is python a port of 47.distance_stats.R
"""

import os
import numpy as np


def getdistavg(fname):
    ss_f = open(''.join(fname))
    ss_dat = (line for line in ss_f)
    return np.mean(map(float, ss_dat))


subjects = ["ANGO", "MYTP", "TRCO", "PIGL", "SNNW", "LDMW", "FLTM", "CLFR", "EEPA", "DNLN", "CRFO", "ANMS", "MRZM", "MRVV", "MRMK", "MRMC", "MRAG", "MNGO", "LRVN"]
conditions = range(1,5)

all_mat = np.array(np.zeros(len(subjects)*len(conditions))).reshape(len(subjects), len(conditions))
for ss in xrange(len(subjects)):
    for cc in xrange(len(conditions)):
        fname = os.environ['state']+'/%s/modularity5p/distances/distances_xyz_filt20_%s_Cond%d.txt' % (subjects[ss], subjects[ss], conditions[cc])
        all_mat[ss,cc] = getdistavg(fname)

cond_means = [round(x, 4) for x in np.mean(all_mat, axis = 0)]
cond_means = ", ".join(map(str, cond_means))
cond_medians = [round(x, 4) for x in np.median(all_mat, axis = 0)]
cond_medians = ", ".join(map(str, cond_medians))
cond_stds = [round(x, 4) for x in np.std(all_mat, axis = 0, ddof = 1)]
cond_stds = ", ".join(map(str, cond_stds))
all_mean = str(round(np.mean(all_mat), 4))
all_median = str(round(np.median(all_mat), 4))
all_std = str(round(np.std(all_mat, ddof = 1), 4))

out_summary = 'Condition medians: '+'\n'+cond_medians+'\n'+'Condition means: '+'\n'+cond_means+'\n'+'Condition standard devs: '+'\n'+cond_stds+'\n'+'Group median: '+'\n'+all_median+'\n'+'Group mean: '+'\n'+all_mean+'\n'+'Group standard dev: '+'\n'+all_std+'\n'

os.chdir(os.environ['state']+'/groupstats/')
fsummary = open('distance_summary_info.txt', 'w')
fsummary.write(out_summary)
fsummary.close()


