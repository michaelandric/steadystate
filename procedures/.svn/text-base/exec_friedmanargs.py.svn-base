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

for i in range(0,len(starts)):
    mm.friedmanargs(starts[i],ends[i])
