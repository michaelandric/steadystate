#!/usr/bin/python

import os
from optparse import OptionParser

class MakeArgs:
    
    def get_opts(self):
        desc = """Program for generating condor_submit arguments. Run this with 'exec_makesubmitargs.py' to iterate arguments."""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog October.2012")
        self.parser.add_option("--subject", dest="subject",
                               help="specify the subject")
        self.parser.add_option("--arg1", dest="arg1",
                               help="first argument")
        self.parser.add_option("--arg2", dest="arg2",
                               help="second argument")
        self.parser.add_option("--arg3", dest="arg3",
                               help="third argument")
        self.parser.add_option("--arg4", dest="arg4",
                               help="fourth argument")

        (self.options, args) = self.parser.parse_args()

    def spliceargs(self):
        ##arg1 == Condition, e.g., '1'
        outdir = "/mnt/tier2/urihas/Andric/steadystate/"+self.options.subject
        print "arguments    = --OutDir "+outdir+" --Condition "+self.options.arg1+" --Subject "+self.options.subject+" \nqueue \n"

    def autotlrcargs(self,subject):
        print "arguments    = --Subject "+subject+" --tlrc_brain "+subject+"tlrc+tlrc \nqueue \n"

    def maskdumpargsOLD(self):
        """
        arg1 == steadystate dir, e.g., '/mnt/tier2/urihas/Andric/steadystate/'
        arg2 == automask, e.g., 'automask_d3'
        arg3 == Condition, e.g., '1'
        example command line:
        python makesubmitargs.py --subject BARS --arg1 /mnt/tier2/urihas/Andric/steadystate/ --arg2 automask_d3 --arg3 1
        """
        automask = self.options.arg1+self.options.subject+"/"+self.options.arg2+"_"+self.options.subject+"+orig"
        input = self.options.arg1+self.options.subject+"/blur."+self.options.arg3+"."+self.options.subject+".steadystate.TRIM+orig"
        output = self.options.arg1+self.options.subject+"/blur."+self.options.arg3+"."+self.options.subject+".steadystate.TRIM.noijk_dump"
        print "arguments    = --ijk no --automask "+automask+" --inputfile "+input+" --outputname "+output+" \nqueue \n"

    def maskdumpargs(self,subject):
        """
        arg1 is condition
        """
        #automask = os.environ["state"]+"/"+subject+"/masking/"+subject+"_graymattermask_resampled+orig"
        automask = os.environ["state"]+"/"+subject+"/masking/"+subject+"_graymattermask_resampled+tlrc"
        #input = os.environ["state"]+"/"+subject+"/blur."+`arg1`+"."+subject+".steadystate.TRIM+orig"
        input = os.environ["state"]+"/"+subject+"/masking/"+subject+"graymatter_voxel_index.ijk+tlrc"
        #output = os.environ["state"]+"/"+subject+"/blur."+`arg1`+"."+subject+".steadystate.TRIM_graymask_dump"
        output = os.environ["state"]+"/"+subject+"/masking/"+subject+"graymatter_voxel_index_tlrc_dump.txt"
        print "arguments    = --mask "+automask+" --inputfile "+input+" --outputname "+output+" --subject "+subject+" \nqueue \n" 

    def dir_maker(self):
        print "arguments    = --Subject "+self.options.subject+" \nqueue \n"

    def corrargs(self):
        ##arg1 == number of voxels, e.g., 22170
        ##arg2 == Condition, e.g., 2
        print "arguments    = 4.corr.R "+self.options.subject+" "+self.options.arg1+" 90 "+self.options.arg2+" \nqueue \n"

    def fcorrargs(self,subject,arg1):
        sourcedir = os.environ["state"]+"/"+subject+"/"
        outdir = os.environ["state"]+"/"+subject+"/corrTRIM_BLUR/"
        """
        Have to give full path for mask
        """
        mask = os.environ["state"]+"/"+subject+"/masking/"+subject+"_graymattermask_resampled+orig"
        print "arguments    = --subject "+subject+" --source_directory "+sourcedir+" --output_directory "+outdir+" --mask "+mask+" --condition "+`arg1`+" \nqueue \n"

    def threshargs(self,subject,arg1):
        ##arg1 == Condition, e.g., 2
        print "arguments    = 6.thresholdmat.R "+subject+" "+`arg1`+" \nqueue \n"

    def convertargs(self,subject,arg1):
        ##arg1 == Conditions, e.g., 2
        print "arguments    = 7.blondel_convert.R "+subject+" "+`arg1`+" \nqueue \n"

    def blondelargs(self,subject,arg1):
        ##arg1 == Conditions, e.g., 2
        print "arguments    = 8.blondel "+subject+" "+`arg1`+" \nqueue \n"

    def hierarchyargs(self,subject,arg1,arg2):
        """
        arg1 = condition
        arg2 = nlevels
        """
        print "arguments    = 9.hierarchy.R "+subject+" "+`arg1`+" "+`arg2`+" \nqueue \n"

    def ijkcoordsargs(self,subject):
        basedir = os.environ["state"]+"/"
        automask = basedir+subject+"/masking/"+subject+"_graymattermask_resampled+orig"
        ijkmaster = basedir+subject+"/blur.1."+subject+".steadystate.TRIM+orig"
        ijkoutname = basedir+subject+"/masking/ijk_coords_graymattermask_"+subject
        print "arguments    = --automask "+automask+" --ijkmaster "+ijkmaster+" --ijkoutputname "+ijkoutname+" \nqueue \n"

    def ijkTALAIRACHcoordsargs(self,subject,automsk):
        basedir = os.environ["state"]+"/"
        automask = basedir+"groupstats/"+automsk+"_"+subject+"+tlrc"
        ijkmaster = automask
        ijkoutname = basedir+"groupstats/ijk_coords_"+subject
        print "arguments    = --automask "+automask+" --ijkmaster "+ijkmaster+" --ijkoutputname "+ijkoutname+" \nqueue \n"

    def undumpargsOLD(self):
        ##arg1 == steadystate dir, e.g., '/mnt/tier2/urihas/Andric/steadystate/'
        ##arg2 == Condition, e.g., '2'
        ##arg3 == tree number, e.g., '4'
        inputf = self.options.arg1+self.options.subject+"/corrTRIM_BLUR/cleanTS.Cond"+self.options.arg2+"."+self.options.subject+".noijk_dump.bin.corr.thresh.tree"+self.options.arg3
        ijkf = self.options.arg1+self.options.subject+"/ijk_coords_"+self.options.subject
        ijkmaster = self.options.arg1+self.options.subject+"/blur.1."+self.options.subject+".steadystate.TRIM+orig"
        outname = self.options.arg1+self.options.subject+"/corrTRIM_BLUR/"+self.options.subject+"."+self.options.arg2+".tree"+self.options.arg3+".ijk"
        print "arguments    = --inputfile "+inputf+" --ijkfile "+ijkf+" --master "+ijkmaster+" --outputname "+outname+" \nqueue \n"

    def undumpargs(self,subject,arg1,arg2):
        """
        arg1 == the condition number
        arg2 == datum type. either short or float
        OR
        arg2 == tree number
        Change in the filename if tree number
        """
        basedir = "/mnt/tier2/urihas/Andric/steadystate/"
        inputf = basedir+subject+"/corrTRIM_BLUR/"+subject+"."+`arg1`+".node_roles"
        ijkfile = basedir+subject+"/masking/ijk_coords_graymattermask_"+subject
        master = basedir+subject+"/blur.1."+subject+".steadystate.TRIM+orig"
        outname = basedir+subject+"/corrTRIM_BLUR/"+subject+"."+`arg1`+".node_roles"
        print "arguments    = --inputfile "+inputf+" --ijkfile "+ijkfile+" --datatype "+arg2+" --master "+master+" --outputname "+outname+" \nqueue \n"

    def filter(self,subject,arg1,arg2):
        ##arg1 == Condition, e.g., '2'
        ##arg2 == tree number, e.g., '4'
        print "arguments    = 13.filter_comm.R "+subject+" "+`arg1`+" "+`arg2`+" \nqueue \n"

    def undump14(self,subject,arg1,arg2,arg3):
        ##arg1 == Condition, e.g., '2'
        ##arg2 == tree number, e.g., '4'
        ##arg3 == filter pass, e.g., '1'
        print "arguments    = "+subject+" "+`arg1`+" "+`arg2`+" "+`arg3`+" \nqueue \n"

    def degree(self,subject,arg1,arg2):
        """
        arg1 == nvox
        arg2 == condition
        """
        print "arguments    = 17.degree.R "+subject+" "+`arg1`+" "+`arg2`+" \nqueue \n"

    def vol2surfargs(self,ss,specfile,surfA,surfB,mapfunc,gridparent,outname):
        print "arguments    = --subject "+ss+" --suma_dir /mnt/tier2/urihas/external1TB/UH-CPLX/fssubjects/"+ss+"/SUMA/ --spec "+specfile+" --surfA "+surfA+" --surfB "+surfB+" --map_function "+mapfunc+" --surfvol /mnt/tier2/urihas/sam.steadystate/"+ss+"/"+ss+".SurfVol_Alnd_Exp+orig. --grid_parent /mnt/tier2/urihas/Andric/steadystate/"+ss+"/corrTRIM_BLUR/"+gridparent+" --outputname /mnt/tier2/urihas/Andric/steadystate/"+ss+"/surfacedata/"+outname+" \nqueue \n"

    def friedmanargs(self,start,end):
        print "arguments    = 19.friedman.R "+`start`+" "+`end`+" \nqueue \n"

    def voxel_id_args(self,subject,arg1):
        print "arguments   = --number_voxels "+`arg1`+" --subject "+subject+" \nqueue \n"

    def bintomatrix_args(self,subject,arg1,arg2):
        print "arguments   = 26.bintomatrix.R "+subject+" "+arg1+" "+`arg2`+" \nqueue \n"

    def maskmakerargs(self,subject):
        automask = os.environ["state"]+"/"+subject+"/automask_d2_"+subject+"+orig"
        location = os.environ["state"]+"/"+subject+"/masking/"
        print "arguments   = --identity "+subject+" --automask "+automask+" --makeautobox n --location "+location+" \nqueue \n"

    def partcoefargs(self,subject,arg1,arg2):
        """
        arg1 == condition
        arg2 == tree number
        """
        print "arguments   = 16.partcoef.R "+subject+" "+`arg1`+" "+`arg2`+" \nqueue \n"

    def module_degreeargs(self,subject,arg1,arg2):
        """
        arg1 == condition
        arg2 == tree number
        """
        print "arguments   = 17.module_degree.R "+subject+" "+`arg1`+" "+`arg2`+" \nqueue \n"

    def getdatafrombin_args(self,subject,arg1,arg2):
        """
        arg1 == nvoxels
        arg2 == condition
        """
        print "arguments   = --subject "+subject+" --number_voxels "+`arg1`+" --condition "+`arg2`+" \nqueue \n"

    def noderoles_args(self,subject,arg1):
        """
        arg1 == condition
        """
        print "arguments   = --subject "+subject+" --condition "+`arg1`+" \nqueue \n"
    

    def tester(self):
        print "this is a test"


makeargs = MakeArgs()

