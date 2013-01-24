#!/usr/bin/python
"""
This is designed to write out a table with the number of modules for each condition for each sujbect.
Output table structured as:
Subject Condition1 Condition2 Condition3 Condition4
"""

import os

conditions = range(1,5)
subjects = ["ANGO","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"]
"""
'tree_d' is a dictionary with the highest hierarachial levels.
This dictionary was generated with 'get_level.py'
CURRENTLY DOES NOT INCLUDE 'EZCR' - COULDN'T GET SEGMENTATION FOR MASK WITH THIS SS
"""
tree_d = {'BARS': (2, 2, 2, 2), 'FLTM': (3, 3, 2, 2), 'MRZM': (2, 2, 3, 2), 'ANMS': (2, 2, 2, 2), 'MRAG': (2, 2, 2, 3), 'ANGO': (3, 3, 3, 2), 'PIGL': (3, 3, 3, 3), 'MRMK': (2, 2, 2, 2), 'CRFO': (2, 3, 2, 2), 'EEPA': (3, 2, 3, 2), 'TRCO': (2, 2, 3, 3), 'MRMC': (2, 2, 2, 2), 'SNNW': (3, 2, 2, 3), 'LDMW': (2, 3, 2, 2), 'LRVN': (2, 2, 2, 2), 'MRVV': (3, 3, 2, 3), 'DNLN': (2, 2, 1, 3), 'CLFR': (3, 2, 3, 2), 'MYTP': (3, 3, 3, 3), 'MNGO': (2, 3, 3, 3)}

"""
'module_table' is just going to be the output table
"""
module_table = ""

for ss in subjects:
    os.chdir(os.environ["state"]+"/"+ss+"/corrTRIM_BLUR/")
    print os.getcwd()
    max_comms = []
    for cc in conditions:
        inputf = open("cleanTS."+`cc`+"."+ss+"_graymask_dump.bin.corr.thresh.tree"+`tree_d[ss][cc-1]`+".justcomm")
        comm_array = []
        for line in inputf:
            comm_array.append([int(x) for x in line.split()])

        max_comms.append(max(comm_array)[0])

    module_table += ss+" "+`max_comms[0]`+" "+`max_comms[1]`+" "+`max_comms[2]`+" "+`max_comms[3]`+"\n"

"""
now going to write out the table with number of modules
"""
outf = open(os.environ["state"]+"/groupstats/number_modules_table.txt","w")
outf.write(module_table)
outf.close()

