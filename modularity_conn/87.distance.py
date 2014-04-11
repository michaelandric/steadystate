#!/usr/bin/python
"""
Get average euclidean distance between a voxel and other voxels in module.
"""
import os
from optparse import OptionParser
from numpy import *
from glob import glob
from time import ctime


def get_distance(p,q):
    """Get distance between 2 x, y, z voxel coords.

    Separate function 'get_distance' makes it easier to run a 'for' loop and subset people or conditions.
    Args:
        p: one coordinate
        q: other coordinate
        
    Run example:
    get_distance([-2,2,5],[2,4,2])

    """
    return sqrt(sum([(x-y)**2 for (x,y) in zip(p,q)]))

def filterbyvalue(seq, value):
    for el in seq:
        if el > value: yield el

def dist_grab(i, ss, cc):
    """Run get_distance function

    Args:
        ss: Subject (participant)
        cc: condition identifier
        
    """
    # Get community identifiers
    comfname = os.environ["state"]+"/"+ss+"/modularity5p/iter"+`i`+"."+ss+"."+cc+".5p_r0.5_linksthresh_proportion.out.maxlevel_tree"
    comf = open(comfname, 'r')
    comm_array = []
    for line in comf:
        comm_array.append(line.split()[1])
    comm_array = map(int, comm_array)

    # Get lines for x, y, z
    coordfname = glob(os.environ["state"]+"/"+ss+"/masking/xyz_coords_graymattermask_"+ss)
    coordf = open(''.join(coordfname))
    coord_array = []
    for line in coordf:
    	a, b, c = [float(x) for x in line.split()]
    	coord_array.append((a,b,c))

    # Get the modules for each condition
    uniq_modules = set(comm_array)

    # Make dictionaries. Module numbers are keys and voxels in modules are values
    mod_dict = {}
    for i in uniq_modules:
        mod_dict[i] = [v for v, c in enumerate(comm_array) if c == i]

    # For each voxel, find its module, identify all other voxels in module, find distance between every other voxel, average those distances. 
    # Get an average distance for each module, average those for an average distance by condition (this will be in another script).
    #euc_dist = []
    euc_dist = array(zeros(len(comm_array)))

    """
    for i in mod_dict.keys():
        if len(mod_dict[i]) == 1:
            continue
            #euc_dist[mod_dict[i][0]] = 0
        else:
            for v in mod_dict[i]:
                v_dist = []
                others = (vx for vx in mod_dict[i] if vx != v)
                for vv in others:
                    gd = get_distance(coord_array[v], coord_array[vv])
                    if gd > 20:
                        v_dist.append(gd)
                euc_dist[v] = average(v_dist)

    """
    for i in xrange(len(comm_array)):
        if len(mod_dict[comm_array[i]]) == 1:
            #euc_dist.append(0)
            continue
        else:
            others = (v for v in mod_dict[comm_array[i]] if v != i)
            x_dist = []
            for v in others:
                x_dist.append((get_distance(coord_array[i], coord_array[v])))

            x_dist_filtered = [y for y in filterbyvalue(x_dist, 20)]   # Filter here by 20
            if len(x_dist_filtered) == 0:
                #euc_dist.append(0)
                euc_dist[i] = 0.
            else:
                #euc_dist.append(round(average(x_dist_filtered), 4))   # Average distance for voxel 'i' to all other voxels in its module
                euc_dist[i] = average(x_dist_filtered)   # Average distance for voxel 'i' to all other voxels in its module

    return euc_dist

    #dist_out = ""
    #for line in euc_dist:
    #    dist_out += str(round(line,4))+"\n"

    #outf = open("distance_xyz_Filter20_"+ss+"_Cond"+cc+".txt","w")
    #outf.write(dist_out)
    #outf.close()



conditions = range(1,5)

if __name__ == "__main__":
    """Run the above functions."""
    parser = OptionParser()
    parser.add_option("--subject", dest="ss", help = "give the subject identifier")
    parser.add_option("--nvoxels", dest="nvox", help = "subject number of voxels")
    options, args = parser.parse_args()

    for cc in conditions:
        niterations = 50
        #print int(options.nvox)*niterations
        ss_array = array(zeros(int(options.nvox)*niterations)).reshape(int(options.nvox), niterations)
        for iter in xrange(1, (1+niterations)):
            print ctime()
            print cc, iter
            dd = dist_grab(iter, options.ss, `cc`)   # Make sure condition is string and not integer type
            ss_array[:,(iter-1)] = dd
            savetxt(os.environ['state']+'/'+options.ss+'/ss_array'+`iter`+'.'+options.ss+'.txt', ss_array, fmt='%1.3f')

        array_out = ""
        for line in ss_array:
            array_out += str(round(average(line), 3))+'\n'

        foutname = os.environ['state']+'/'+options.ss+'/modularity5p/distances/distances_xyz_filt20_'+options.ss+'_Cond'+`cc`+'.txt'
        outf = open(foutname, 'w')
        outf.write(array_out)
        outf.close()



