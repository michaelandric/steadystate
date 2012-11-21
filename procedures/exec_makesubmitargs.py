#!/usr/bin/python

"""
Here's how you use this on the command line:
python exec_makesubmitargs.py >> submit.try
where 'submit.try' is the condor_submit file that you're adding arguments to
"""
import commands
from makesubmitargs import makeargs as mm

#subjects = ["ANGO"]
#subjects = ["MYTP","TRCO","CLFR","PIGL","SNNW"]
#subjects = ["LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS"]
#subjects = ["MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"]
##subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"] #CLFR & ANGO not in here
subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"] # ANGO & EZCR not in here
conditions = range(1,5)

"""
nvox_dict subject to the number of voxels in the image. 
This goes by the voxels in the graymattermask
"""
nvox_dict = {'BARS': 10023, 'FLTM': 12215, 'MRZM': 9044, 'ANMS': 10879, 'MRAG': 10235, 'ANGO': 10094, 'PIGL': 10927, 'MRMK': 10885, 'CRFO': 11786, 'EEPA': 10884, 'TRCO': 10753, 'MRMC': 12938, 'SNNW': 11735, 'LDMW': 10612, 'LRVN': 10633, 'MRVV': 9541, 'DNLN': 11296, 'CLFR': 10946, 'MYTP': 10699, 'MNGO': 11001}

"""
'tree_d' is a dictionary with the highest hierarachial levels.
This dictionary was generated with 'get_level.py'
CURRENTLY DOES NOT INCLUDE 'EZCR' - COULDN'T GET SEGMENTATION FOR MASK WITH THIS SS
"""
tree_d = {'BARS': (2, 2, 2, 2), 'FLTM': (3, 3, 2, 2), 'MRZM': (2, 2, 3, 2), 'ANMS': (2, 2, 2, 2), 'MRAG': (2, 2, 2, 3), 'ANGO': (3, 3, 3, 2), 'PIGL': (3, 3, 3, 3), 'MRMK': (2, 2, 2, 2), 'CRFO': (2, 3, 2, 2), 'EEPA': (3, 2, 3, 2), 'TRCO': (2, 2, 3, 3), 'MRMC': (2, 2, 2, 2), 'SNNW': (3, 2, 2, 3), 'LDMW': (2, 3, 2, 2), 'LRVN': (2, 2, 2, 2), 'MRVV': (3, 3, 2, 3), 'DNLN': (2, 2, 1, 3), 'CLFR': (3, 2, 3, 2), 'MYTP': (3, 3, 3, 3), 'MNGO': (2, 3, 3, 3)}
hemispheres = ["lh","rh"]


#mm.ijkTALAIRACHcoordsargs("TTavg152T1","automask_d1")

for ss in subjects:
    #mm.ijkcoordsargs(ss)
    mm.autotlrcargs(ss)
    #mm.voxel_id_args(ss, dictionary[ss])
    #mm.maskdumpargs(ss)
    #mm.maskmakerargs(ss)
    #for cc in conditions:
        #for i in range(dictionary2[ss][cc-1]+1): 
        #mm.maskdumpargs(ss,cc)
        #mm.fcorrargs(ss,cc)
        #mm.threshargs(ss,cc) ## for submit.6.threshold
        #mm.convertargs(ss,cc) ## for submit.7.blondel_convert
        #mm.blondelargs(ss,cc) ## for submit.8.blondel
        #mm.hierarchyargs(ss,cc,tree_d[ss][cc-1])
        #mm.undumpargs(ss,cc,tree_d[ss][cc-1])
        #mm.filter(ss,cc,dictionary2[ss][cc-1]) ## for submit.13.filter
        #mm.undump14(ss,cc,dictionary2[ss][cc-1],1)
        #mm.degree(ss,nvox_dict[ss],cc)


