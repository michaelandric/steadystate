#!/usr/bin/python
"""
Get average euclidean distance between a voxel and other voxels in module.
"""
import os
from optparse import OptionParser
from numpy import *
from glob import glob


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


def dist_grab(ss, cc):
    """Run get_distance function

    Args:
        ss: Subject (participant)
        cc: condition identifier
        
    """
    os.chdir(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/")
    print os.getcwd()
    print "Condition: "+cc

    # Get community identifiers

    comfname = glob("cleanTS."+cc+"."+ss+"_graymask_dump.bin.corr.thresh.tree*.justcomm")
    comf = open(''.join(comfname))

    comm_array = []
    for line in comf:
        comm_array.append(int(line))
    
    # Get lines for x, y, z
    
    coordfname = glob(os.environ["state"]+"/"+ss+"/masking/xyz_coords_graymattermask_"+ss)
    coordf = open(''.join(coordfname))
    
    coord_array = []
    for line in coordf:
    	a, b, c = [float(x) for x in line.split()]
    	coord_array.append((a,b,c))


    # Two column arrays where Column 1 are voxel IDs and Column 2 are module IDs

    vox_comm_array = zip(range(len(comm_array)), comm_array)    

    # Get the modules for each condition

    uniq_modules = set(comm_array)

    # Make dictionaries. Module numbers are keys and voxels in modules are values

    mod_dict = {}
    for i in uniq_modules:
        mod_dict[i] = [item for item in vox_comm_array if item[1]==i]

    # For each voxel, find its module, identify all other voxels in module, find distance between every other voxel, average those distances. 
    # Get an average distance for each module, average those for an average distance by condition (this will be in another script).

    euc_dist = []
    for i in range(len(comm_array)):
        tmp_set = []


        # If only 1 voxel comprises module then distance is 0

        if len(mod_dict[vox_comm_array[i][1]]) == 1:
            euc_dist.append(0)
        else:
            for item in mod_dict[vox_comm_array[i][1]]:
                tmp_set.append(item[0])   # These are the voxels in a module with voxel 'i'

            others = [v for v in tmp_set if v != i]   # 'others' is a list of all other voxels in the module besides the current one ('i')   
            
            x_dist = []   # 'x_dist' is a list of distances from voxel 'i' to every other voxel in the modules
            for v in others:
                x_dist.append((get_distance(coord_array[i], coord_array[v])))   # since voxels are 4 x 4 x 4.8, use 5 to be conservative for scaling

            x_dist_filtered = [y for y in x_dist if y > 20]   # filter distance 

            if len(x_dist_filtered) == 0:
                euc_dist.append(0)
            else:
                a = [round(xd,3) for xd in x_dist_filtered]
                euc_dist.append(a)   # distances for voxel 'i' to every other voxel in the module

    dist_out = ""
    for line in euc_dist:
        try:
            for x in line:
                dist_out += str(round(x, 4))+"\n"
        except:
            dist_out += str(0)+"\n"

    outf = open("distance_noavgs_Filter20_"+ss+"_Cond"+cc+".txt","w")
    outf.write(dist_out)
    outf.close()


conditions = range(1,5)

def main():
    """Run the above functions."""
    parser = OptionParser()
    parser.add_option("--subject", dest="ss", help = "give the subject identifier")
    options, args = parser.parse_args()

    for cc in conditions:
        dist_grab(options.ss, `cc`)   # Make sure condition is string and not integer type

if __name__ == "__main__":
    main()
