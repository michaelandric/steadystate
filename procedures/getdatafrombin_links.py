#!/usr/bin/python

import os
from optparse import OptionParser
from struct import *
import numpy as np


class LinksCor:

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

        (self.options, args) = self.parser.parse_args()

    def getbin_data(self):
        input = "cleanTS."+self.options.condition+"."+self.options.subject+"_graymask_dump.bin.corr"
        nvox = int(self.options.nvoxels)
        f = open(input,'rb')
        self.f_out = unpack('f'*(nvox*nvox),f.read(4*(nvox*nvox)))

    def getbin_data2(self):
        """
        Trying to unpack and write out entire matrix. This could be massive.
        """
        input = "cleanTS."+self.options.condition+"."+self.options.subject+"_graymask_dump.bin.corr"
        nvox = int(self.options.nvoxels)
        f = open(input,'rb')
        self.f_out = unpack('f'*(nvox*nvox),f.read(4*(nvox*nvox)))

        #np.triu(np.array(f_out).reshape(nvox,nvox), 1)   # gives the upper triangle and zeros out the diagonal
        #sorted(zip(aa, range(16)))   # where aa is a tuple 
        #np.where(np.triu(np.array(range(1,17)).reshape(4,4), 1))   # returns two arrays, an 'x' and a 'y' array, giving x, y of non-zero elements
        # ((n*n) / 2.000) - (n/2.000)   # this tells how many values in the upper triangle (with the diagonal zeroed out)
        """
        I used the above formula to find that only the upper triangle is kept in the correlation matrix construction
        >>> len(np.where(np.triu(np.array(f_out).reshape(nvox,nvox), 1))[0])
        50939371
        >>> ((nvox*nvox) / 2.000) - (nvox/2.000)
        50939371.0
        
        Below gives tuples for every pair:
        tt = []
        for x in range(4):
            for j in range(4):
                tt.append((x,j))

        can then:
        zip(aa, tt)

        
        xy_pairs = []
        for x in range(nvox):
            for j in range(nvox):
                xy_pairs.append((x, j))

        Alternative way to do this:
        x = np.repeat(range(nvox),nvox)
        y = np.tile(range(nvox), nvox)
        xy_pairs = zip(x, y)



        f_out_xy_pairs = zip(f_out, xy_pairs)
        f_out_xy_pairs = sorted(f_out_xy_pairs)


        Making list out of matrix array
        np.array(np.triu(np.array(aa).reshape(nn,nn), 1)).reshape(-1).tolist()

        The elements kept in upper triangle:
        [ii[0] for ii in enumerate(np.array(np.triu(np.array(aa).reshape(nn,nn), 1)).reshape(-1).tolist()) if ii[1] != 0.0]

        """

 
        outname = os.environ["state"]+"/links_files/"+self.options.subject+"."+self.options.condition+".corr_links"
        outf = open(outname, "w")
        outf.write()
        outf.close()
    
    def links_with_cor(self):
        links = "cleanTS."+self.options.condition+"."+self.options.subject+"_graymask_dump.bin.corr.thresh.links"
        f_links = open(links,'r')

        nvox = int(self.options.nvoxels)
        links_cor = ""
        for line in f_links:
            a, b = line.split()
            corval = '%.4f' % self.f_out[(int(a)*nvox) + int(b)]
            links_cor += a+" "+b+" "+corval+"\n"

        outname = os.environ["state"]+"/links_files/"+self.options.subject+"."+self.options.condition+".links_corval"
        outf = open(outname,"w")
        outf.write(links_cor)
        outf.close()

def main():
    LC = LinksCor()
    LC.get_opts()
    os.chdir(os.environ["state"]+"/"+LC.options.subject+"/corrTRIM_BLUR/")
    print os.getcwd()
    LC.getbin_data()
    LC.links_with_cor()

if __name__ == "__main__":
    main()


