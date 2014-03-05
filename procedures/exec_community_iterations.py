#!/usr/bin/python

from makesubmitargs import makeargs as mm


#subjects = ["ANGO"]
subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"] # ANGO, BARS & EZCR not in here

conditions = range(1,5)
densities = ["5p", "8p", "12p", "15p"]


#Now just doing all iterations within the script 70.community_iterations.py
#totaliters = 100
#batch = 50
#startfinish = [(i, i+(batch-1)) for i in range(1, totaliters+1, batch)]

for ss in subjects:
    for de in densities:
        for cc in conditions:
            #mm.blondel_iterations(ss, cc, item[0], item[1])   # was for the previous attempt at batches set here
            mm.community_iterations(ss, de, cc)


