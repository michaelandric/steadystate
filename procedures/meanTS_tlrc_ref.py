#!/usr/bin/python

import os
from optparse import OptionParser

class MeanTLRC:

    def get_opts(self):
        desc = """simple program for doing trimming the time series"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 8.Nov.2012")
        self.parser.add_option("--subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def meanTS(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject)
        print os.system("3dTstat -mean -prefix avg.blur.1."+self.options.subject+".steadystate.TRIM blur.1."+self.options.subject+".steadystate.TRIM+orig")
        print os.system("3dAFNItoNIFTI avg.blur.1."+self.options.subject+".steadystate.TRIM+orig")

    def tlrc_transform_template(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject)
        print os.system("fslcreatehd 45 55 45 1 4 4 4 1 0 0 0 16 avg.blur.1."+self.options.subject+"_tlrc_tmp.nii.gz ; flirt -in avg.blur.1."+self.options.subject+".steadystate.TRIM.nii -applyxfm -init /mnt/tier2/urihas/Software/fsl/etc/flirtsch/ident.mat -out avg.blur.1."+self.options.subject+"_tlrc -paddingsize 0.0 -interp trilinear -ref avg.blur.1."+self.options.subject+"_tlrc_tmp")

    def tlrc_transform_data(self):
        os.chdir(os.environ["state"]+"/"+self.options.subject)
        print os.system("flirt -in "+self.options.subject+"voxel_index.ijk.nii -ref avg.blur.1."+self.options.subject+"_tlrc.nii.gz -out "+self.options.subject+"voxel_index.ijk_tlrc -omat "+self.options.subject+"voxel_index.ijk_tlrc.mat -bins 256 -cost corratio -searchrx -180 180 -searchry -180 180 -searchrz -180 180 -dof 12 -interp nearestneighbour")
        

ex = MeanTLRC()
ex.get_opts()
ex.meanTS()
#ex.tlrc_transform_template()
#ex.tlrc_transform_data()
