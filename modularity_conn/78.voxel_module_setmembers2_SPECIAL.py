#!/usr/bin/python

"""
Find whether voxels part of a module in one condition prune or reorganize
"prune" -> Partition big module into sub-modules
"reorganize" -> different connections, voxels are that were together in one module are now in different modules

This version is to do this on iterations of the modularity solution.

Doing this between conditions or on the same condition is very easy to change: Lines 107 and 108 

SPECIAL:
This version set up to handle MRAG. When running the 'hierarchy' on this pariticpant, only parsed 10234 voxels and left out the last one.
This is only the case for conditions 1 and 3. Conditions 2 and 4 both received that last voxel. 
Work around: Adding the single voxel to the end of the list based on the same as previous voxel (i.e., 10234 becomes 10235, as well).

"""

import os
import sys
from glob import glob


def set_consist(ss, ia, ib, input1, input2):

    """
    Get the community (module) IDs for each
    """
    comf3 = open(input2).readlines()
    comf1 = open(input1).readlines()

    """
    get module identifiers
    """
    comm1_array = []
    voxID1_array = []
    comm3_array = []
    voxID3_array = []

    for line in comf1:
        a, b = map(int, line.split())
        voxID1_array.append(a)
        comm1_array.append(b)

    voxID1_array.append(10234)
    comm1_array.append(comm1_array[len(comm1_array)-1])

    for line in comf3:
        a, b = map(int, line.split())
        voxID3_array.append(a)
        comm3_array.append(b)


    """
    Make two column arrays 
    Column 1 are voxel IDs and Column 2 are module IDs
    """
    vox_comm3_array = zip(voxID3_array, comm3_array)
    vox_comm1_array = zip(voxID1_array, comm1_array)
    
    """
    get the modules for each condition
    """
    uniq3_modules = set(comm3_array)
    uniq1_modules = set(comm1_array)
    """
    Make dictionaries. module numbers are keys and voxels in modules are values
    """    
    mod3_dict = {}
    for i in uniq3_modules:
        mod3_dict[i] = [item for item in vox_comm3_array if item[1]==i]

    mod1_dict = {}
    for i in uniq1_modules:
        mod1_dict[i] = [item for item in vox_comm1_array if item[1]==i]

    """
    For each voxel, find its module in condition3, then in condition1, and interset voxels in its module in condition3 with condition1
    """

    preservation = []
    for i in xrange(len(comm3_array)):
        tmp3 = []
        tmp1 = []

        if mod3_dict[vox_comm3_array[i][1]] < 20:
            preservation.append(777)
        else:
            for item in mod3_dict[vox_comm3_array[i][1]]:
                tmp3.append(item[0]) ## these are the voxels in a module with voxel 'i'
            for item in mod1_dict[vox_comm1_array[i][1]]:
                tmp1.append(item[0])

            #pruning = [filter(lambda x: x in tmp3, sublist) for sublist in tmp1]
            #len_tmp_intersect = len([x in for x in tmp3 if x in tmp1])
            #len(set(tmp3) & set(tmp1))
            preservation.append(round(len(set(tmp3).intersection(set(tmp1))) / float(len(tmp3)), 4))
            #preservation.append(round(float(len(set(tmp3) & set(tmp1))) / float(len(tmp3)), 4))
    
    pres_out = ""
    for line in preservation:
        pres_out += str(round(line,4))+"\n"

    #outname = os.environ["state"]+"/"+ss+"/modularity5p/set_consistency/preserved_iters_"+ia+"_"+ib+"_"+ss+".txt"
    #outname = os.environ["state"]+"/"+ss+"/modularity5p/set_consistency/iter"+ia+"_"+ss+"_preserved.txt"
    outname = os.environ["state"]+"/"+ss+"/modularity5p/set_consistency2/iter"+ia+"_"+ss+"_preserved.txt"
    outf = open(outname, "w")
    outf.write(pres_out)
    outf.close()



if __name__ == "__main__":

    participant = sys.argv[1]
    os.chdir(os.environ["state"]+"/"+participant+"/modularity5p/")
    print os.getcwd()

    """
#This is to do the iters between each different combination in same condition
    cca = 1
    ccb = 1
    for i in range(1, 51):
        for j in range(1, 51):
            if i == j:
                continue
            else:
#                combos.append((i, j))
                input1name = "iter"+`i`+"."+participant+"."+`cca`+".5p_r0.5_linksthresh_proportion.out.maxlevel_tree" 
                input2name = "iter"+`j`+"."+participant+"."+`ccb`+".5p_r0.5_linksthresh_proportion.out.maxlevel_tree" 

                set_consist(participant, `i`, `j`, input1name, input2name)
    """

    #This is to do between Highly Ordered (cca = 1) and Random (ccb = 3) conditions
    cca = 1
    ccb = 3
    for i in xrange(1, 101):
        j = i
        print i
        input1name = "iter"+`i`+"."+participant+"."+`cca`+".5p_r0.5_linksthresh_proportion.out.maxlevel_tree" 
        input2name = "iter"+`j`+"."+participant+"."+`ccb`+".5p_r0.5_linksthresh_proportion.out.maxlevel_tree" 

        set_consist(participant, `i`, `j`, input1name, input2name)



