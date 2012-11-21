#!/usr/bin/python

"""
Here's how you use this on the command line:
python exec_makesubmitargs.py >> submit.try
where 'submit.try' is the condor_submit file that you're adding arguments to
"""
import commands
import makesubmitargs

#subjects = ["ANGO"]
#subjects = ["MYTP","TRCO","CLFR","PIGL","SNNW"]
#subjects = ["LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS"]
#subjects = ["MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"]
##subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"] #CLFR & ANGO not in here
subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"] # ANGO & EZCR not in here
conditions = range(1,5)

"""
this is the dictionary that maps nvox to subject
"""
dictionary = {'EZCR': '31902', 'FLTM': '32555', 'MRZM': '23081', 'MRMC': '29045', 'ANMS': '25009', 'MRAG': '26830', 'ANGO': '22170', 'PIGL': '26253', 'CLFR': '24883', 'CRFO': '28632', 'EEPA': '30432', 'TRCO': '28705', 'MRMK': '26331', 'SNNW': '27839', 'BARS': '28340', 'LDMW': '27133', 'LRVN': '26562', 'MRVV': '24476', 'DNLN': '25884', 'MYTP': '26202', 'MNGO': '28266'}

"""
this dictionary gives the highest level (at .5 corr threshold)
"""
#dictionary2 = {'MYTP':(4,3,3,3), 'TRCO':(4,4,4,3), 'CLFR':(4,3,4,3), 'PIGL':(4,4,4,4), 'SNNW':(3,4,3,3)}
#dictionary2 = {"LDMW":(,) ,"FLTM":() ,"EZCR":() ,"EEPA":() ,"DNLN":() ,"CRFO":() ,"ANMS":() ,"BARS":()}
"""
'tree_d' is a dictionary with the highest hierarachial levels.
This dictionary was generated with 'get_level.py'
CURRENTLY DOES NOT INCLUDE 'EZCR' - COULDN'T GET SEGMENTATION FOR MASK WITH THIS SS
"""
tree_d = {'BARS': (2, 2, 2, 2), 'FLTM': (3, 3, 2, 2), 'MRZM': (2, 2, 3, 2), 'ANMS': (2, 2, 2, 2), 'MRAG': (2, 2, 2, 3), 'ANGO': (3, 3, 3, 2), 'PIGL': (3, 3, 3, 3), 'MRMK': (2, 2, 2, 2), 'CRFO': (2, 3, 2, 2), 'EEPA': (3, 2, 3, 2), 'TRCO': (2, 2, 3, 3), 'MRMC': (2, 2, 2, 2), 'SNNW': (3, 2, 2, 3), 'LDMW': (2, 3, 2, 2), 'LRVN': (2, 2, 2, 2), 'MRVV': (3, 3, 2, 3), 'DNLN': (2, 2, 1, 3), 'CLFR': (3, 2, 3, 2), 'MYTP': (3, 3, 3, 3), 'MNGO': (2, 3, 3, 3)}
hemispheres = ["lh","rh"]



mm = makesubmitargs.makeargs
#mm.ijkTALAIRACHcoordsargs("TTavg152T1","automask_d1")

for ss in subjects:
    #mm.ijkcoordsargs(ss)
    #mm.autotlrcargs(ss)
    #mm.voxel_id_args(ss, dictionary[ss])
    #mm.maskdumpargs(ss)
    #mm.maskmakerargs(ss)
    for cc in conditions:
        #for i in range(dictionary2[ss][cc-1]+1): 
        #mm.maskdumpargs(ss,cc)
        #mm.fcorrargs(ss,cc)
        #mm.threshargs(ss,cc) ## for submit.6.threshold
        #mm.convertargs(ss,cc) ## for submit.7.blondel_convert
        #mm.blondelargs(ss,cc) ## for submit.8.blondel
        mm.hierarchyargs(ss,cc,tree_d[ss][cc-1])
        #mm.undumpargs(ss,cc,dictionary2[ss][cc-1])
        #mm.filter(ss,cc,dictionary2[ss][cc-1]) ## for submit.13.filter
        #mm.undump14(ss,cc,dictionary2[ss][cc-1],1)
        #mm.degree(ss,dictionary[ss],cc)


