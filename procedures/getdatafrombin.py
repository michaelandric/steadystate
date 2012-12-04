#!/usr/bin/python

import os
from optparse import OptionParser
from struct import *

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
    
    def links_with_cor(self):
        links = "cleanTS."+self.options.condition+"."+self.options.subject+"_graymask_dump.bin.corr.thresh.links"
        f_links = open(links,'r')

        nvox = int(self.options.nvoxels)
        links_cor = ""
        for line in f_links:
            a, b = line.split()
            corval = '%.4f' % self.f_out[(int(a)*nvox) + int(b)]
            links_cor += a+" "+b+" "+corval+"\n"

        outname = os.environ["state"]+"/graymask_links/"+self.options.subject+"."+self.options.condition+".links_corval"
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


