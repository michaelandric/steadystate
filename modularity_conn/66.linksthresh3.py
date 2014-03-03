#!/usr/bin/python

import os
from optparse import OptionParser
import numpy as np
from struct import *
import time


#subject_list = ["EEPA","DNLN","CRFO"]
#subject_list = ["ANMS","MRZM","MRVV"]
#subject_list = ["MRZM","MRVV"]
#subject_list = ["MRMK","MRMC","MRAG"]
#subject_list = ["SNNW","LDMW","FLTM"]
#subject_list = ["MNGO","LRVN","CLFR"]

#subject_list = ["ANGO", "EEPA", "DNLN", "CRFO", "ANMS", "MRZM", "MRVV", "PIGL", "MRAG", "MYTP"]
subject_list = ["SNNW", "MRMC", "LDMW", "FLTM", "MNGO", "LRVN", "CLFR", "MRMK", "TRCO"]

nvox_dict = {'BARS': 10023, 'FLTM': 12215, 'MRZM': 9044, 'ANMS': 10879, 'MRAG': 10235, 'ANGO': 10094, 'PIGL': 10927, 'MRMK': 10885, 'CRFO': 11786, 'EEPA': 10884, 'TRCO': 10753, 'MRMC': 12938, 'SNNW': 11735, 'LDMW': 10612, 'LRVN': 10633, 'MRVV': 9541, 'DNLN': 11296, 'CLFR': 10946, 'MYTP': 10699, 'MNGO': 11001}

median_proportion_links = {'MRMK': 8651298, 'MRVV': 1493433, 'FLTM': 9576512, 'MRZM': 7398024, 'ANMS': 7773906, 'ANGO': 1578799, 'PIGL': 2431684, 'CLFR': 1414788, 'CRFO': 8103050, 'EEPA': 7898114, 'TRCO': 3864182, 'MRMC': 25947183, 'SNNW': 8810777, 'DNLN': 15801113, 'LRVN': 2091584, 'MRAG': 2486906, 'LDMW': 5161122, 'MYTP': 7941891, 'MNGO': 1913600}   # this corresponds to 0.5 Pearson


def links_thresh(subject, nvoxels):

    for cc in [1,2,3,4]:
        print `cc`
        print (time.strftime("%H:%M:%S"))

        nvox = int(nvoxels)
        input = "cleanTS."+`cc`+"."+subject+"_graymask_dump.bin.corr"
        f = open(input, "rb")
        f_out = unpack('f'*(nvox*nvox),f.read(4*(nvox*nvox)))
        UT = [ii[0] for ii in enumerate(np.array(np.triu(np.array(np.repeat(1, (nvox*nvox))).reshape(nvox, nvox), 1)).reshape(-1).tolist()) if ii[1] !=0]   # upper triangle index
        f_out_UT = np.array(f_out)[UT]

        v, b = np.histogram(f_out_UT, bins = 4)

        f_out_UTfilter = f_out_UT[f_out_UT > b[2]]
        UTarray = np.array(UT)
        UTfilter = UTarray[f_out_UT > b[2]]

        f_out_UTfilter_sorted = np.sort(f_out_UTfilter, kind = 'mergesort')
        UTfilter_new_order = UTfilter[np.argsort(f_out_UTfilter, kind = 'mergesort')]

        """
        This section is for absolute median observed links cutoff (at 0.5 Pearson)
        cutoff_f_out = f_out_UTfilter_sorted[(len(f_out_UTfilter_sorted)-4768000):]
        cutoff_UTfilter_new_order = UTfilter_new_order[(len(f_out_UTfilter_sorted)-4768000):]
        """
        cutoff_f_out = f_out_UTfilter_sorted[(len(f_out_UTfilter_sorted) - median_proportion_links[subject]):]
        cutoff_UTfilter_new_order = UTfilter_new_order[(len(f_out_UTfilter_sorted) - median_proportion_links[subject]):]

        #f_new = list(np.repeat(0, len(f_out)))
        f_new = np.array(np.repeat(0.0, len(f_out)))
        f_new[cutoff_UTfilter_new_order] = cutoff_f_out

        #outname = os.environ["state"]+"/links_files/"+subject+"."+`cc`+".0.5median_linksthresh.out"
        outname = os.environ["state"]+"/links_files/"+subject+"."+`cc`+".0.5median_linksthresh_proportion.out"   # for median completeness proportional for each ss 
        fo = open(outname, "wb")
        fo.write(pack('f'*(nvox*nvox), *f_new))   # new_f_out is really a list. The R code takes inputs that organize as links and matrices
        fo.close()
        print (time.strftime("%H:%M:%S"))


print subject_list
for subject in subject_list:
    os.chdir(os.environ["state"]+"/"+subject+"/corrTRIM_BLUR/")
    print os.getcwd()
    links_thresh(subject, nvox_dict[subject])
        

