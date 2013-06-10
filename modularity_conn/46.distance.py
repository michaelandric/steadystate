#!/usr/bin/python

import os
from numpy import *
from glob import glob


conditions = range(1,5)
subjects = ["ANGO","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"]


def get_distance(p,q):
    return sqrt(sum([(x-y)**2 for (x,y) in zip(p,q)]))

"""
Example to run:
get_distance([-2,2,5],[2,4,2])
"""

"""
Separate function that calls 'get_distance' because it will be easier to run it in a 'for' loop if I want to do only select people or conditions
"""

def dist_grab(ss, cc): 
#for ss in subjects:
    os.chdir(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/")
    print os.getcwd()
    """
    Get the community (module) IDs for condition
    """
    fname = glob("cleanTS."+cc+".ANGO_graymask_dump.bin.corr.thresh.tree*.ijk.txt")
    comf = open(''.join(fname))

    """
    Get lines from ijk+community identifiers file
    """
    comm_array = []
    coord_array = []
    for line in comf:
        #comm_array.append([int(x) for x in line.split()][0])
        #[int(x) for x in line.split()[0:3]]
        a, b, c, d = [int(x) for x in line.split()]
        coord_array.append((a,b,c))
        comm_array.append(d)


    """
    Two column arrays where Column 1 are voxel IDs and Column 2 are module IDs
    """
    vox_comm_array = zip(range(len(comm_array)), comm_array)
    
    """
    get the modules for each condition
    """
    uniq_modules = set(comm_array)
    """
    Make dictionaries. module numbers are keys and voxels in modules are values
    """    
    mod_dict = {}
    for i in uniq_modules:
        mod_dict[i] = [item for item in vox_comm_array if item[1]==i]


    """
    For each voxel, find its module, identify all other voxels in module, find distance between every other voxel, average those distances. 
    Get an average distance for each module, average those for an average distance by condition (this will do in another script).
    """

    euc_dist = []
    for i in range(len(comm_array)):
        tmp_set = []

        for item in mod_dict[vox_comm_array[i][1]]:
            tmp_set.append(item[0]) ## these are the voxels in a module with voxel 'i'

        """
        'others' is a list of all other voxels in the module besides the current one ('i')
        """
        others = [v for v in tmp_set if v != i]
        """
        'x_dist' is a list of distances from voxel 'i' to every other voxel in the modules   
        """
        x_dist = []
        for v in others:
            x_dist.append(get_distance(coord_array[i], coord_array[v]))

        euc_dist.append(round(average(x_dist),4)) ## average distance for voxel 'i' to every other voxel in the module  

    dist_out = ""
    for line in euc_dist:
        dist_out += str(round(line,4))+"\n"

    outf = open("euclidean_distancep_"+ss+"_Cond"+cc+".txt","w")
    outf.write(pres_out)
    outf.close()


def main():
    for ss in subjects:
        for cc in conditions:
            dist_grab(ss, `cc`)

if __name__ == "__main__":
    main()
