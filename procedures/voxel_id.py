#!/usr/bin/python

import os
from optparse import OptionParser

class VoxelID:

    def get_opts(self):
        desc = """simple program for doing trimming the time series"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 8.Nov.2012")
        self.parser.add_option("--number_voxels", dest="nvox",
                               help="specify the number of voxels")
        self.parser.add_option("--subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def voxel_index(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject)
        print os.getcwd()

        ijk_coords = open("ijk_coords_"+self.options.subject,"r")
        icoord = []
        jcoord = []
        kcoord = []
        for line in ijk_coords:
            i, j, k = line.split()
            icoord.append(i)
            jcoord.append(j)
            kcoord.append(k)

        nn = ""
        for i in range(int(self.options.nvox)):
            nn += icoord[i]+" "+jcoord[i]+" "+kcoord[i]+" "+`i`+"\n"

        self.outname = self.options.subject+"voxel_index.ijk"

        outf = open(self.outname+".txt","w")
        outf.write(nn)
        outf.close()

    def undump(self):
        print os.system("3dUndump -prefix "+self.outname+" -ijk -datum short -master blur.1."+self.options.subject+".steadystate+orig "+self.outname+".txt")

    def AFNItoNIFTI(self):
        print os.system("3dAFNItoNIFTI "+self.outname+"+orig")



ID = VoxelID()
ID.get_opts()
ID.voxel_index()
ID.undump()
ID.AFNItoNIFTI()
