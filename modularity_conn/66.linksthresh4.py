#!/usr/bin/python

import os
from optparse import OptionParser
import numpy as np
from struct import *
import time


#subject_list = ["ANGO"]
#subject_list = ["EEPA", "DNLN", "CRFO", "ANMS", "MRZM", "MRVV", "PIGL", "MRAG", "MYTP"]
subject_list = ["SNNW", "MRMC", "LDMW", "FLTM", "MNGO", "LRVN", "CLFR", "MRMK", "TRCO"]

nvox_dict = {'BARS': 10023, 'FLTM': 12215, 'MRZM': 9044, 'ANMS': 10879, 'MRAG': 10235, 'ANGO': 10094, 'PIGL': 10927, 'MRMK': 10885, 'CRFO': 11786, 'EEPA': 10884, 'TRCO': 10753, 'MRMC': 12938, 'SNNW': 11735, 'LDMW': 10612, 'LRVN': 10633, 'MRVV': 9541, 'DNLN': 11296, 'CLFR': 10946, 'MYTP': 10699, 'MNGO': 11001}

dict5p = {'MRMK': 2961808, 'MRVV': 2275528, 'FLTM': 3729850, 'MRZM': 2044622, 'ANMS': 2958544, 'ANGO': 2546969, 'PIGL': 2984710, 'CLFR': 2995099, 'CRFO': 3472450, 'EEPA': 2961264, 'TRCO': 2890406, 'MRMC': 4184473, 'SNNW': 3442462, 'DNLN': 3189708, 'LRVN': 2826251, 'MRAG': 2618625, 'LDMW': 2815098, 'MYTP': 2861448, 'MNGO': 3025275}

dict8p = {'MRMK': 5153547, 'MRVV': 3959420, 'FLTM': 6489939, 'MRZM': 3557643, 'ANMS': 5147867, 'ANGO': 4431725, 'PIGL': 5193395, 'CLFR': 5211473, 'CRFO': 6042063, 'EEPA': 5152600, 'TRCO': 5029307, 'MRMC': 7280982, 'SNNW': 5989884, 'DNLN': 5550092, 'LRVN': 4917677, 'MRAG': 4556407, 'LDMW': 4898271, 'MYTP': 4978919, 'MNGO': 5263978}

dict12p = {'MRMK': 7108340, 'MRVV': 5461268, 'FLTM': 8951641, 'MRZM': 4907094, 'ANMS': 7100506, 'ANGO': 6112725, 'PIGL': 7163304, 'CLFR': 7188238, 'CRFO': 8333881, 'EEPA': 7107034, 'TRCO': 6936975, 'MRMC': 10042734, 'SNNW': 8261909, 'DNLN': 7655299, 'LRVN': 6783003, 'MRAG': 6284699, 'LDMW': 6756236, 'MYTP': 6867474, 'MNGO': 7260660}

dict15p = {'MRMK': 8885426, 'MRVV': 6826586, 'FLTM': 11189551, 'MRZM': 6133867, 'ANMS': 8875632, 'ANGO': 7640906, 'PIGL': 8954130, 'CLFR': 8985298, 'CRFO': 10417351, 'EEPA': 8883793, 'TRCO': 8671219, 'MRMC': 12553418, 'SNNW': 10327387, 'DNLN': 9569124, 'LRVN': 8478754, 'MRAG': 7855874, 'LDMW': 8445295, 'MYTP': 8584343, 'MNGO': 9075825}

def links_thresh(subject, nvoxels):

    links_limits = [x for x in dict15p[subject], dict12p[subject], dict8p[subject], dict5p[subject]]
    threshes = [15, 12, 8, 5]
    limits_dict = dict(zip(threshes, links_limits))
    print limits_dict
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

        for limit in limits_dict:
            print `limit`+" /// "+time.strftime("%H:%M:%S")
            f_new = np.array(np.repeat(0.0, len(f_out)))
            cutoff_f_out = f_out_UTfilter_sorted[(len(f_out_UTfilter_sorted) - limits_dict[limit]):]
            cutoff_UTfilter_new_order = UTfilter_new_order[(len(f_out_UTfilter_sorted) - limits_dict[limit]):]
            f_new[cutoff_UTfilter_new_order] = cutoff_f_out
#
            outname = os.environ["state"]+"/links_files"+`limit`+"p/"+subject+"."+`cc`+"."+`limit`+"p_r0.5_linksthresh_proportion.out"   # for median completeness proportional for each ss 
            fo = open(outname, "wb")
            fo.write(pack('f'*(nvox*nvox), *f_new))   # new_f_out is really a list. The R code takes inputs that organize as links and matrices
            fo.close()

        print (time.strftime("%H:%M:%S"))


print subject_list
for subject in subject_list:
    os.chdir(os.environ["state"]+"/"+subject+"/corrTRIM_BLUR/")
    print os.getcwd()
    links_thresh(subject, nvox_dict[subject])
        

