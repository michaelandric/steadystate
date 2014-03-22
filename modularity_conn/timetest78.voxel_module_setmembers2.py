#!/usr/bin/python

import timeit

setup = '''
import os
import sys
from glob import glob

def tester():

    def set_consist(ss, ia, ib, input1, input2):

        comf3 = open(input2).readlines()
        comf1 = open(input1).readlines()

        comm1_array = []
        voxID1_array = []
        comm3_array = []
        voxID3_array = []

        for line in comf1:
            a, b = map(int, line.split())
            voxID1_array.append(a)
            comm1_array.append(b)

        for line in comf3:
            a, b = map(int, line.split())
            voxID3_array.append(a)
            comm3_array.append(b)

        vox_comm3_array = zip(voxID3_array, comm3_array)
        vox_comm1_array = zip(voxID1_array, comm1_array)
        
        uniq3_modules = set(comm3_array)
        uniq1_modules = set(comm1_array)

        mod3_dict = {}
        for i in uniq3_modules:
            mod3_dict[i] = [item for item in vox_comm3_array if item[1]==i]

        mod1_dict = {}
        for i in uniq1_modules:
            mod1_dict[i] = [item for item in vox_comm1_array if item[1]==i]

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
            #len(set(tmp3) & set(tmp1))
            preservation.append(round(len(set(tmp3).intersection(set(tmp1))) / float(len(tmp3)), 4))
            #preservation.append(round(float(len(set(tmp3) & set(tmp1))) / float(len(tmp3)), 4))
        
        pres_out = ""
        for line in preservation:
            pres_out += str(round(line,4))+' '

        outname = os.environ["state"]+"/"+ss+"/modularity5p/set_consistency/preserved_iters_"+ia+"_"+ib+"_"+ss+".txt"
        #outf = open(outname, "w")
        #outf.write(pres_out)
        #outf.close()



    #if __name__ == "__main__":

        #participant = sys.argv[1]
    participant = "ANGO"
    os.chdir(os.environ["state"]+"/"+participant+"/modularity5p/")
    print os.getcwd()

    combos = []
    cca = 1
    ccb = 1
    for i in range(1, 3):
        for j in range(1, 3):
            if i == j:
                continue
            else:
    #                combos.append((i, j))
    #                ia = sys.argv[2]
    #                ib = sys.argv[3]
                input1name = "iter"+`i`+"."+participant+"."+`cca`+".5p_r0.5_linksthresh_proportion.out.maxlevel_tree" 
                input2name = "iter"+`j`+"."+participant+"."+`ccb`+".5p_r0.5_linksthresh_proportion.out.maxlevel_tree" 

                print i,j
                set_consist(participant, `i`, `j`, input1name, input2name)
'''

#print timeit.Timer('set_consist(participant, `i`, `j`, input1name, input2name)', setup=setup).repeat(7, 1000)
#print setup
print min(timeit.Timer('tester()', setup=setup).repeat(1, 3))

