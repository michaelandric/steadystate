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
    f3 = glob("cleanTS.3.*justcomm")
    fl = glob("cleanTS.1.*justcomm")
    com3f = open(''.join(f3))
    com1f = open(''.join(f1))
    link3f_name = "/mnt/tier2/urihas/Andric/steadystate/graymask_links/"+ss+".3.links_corval"
    link1f_name = "/mnt/tier2/urihas/Andric/steadystate/graymask_links/"+ss+".1.links_corval"
    link3f = open(link3f_name)
    link1f = open(link1f_name)

    """
    get module identifiers
    """
    comm_array = []
    for line in inputf:
        comm_array.append([int(x) for x in line.split()][0])

    """
    get links
    """
    link3_pair = []
    for line in link3f:
        link3_pair.append((int(line.split()[0]), int(line.split()[1])))

    link1_pair = []
    for line in link1f:
        link1_pair.append((int(line.split()[0]), int(line.split()[1])))

    """
    See if link in condition3 if in condition1 too
    """
    res = [rec for rec in set(link3_pair) if rec in set(link1_pair)] 
    

    """
    Now see if voxels link within module
    """
    same_comm = []
    link_both = []
    for line in link3_pair:
        if comm_array[int(link3_pair[0][0])] == comm_array[int(link3_pair[0][1])]: ## within-module filter: finds 'if' the community IDs are same for the two voxels that make the link
            for i in link3_pair:
                for v in link1_pair:
                    if i == v and if comm_array[int(link1_pair[0][0])] == comm_array[int(link1_pair[0][1])]: ## 'if' the link also in condition 1 AND if they still in the same community
                        link_both.append(i)

            same_comm.append("YES")
            if comm_array[int(link1_pair[0][0])] == comm_array[int(link1_pair[0][1])]:
                link_both.append(link_pair[]) 
        else:
            same_comm.append("NO")


    """
    See if voxel pair also in Highly ordered condition
    """

res = [rec for rec in link3_pair if rec in link1_pair] ## see below
[rec for rec in t33 if rec in t11] ## this gives the 'rec' in a list (t33) if it's also in (t11)
##[i for i, v in enumerate(t3) if v[0] == '1' and v[1] == '212']
##[e for e in comm_array if e==3]
