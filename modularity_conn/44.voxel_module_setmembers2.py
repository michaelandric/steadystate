#!usr/bin/python

"""
Find whether voxels part of a module in one condition prune or reorganize
"prune" -> Partition big module into sub-modules
"reorganize" -> different connections, voxels are that were together in one module are now in different modules
"""

import os
from glob import glob

conditions = range(1,5)
subjects = ["ANGO","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"]

for ss in subjects:
    os.chdir(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/")
    print os.getcwd()
    """
    Get the community (module) IDs for conditions 1 and 3
    """
    f3 = glob("cleanTS.3.*justcomm")
    f1 = glob("cleanTS.1.*justcomm")
    comf3 = open(''.join(f3))
    comf1 = open(''.join(f1))
    """
    Get the links files for conditions 1 and 3
    """
    link3f_name = "/mnt/tier2/urihas/Andric/steadystate/graymask_links/"+ss+".3.links_corval"
    link1f_name = "/mnt/tier2/urihas/Andric/steadystate/graymask_links/"+ss+".1.links_corval"
    link3f = open(link3f_name)
    link1f = open(link1f_name)

    """
    get module identifiers
    """
    comm3_array = []
    for line in comf3:
        comm3_array.append([int(x) for x in line.split()][0])

    comm1_array = []
    for line in comf1:
        comm1_array.append([int(x) for x in line.split()][0])
    
    """
    Make two column arrays 
    Column 1 are voxel IDs and Column 2 are module IDs
    """
    vox_comm3_array = zip(range(len(comm3_array)), comm3_array)
    vox_comm1_array = zip(range(len(comm1_array)), comm1_array)
    
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
    for i in range(len(comm3_array)):
        tmp3 = []
        tmp1 = []

        for item in mod3_dict[vox_comm3_array[i][1]]:
            tmp3.append(item[0]) ## these are the voxels in a module with voxel 'i'

        for item in mod1_dict[vox_comm1_array[i][1]]:
            tmp1.append(item[0])

        #pruning = [filter(lambda x: x in tmp3, sublist) for sublist in tmp1]
        #len_tmp_intersect = len([x in for x in tmp3 if x in tmp1])
        len(set(tmp3) & set(tmp1))
        preservation.append(round(float(len(set(tmp3) & set(tmp1))) / float(len(tmp3)), 4))
    
    pres_out = ""
    for line in preservation:
        pres_out += str(round(line,4))+"\n"

    outf = open("preserved_"+ss+".txt","w")
    outf.write(pres_out)
    outf.close()

