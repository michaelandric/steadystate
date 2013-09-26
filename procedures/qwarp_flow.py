#!/usr/bin/python

import os
from subprocess import call
from optparse import OptionParser


class QWARP_FLOW:

    def get_opts(self):
        desc = """
        simple program for doing AFNI's 3dQwarp + preceeding recommended steps
        """
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Nov.2012")
        self.parser.add_option("--tlrc_brain", dest="tlrcT1",
                               help="specify the talairach anat")
        self.parser.add_option("--input", dest="input",
                               help="specify the input")
        self.parser.add_option("--Subject", dest="subject",
                               help="specity the subject")

        (self.options, args) = self.parser.parse_args()

    def Unfize(self):
        """
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/masking/")
        print call("3dUnifize -prefix "+self.options.subject+".SurfVol_Alnd_Exp_U -input "+self.options.subject+".SurfVol_Alnd_Exp+orig", shell = True)

    def SkullStrip(self):
        """
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/masking/")
        #print call("3dSkullStrip -input "+self.options.subject+".SurfVol_Alnd_Exp_U+orig -prefix "+self.options.subject+".SurfVol_Alnd_Exp_US -niter 400 -ld 40", shell = True)
        print call("3dSkullStrip -input "+self.options.subject+".SurfVol_Alnd_Exp+orig -prefix "+self.options.subject+".SurfVol_Alnd_Exp_SkSt -niter 400 -ld 40", shell = True)

    def Allineate(self):
        """
        The '-base' is same TT_avg152T1 found in afni program dir
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/masking/")
        print call("3dAllineate -prefix "+self.options.subject+".SurfVol_Alnd_Exp_SkStAl -base /mnt/tier2/urihas/Andric/steadystate/groupstats/TT_avg152T1+tlrc \
                    -source "+self.options.subject+".SurfVol_Alnd_Exp_SkSt+orig -twopass -cost lpa \
                    -1Dmatrix_save "+self.options.subject+".SurfVol_Alnd_Exp_SkStAl.aff12.1D -autoweight -fineblur 3 -cmass", shell = True)

    def Qwarp(self):
        """
        The '-base' is same TT_avg152T1 found in afni program dir
        """
        os.chdir(os.environ["state"]+"/"+self.options.subject+"/masking/")
        print call("3dQwarp -prefix "+self.options.subject+".SurfVol_Alnd_Exp_SkStAlQ -duplo -useweight -blur 0 3 \
                    -base /mnt/tier2/urihas/Andric/steadystate/groupstats/TT_avg152T1+tlrc \
                    -source "+self.options.subject+".SurfVol_Alnd_Exp_SkStAl+tlrc", shell = True)

    def Nwarp(self):
        """
        """
        mask_dir = os.environ["state"]+"/"+self.options.subject+"/masking/"
        data_dir = os.environ["state"]+"/"+self.options.subject+"/corrTRIM_BLUR/"
        print data_dir+"preserved_"+self.options.subject+"+orig"
        print call("3dNwarpApply -nwarp '"+mask_dir+self.options.subject+".SurfVol_Alnd_Exp_SkStAlQ_WARP+tlrc "+mask_dir+self.options.subject+".SurfVol_Alnd_Exp_SkStAl.aff12.1D' \
                    -source "+data_dir+"preserved_"+self.options.subject+"+orig -prefix "+data_dir+"preserved_"+self.options.subject+"_warped", shell = True)


def main():
    qw = QWARP_FLOW()
    qw.get_opts()
    #qw.Unfize()
    #qw.SkullStrip()
    #qw.Allineate()
    #qw.Qwarp()
    qw.Nwarp()

if __name__ == "__main__":
    main()


