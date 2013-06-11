#!/usr/bin/python

import os
import makesubmitargs

batch = 10000
totalvox = 231203
starts = range(0,totalvox,batch)
ends = []
for i in starts:
    ends.append(i+(batch-1))

ends[len(ends)-1] = totalvox-1

mm = makesubmitargs.makeargs

for cc in range(3,5):
    for i in range(0,len(starts)):
        mm.major_noderoleargs(starts[i],ends[i],cc)

