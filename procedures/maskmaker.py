#!/usr/bin/python

"""
Here is a sample command line for using this program:

[andric@cosmo mask]$ MaskMaker.py --identity hel1 --volume /gpfs/pads/projects/normal_language/HEL/hel1/masking/volume.hel1+orig. --automask /gpfs/pads/projects/normal_language/HEL/hel1/masking/automask_d1_hel1+orig. --makeautobox n --location /gpfs/pads/projects/normal_language/HEL/hel1/masking/

Second sample command line:
[michaeljames.andric@mat-dt410-uhs1 procedures]$ ./maskmaker.py --identity ANGO --volume /mnt/tier2/urihas/Andric/steadystate/ANGO/ANGOavg_Alnd+orig. --automask /mnt/tier2/urihas/Andric/steadystate/ANGO/automask_d2_ANGO+orig. --makeautobox y --location /mnt/tier2/urihas/Andric/steadystate/ANGO/masking/ 2>&1 | tee -a maskmaker.log

"""

import os
import sys
import commands
import time
import shutil
from optparse import OptionParser

class MaskOps:

    def get_opts(self):
        desc="""
        This is a program to make white matter and ventricle masks to then regress out some sources of nuisance noise. It uses AFNI functions, as well as FSL.  You will need an environment variable 'FSLDIR' pointing to the FSL directory. Note: Make sure to include '+orig' for all input AFNI data types specified here.
        """
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 28.April.2010")
        self.parser.add_option("--identity", dest="id",
            help="subject and/or run identifier")
        self.parser.add_option("--volume", dest="vol",
            help="this is your volume data")
        self.parser.add_option("--automask", dest="amask",
            help="Specify the name of the automask")
        self.parser.add_option("--makeautobox", dest="doautobox",
            help="Do you want to use 3dAutobox to crop the volume image? Answer 'y' for yes and 'n' for no")
        self.parser.add_option("--location", dest="loc",
            help="Specify the working directory. this option is for the benefit of swift functionality.")
        
        (self.options, args) = self.parser.parse_args()
        if len(args) !=0:
            self.parser.error("your arguments == NO BUENO! maybe you put in a flag without giving the argument? maybe you're just messing with me??")
    
        
    def Autobox(self):
    	"""
    	To not include the whole image - surrounding black space, etc.
    	We use this to clip a box around the volume
    	"""
        print "Cropping volume to box fit around the volume.\n"
        print "<<<<<<<<<<<<<<<<<<<<<< 3dAutobox >>>>>>>>>>>>>>>>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dAutobox -noclust -prefix "+self.options.loc+"/volume.box."+self.options.id+" "+self.options.vol)

    def get_volume(self):
        """
        Have to make sure the correct volume is in the working directory
        """
        if not os.path.exists(self.options.loc+"/"+self.options.id+".SurfVol_Alnd_Exp+orig.BRIK"):
            parts = ["HEAD","BRIK"]
            for HB in parts:
                shutil.copy2("/mnt/tier2/urihas/sam.steadystate/"+self.options.id+"/"+self.options.id+".SurfVol_Alnd_Exp+orig."+HB,self.options.loc)
        """
        Convert AFNI to NIFTI
        """
        os.chdir(self.options.loc)
        print "Now working in: "+os.getcwd()
        print os.system("3dAFNItoNIFTI "+self.options.id+".SurfVol_Alnd_Exp+orig")

    def bet_brain(self):
        os.chdir(self.options.loc)
        print "Now working in: "+os.getcwd()
        """
        Use FSL's bet to extract brain from *SurfVol_Alnd_Exp+orig
        """
        print os.system("bet "+self.options.loc+"/"+self.options.id+".SurfVol_Alnd_Exp "+self.options.loc+"/"+self.options.id+".SurfVol_Alnd_Exp_brain -R -f 0.5 -g 0")
                
    def CalcMaskedVol(self):
        os.chdir(self.options.loc)
        print "Now working in: "+os.getcwd()
        print "Get masked data from the volume for ventricles and white matter.\n"
        auto_mask = self.options.amask
        """
        Use FSL program 'fast' to segment the volume
        """
        print "<<<<<<<< running 'fast' to get segmentation >>>>>>>>>>>>> "+time.ctime()
        print os.system("fast -t 1 -n 4 -H 0.4 -I 4 -l 20.0 -g -o "+self.options.id+".SurfVol_Alnd_Exp_fast_out "+self.options.id+".SurfVol_Alnd_Exp_brain")
        """
        Use FSL program 'first' to segment the subcortical.
        'first' is run NOT run on the output from 'bet' (but 'fast' is run on that brain).
        For some reason, 'first' needs the original T1 - not the extracted.
        """
        print "<<<<<<<<<<<<<< runing 'first' to segment the subcortical >>>>>>>>>>>"
        print os.system("run_first_all -i "+self.options.id+".SurfVol_Alnd_Exp.nii -o "+self.options.id+".SurfVol_Alnd_Exp_first_out")
        """
        Get the gray matter mask by combining segmentations from cortex and subcortical
        """
        print "<<<<<<<<<<<< now get the mask >>>>>>>>>>>>>"
        graymatter = self.options.id+"_graymattermask"
        print os.system("3dcalc -a "+self.options.id+".SurfVol_Alnd_Exp_first_out_all_fast_firstseg.nii.gz -b "+self.options.id+".SurfVol_Alnd_Exp_fast_out_seg_1.nii.gz -c "+self.options.id+".SurfVol_Alnd_Exp_fast_out_seg_2.nii.gz -expr 'step(a+b+c)' -prefix "+graymatter)
        """
        Now resample mask into functional resolution
        """
        print os.system("3dresample -master "+auto_mask+" -inset "+graymatter+"+orig -prefix "+graymatter+"_resampled")
        
    def Clipper(self):
        """
        This is a legacy function.
        I haven't used it in 2+ years.
        There may be bugs.
        """
        print "Now get quartile clips\n"
        auto_mask = self.options.amask
        vent_med1 = os.system("3dmaskave -median -mask "+self.options.loc+"/volume.VENT."+self.options.id+"+orig "+self.options.loc+"/volume.box."+self.options.id+"+orig | awk '{print $1}'").split('\n')[2]
        print "vent_med1: "+vent_med1
        vent_med2 = os.system("3dmaskave -median -mask "+self.options.loc+"/volume.VENT."+self.options.id+"+orig -drange 0 "+vent_med1+" "+self.options.loc+"/volume.box."+self.options.id+"+orig | awk '{print $1}'").split('\n')[2]
        print "vent_med2: "+vent_med2
        print "now running: 3dcalc -a "+self.options.loc+"/volume.box."+self.options.id+"+orig -b "+self.options.loc+"/volume.VENT."+self.options.id+"+orig. -expr 'step(a-"+vent_med2+")*step(b)' -prefix "+self.options.loc+"/mask.VENTclip."+self.options.id+"+orig"
        print os.system("3dcalc -a "+self.options.loc+"/volume.box."+self.options.id+"+orig -b "+self.options.loc+"/volume.VENT."+self.options.id+"+orig. -expr 'step(a-"+vent_med2+")*step(b)' -prefix "+self.options.loc+"/mask.VENTclip."+self.options.id+"+orig")
        print os.system("3dfractionize -template "+auto_mask+" -input "+self.options.loc+"/mask.VENTclip."+self.options.id+"+orig -prefix "+self.options.loc+"/mask.VENTclip.frac."+self.options.id+"+orig -vote -clip 0.5")        
        wm_med1 = commands.getoutput("3dmaskave -median -mask "+self.options.loc+"/volume.WM."+self.options.id+"+orig "+self.options.loc+"/volume.box."+self.options.id+"+orig | awk '{print $1}'").split('\n')[2]
        print "wm_med1: "+wm_med1
        wm_med2 = commands.getoutput("3dmaskave -median -mask "+self.options.loc+"/volume.WM."+self.options.id+"+orig -drange "+wm_med1+" 100000 "+self.options.loc+"/volume.box."+self.options.id+"+orig | awk '{print $1}'").split('\n')[2]
        print "wm_med2: "+wm_med2
        print "now running: 3dcalc -a "+self.options.loc+"/volume.box."+self.options.id+"+orig -b "+self.options.loc+"/volume.WM."+self.options.id+"+orig. -expr 'step("+wm_med2+"-a)*step(b)' -prefix "+self.options.loc+"/mask.WMclip."+self.options.id+"+orig"
        print os.system("3dcalc -a "+self.options.loc+"/volume.box."+self.options.id+"+orig -b "+self.options.loc+"/volume.WM."+self.options.id+"+orig. -expr 'step("+wm_med2+"-a)*step(b)' -prefix "+self.options.loc+"/mask.WMclip."+self.options.id+"+orig")
        print os.system("3dfractionize -template "+auto_mask+" -input "+self.options.loc+"/mask.WMclip."+self.options.id+"+orig -prefix "+self.options.loc+"/mask.WMclip.frac."+self.options.id+"+orig -vote -clip 0.9")


def main():
    mm = MaskOps()
    mm.get_opts()
    if mm.options.doautobox == "y" or mm.options.doautobox == "yes":
        mm.Autobox()
        vol = mm.options.loc+"/volume.box."+mm.options.id+"+orig"
    #elif mm.options.doautobox == "n" or mm.options.doautobox == None:
    #    vol = mm.options.vol
    mm.get_volume()
    mm.bet_brain()
    mm.CalcMaskedVol()

if __name__ == "__main__":
    main()
