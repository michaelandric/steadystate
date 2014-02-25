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

        """
        #np.triu(np.array(f_out).reshape(nvox,nvox), 1)   # gives the upper triangle and zeros out the diagonal
        #sorted(zip(aa, range(16)))   # where aa is a tuple 
        #np.where(np.triu(np.array(range(1,17)).reshape(4,4), 1))   # returns two arrays, an 'x' and a 'y' array, giving x, y of non-zero elements
        # ((n*n) / 2.000) - (n/2.000)   # this tells how many values in the upper triangle (with the diagonal zeroed out)
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
        
        Gives indicies for which elements to keep
        #keepers = [ii[0] for ii in enumerate(np.array(np.triu(np.array(np.repeat(1, 16)).reshape(nn, nn), 1)).reshape(-1).tolist()) if ii[1] !=0 ]
        f_out_keepers = [ii[0] for ii in enumerate(np.array(np.triu(np.array(np.repeat(1, (nvox*nvox))).reshape(nvox, nvox), 1)).reshape(-1).tolist()) if ii[1] !=0 ]
        
        f_out_uppertri = []
        xy_uppertri = []
        for k in f_out_keepers:
            f_out_uppertri.append((f_out[k], k))
            #xy_uppertri.append(xy_pairs[k])
        
        
        
        keepers = [ii[0] for ii in enumerate(np.array(np.triu(np.array(np.repeat(1, 16)).reshape(nn, nn), 1)).reshape(-1).tolist()) if ii[1] !=0 ]
        aa_keepers = []
        for ii in keepers:
            aa_keepers.append((aa[ii], ii))
        
        new_aa = list(np.repeat(0, len(aa)))
        aa_keepers_cut = sorted(aa_keepers, reverse = True)[0:(int(len(aa)*(1/8.000)))]
        
        for el in aa_keepers_cut:
            new_aa[el[1]] = el[0]
        
        np.array(new_aa).reshape(4,4)
        #new_aa_array = np.array(new_aa).reshape(nn,nn)

        fo = open("myfile","wb")
        fo.write(pack('f'*(nn*nn), *new_aa))
        fo.close()
        
        
def qsort(inlist):
    if inlist == []: 
        yield []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        yield lesser + [pivot] + greater
        
        ______________________________________________________________________
        """
        
        keepers = [ii[0] for ii in enumerate(np.array(np.triu(np.array(np.repeat(1, (nvox*nvox))).reshape(nvox, nvox), 1)).reshape(-1).tolist()) if ii[1] !=0]   # This gives index to upper triangle values, also excludes diagonal (self-connections)
        #f_out_keepers = []
        #for ii in keepers:
        #    f_out_keepers.append((f_out[ii], ii))
            
        f_out_keepers = ((f_out[ii], ii) for ii in keepers)
        f_out_keepers_cut = sorted(f_out_keepers, reverse = True)[0:(int(len(f_out) * .05))]   # This is where I threshold by links. 5% here is 10% of upper triangle (i.e., unique links available)
        
        
        new_f_out = list(np.repeat(0, len(f_out)))
        for el in f_out_keepers_cut:
            new_f_out[el[1]] = el[0]
            
        #new_f_out[el[1]] = el[0] for el in f_out_keepers_cut
        
        #outname = os.environ["state"]+"/links_files/"+self.options.subject+"."+self.options.condition+".links_thresh"
        outname = os.environ["state"]+"/links_files/"+subject+"."+condition+".links_thresh"
        fo = open(outname, "wb")
        fo.write(pack('f'*(nvox*nvox), *new_f_out))   # new_f_out is really a list. The R code takes inputs that organize as links and matrices
        fo.close()

    
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
    LC.getbin_data2()

if __name__ == "__main__":
    main()


