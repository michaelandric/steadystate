#!/usr/bin/python

"""
Fitting the distance measures for each participant X condition
"""
import os
import scipy.stats


fname1 = "distances_xyz_filt20_LRVN_Cond1.txt"

def distfitter(fname):
    f1 = open(''.join(fname))
    d1 = (line for line in f1)
    d1 = map(float, d1)
    d1 = np.array(d1)
    d1 = d1[np.where(d1 != 0)]
    fit_shape, fit_loc, fit_scale = gamma.fit(d1)
    return (fit_shape, fit_loc, fit_scale)



if __name__ == "__main__":
parser = OptionParser()
parser.add_option("--subject", dest="ss", help = "give the subject identifier")
options, args = parser.parse_args()
ss = options.ss
conditions = xrange(1,5)
for cc in conditions:
    fname = os.environ['state']+'/%s/modularity5p/distances/distances_xyz_filt20_%s_Cond%d.txt' % (ss, ss, cc)
    fit_shape, fit_loc, fit_scale = distfitter(fname)



f1 = open(''.join(fname1))
d1 = (line for line in f1)
d1 = map(float, d1)
