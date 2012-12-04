#!/usr/bin/python

from subprocess import call


subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR","ANG\
O"]
nvox_dict = {'BARS': 10023, 'FLTM': 12215, 'MRZM': 9044, 'ANMS': 10879, 'MRAG': 10235, 'ANGO': 10094, 'PIGL': 10927, 'MRMK': 10885, 'CRFO': 11786, 'EEPA': 10884, 'TRCO': 10753, 'MRMC': 12938, 'SNNW': 11735, 'LDMW': 10612, 'LRVN': 10633, 'MRVV': 9541, 'DNLN': 11296, 'CLFR': 10946, 'MYTP': 10699, 'MNGO': 11001}
conditions = range(1,5)

for ss in subjects:
    for cc in conditions:
        cmd = "./getdatafrombin.py --subject "+ss+" --number_voxels "+str(nvox_dict[ss])+" --condition "+str(cc)
        print cmd
        call(cmd, shell=True)
