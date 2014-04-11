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
    comm3_array = []

    for line in comf1:
        a, b = map(int, line.split())
        comm1_array.append(b)

    comm1_array.append(comm1_array[len(comm1_array)-1])

    for line in comf3:
        a, b = map(int, line.split())
        comm3_array.append(b)


    """
    Make dictionaries. module numbers are keys and voxels in modules are values
    """    
    mod3_dict = {}
    mod1_dict = {}
    for i in set(comm3_array):
        mod3_dict[i] = [v for v, c in enumerate(comm3_array) if c == i]
    for i in set(comm1_array):
        mod1_dict[i] = [v for v, c in enumerate(comm1_array) if c == i]


    """
    For each voxel, find its module in condition3, then in condition1, and interset voxels in its module in condition3 with condition1
    """
    preservation = []
    for i in xrange(len(comm3_array)):
        if len(mod3_dict[comm3_array[i]]) < 20 or len(mod1_dict[comm1_array[i]]) < 20:
            preservation.append(777)
        else:
            inter = len(set(mod3_dict[comm3_array[i]]).intersection(set(mod1_dict[comm1_array[i]])))
            preservation.append(round(inter / float(len(mod3_dict[comm3_array[i]])), 4))

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



