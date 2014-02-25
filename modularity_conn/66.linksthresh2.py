#!/usr/bin/python

import os
from optparse import OptionParser
import numpy as np
from struct import *
import time


class CorLinks:

    def get_opts(self):
        desc = """simple program for doing trimming the time series"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Dec.2012")
        self.parser.add_option("--subject", dest="subject",
                               help="specify the subject")
        self.parser.add_option("--number_voxels", dest="nvoxels",
                               help="specify the number of voxels")
        self.parser.add_option("--condition", dest="condition",
                               help="specify the condition")
        self.parser.add_option("--links_count", dest="linkcount",
                               help="specify the amount of links to keep")

        (self.options, args) = self.parser.parse_args()
        
    
    def links_thresh(self):

        for cc in [1,2,3,4]:
            print `cc`
            print (time.strftime("%H:%M:%S"))

            nvox = int(self.options.nvoxels)
            input = "cleanTS."+`cc`+"."+self.options.subject+"_graymask_dump.bin.corr"
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

            cutoff_f_out = f_out_UTfilter_sorted[(len(f_out_UTfilter_sorted)-4768000):]
            cutoff_UTfilter_new_order = UTfilter_new_order[(len(f_out_UTfilter_sorted)-4768000):]

            f_new = list(np.repeat(0, len(f_out)))
            f_new = np.array(np.repeat(0.0, len(f_out)))
            f_new[cutoff_UTfilter_new_order] = cutoff_f_out

            outname = os.environ["state"]+"/links_files/"+self.options.subject+"."+`cc`+".0.5median_linksthresh.out"
            #outname = "ANGO.2.test_linksthresh.out"
            fo = open(outname, "wb")
            fo.write(pack('f'*(nvox*nvox), *f_new))   # new_f_out is really a list. The R code takes inputs that organize as links and matrices
            fo.close()
            print (time.strftime("%H:%M:%S"))

        
def main():
    LC = CorLinks()
    LC.get_opts()
    os.chdir(os.environ["state"]+"/"+LC.options.subject+"/corrTRIM_BLUR/")
    print os.getcwd()
    LC.links_thresh()
    
if __name__ == "__main__":
    main()


