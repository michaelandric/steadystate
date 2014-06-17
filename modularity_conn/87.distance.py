#!/usr/bin/python
"""
Get average euclidean distance between a voxel and other voxels in module.
"""
import os
from optparse import OptionParser
from numpy import *
from glob import glob
from time import ctime


class GetDistance(object):

    def make_mod_dict(self, ComArray):
        """Make dictionary of modules and their voxels"""
        uniq_modules = set(ComArray)
        mod_dict = {}
        for i in uniq_modules:
            mod_dict[i] = [v for v, c in enumerate(ComArray) if c == i]
        return(mod_dict)

    def getSNSC(self, i, others, ComArray, CoordArray):
        """linalg.norm is from the numpy module and used here to get Euc distance."""
        xdist = array([linalg.norm(CoordArray[i]-CoordArray[v]) for v in others])
        snsc = average(xdist[where(xdist > 20)])   # filter by 20
        if isnan(snsc):
            return 0.        
        else:
            return snsc

    def dist_grab(self, i, ss, nvox, cc):
        nvox = int(nvox)
        comfname = os.environ["state"]+"/%(ss)s/modularity5p/iter%(i)s.%(ss)s.%(cc)s.5p_r0.5_linksthresh_proportion.out.maxlevel_tree" % locals()
        ca = (line.split()[1] for line in open("".join(comfname)))
        comm_array = map(int, ca)

        coordfname = os.environ["state"]+"/%(ss)s/masking/xyz_coords_graymattermask_%(ss)s" % locals()
        coordf = open("".join(coordfname))
        npCoordArray = array([map(float, line.split()) for line in coordf])

        md = self.make_mod_dict(comm_array)   # dictionary of modules and their voxels

        euc_dist = array(zeros(nvox))
        for i in xrange(nvox):
            if len(md[comm_array[i]]) > 1:
                mod_dict_vals = md.get(comm_array[i])
                others = array(mod_dict_vals)[where(array(mod_dict_vals) != i)]
                euc_dist[i] = self.getSNSC(i, others, comm_array, npCoordArray)
            else:
                pass
        return euc_dist


#conditions = range(1,5)
if __name__ == "__main__":
    """Run the above functions."""
    parser = OptionParser()
    parser.add_option("--subject", dest="ss", help = "give the subject identifier")
    parser.add_option("--nvoxels", dest="nvox", help = "subject number of voxels")
    parser.add_option("--condition", dest="cond", help = "subject number of voxels")
    options, args = parser.parse_args()
    ss = options.ss
    cc = options.cond
    
    GD = GetDistance()
    #for cc in conditions:
    niterations = 50
    ss_array = array(zeros(int(options.nvox)*niterations)).reshape(int(options.nvox), niterations)
    for iter in xrange(1, (1+niterations)):
        print ctime()
        print cc, iter

        ss_array[:,(iter-1)] = GD.dist_grab(iter, options.ss, options.nvox, cc)   # Make sure condition is string and not integer type

    array_out_list = (str(round(average(line), 3))+'\n' for line in ss_array)
    array_out = "".join(array_out_list)

    foutname = os.environ['state']+'/%(ss)s/modularity5p/distances/distances_xyz_filt20_%(ss)s_Cond%(cc)s.txt' % locals()
    outf = open(foutname, 'w')
    outf.write(array_out)
    outf.close()



