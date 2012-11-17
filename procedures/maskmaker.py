#!/usr/bin/python

"""
Here is a sample command line for using this program:

[andric@cosmo mask]$ MaskMaker.py --identity hel1 --volume /gpfs/pads/projects/normal_language/HEL/hel1/masking/volume.hel1+orig. --automask /gpfs/pads/projects/normal_language/HEL/hel1/masking/automask_d1_hel1+orig. --makeautobox n --location /gpfs/pads/projects/normal_language/HEL/hel1/masking/

"""

import os
import sys
import commands
import time
from optparse import OptionParser

class MaskOps:

    def get_opts(self):
        desc="""
        This is a program to make white matter and ventricle masks to then regress out some sources of nuisance noise.  
        It uses AFNI functions, as well as FSL.  You will need an environment variable 'FSLDIR' pointing to the FSL directory. 
        Note: Make sure to include '+orig' for all input AFNI data types specified here. 
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
    	We clip a box around the volume
    	"""
        print "Cropping volume to box fit around the volume.\n"
        print "<<<<<<<<<<<<<<<<<<<<<< 3dAutobox >>>>>>>>>>>>>>>>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dAutobox -noclust -prefix "+self.options.loc+"/volume.box."+self.options.id+" "+self.options.vol)
        
    def TLRC_algn(self):
    	"""
    	Here we get rid of the skull and align the brain to talairach coords
    	"""
        print "Skull strip and get a tal align coordinate vector\n"
        print "<<<<<<<<<<<<<<<<<<<<<< 3dSkullStrip >>>>>>>>>>>>>>>>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dSkullStrip -input "+self.options.vol+" -prefix "+self.options.loc+"/volume.sklstrp."+self.options.id+" -orig_vol") ## do Skull strip
        print "<<<<<<<<<<<<<<<<<<<<<< 3dZeropad >>>>>>>>>>>>>>>>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dZeropad -I 10 -S 10 -A 10 -P 10 -L 10 -R 10 -prefix "+self.options.loc+"/volume.padded.sklstrp."+self.options.id+" "+self.options.loc+"/volume.sklstrp."+self.options.id+"+orig") ## create extra padding in the volume space
        print "<<<<<<<<<<<<<<<<<<<<<< 3dresample >>>>>>>>>>>>>>>>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dresample -inset "+os.environ["AFNI_PLUGINPATH"]+"/TT_N27+tlrc -master "+self.options.loc+"/volume.padded.sklstrp."+self.options.id+"+orig -prefix "+self.options.loc+"/template.resampled."+self.options.id+"+orig") ## resample to tal
        print "<<<<<<<<<<<<<<<<<<<<<< 3dWarpDrive >>>>>>>>>>>>>>>>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dWarpDrive -affine_general -cubic -input "+self.options.loc+"/volume.padded.sklstrp."+self.options.id+"+orig -prefix "+self.options.loc+"/volume.tal.padded.sklstrp."+self.options.id+" -base "+self.options.loc+"/template.resampled."+self.options.id+"+orig -1Dmatrix_save "+self.options.loc+"/volume.tal."+self.options.id+".1D") ## using this to get the tal transform matrix 'volume.tal.*.1D'
        
    def CalcMaskedVol(self,vol):
        print "Get masked data from the volume for ventricles and white matter.\n"
        auto_mask = self.options.amask
        frac_mask = self.options.loc+"/automask_frac_"+self.options.id+"+orig"
        print "<<<<<<<<<<<<<<<<<<<<<< 3dfractionize >>>>>>>>>>>>>>>>>>>>>>>>>>> \n"+time.ctime()
        os.system("3dfractionize -template "+self.options.loc+"/volume.box."+self.options.id+"+orig -input "+auto_mask+" -preserve -clip 0.2 -prefix "+frac_mask)
        """
        This is where we make sure FSL is sourced
        """
        print "Sourcing FSLDIR: "+os.environ["FSLDIR"]
        print commands.getoutput("source "+os.environ["FSLDIR"]+"/etc/fslconf/fsl.csh") ## source FSL
        print "<<<<<<<< 3dcalc to get masked volume from the fractionized and boxed volume >>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dcalc -a "+frac_mask+" -b "+self.options.loc+"/volume.box."+self.options.id+"+orig -expr 'step(a)*b' -prefix "+self.options.loc+"/volume.masked."+self.options.id+"+orig") ## mask sample volume
        """
        This NIFTI conversion is needed because that's the format fsl uses
        """
        print "<<<<<<<< 3dAFNItoNIFTI to get nii volume >>>>>>>>>>>>>\n"+time.ctime()
        os.system("3dAFNItoNIFTI -prefix "+self.options.loc+"/volume.masked."+self.options.id+".nii "+self.options.loc+"/volume.masked."+self.options.id+"+orig") ## convert to nii
        """
        now use FSL program 'fast' to segment the volume
        """
        print "<<<<<<<< running 'fast' to get segmentation >>>>>>>>>>>>> "+time.ctime()
        print os.system("fast -o "+self.options.loc+"/volume."+self.options.id+" "+self.options.loc+"/volume.masked."+self.options.id+".nii") ## segments volume?
        print "<<<<<<<< 3dcalc to get mask around ventricles from nii segmentation >>>>>>>>>>>>> "+time.ctime()
        os.system("3dcalc -a "+self.options.loc+"/volume."+self.options.id+"_seg.nii.gz -b "+frac_mask+" -expr '100*step(b)*iszero(amongst(a,1,0))' -prefix "+self.options.loc+"/volume.aroundVent.preblur."+self.options.id)  ## mask around the ventricle
        print "<<<<<<<< 3dmerge to blur aroundVent >>>>>>>>>>>>> "+time.ctime()
        """
        Note: This blur is not 'one size fits all', i.e., may have to change 1filter_nzmean value so it doesn't blur over the ventricle completely.
        Start with '-1filter_nzmean 3'
        """
        os.system("3dmerge -1filter_nzmean 2 -prefix "+self.options.loc+"/volume.aroundVent.blur."+self.options.id+" "+self.options.loc+"/volume.aroundVent.preblur."+self.options.id+"+orig") ## blur around the ventricle
        
        print "<<<<<<<< Generating the Ventricles seed 'Vseed' >>>>>>>>>>>>> "+time.ctime()
        """
        This creates seed in areas of ventricle, using talairach coords
        """
        Vseed = "-8 13 19\n8 13 19\n"
        file = open('vent.seed.tal.1D','w')
        file.write(Vseed)
        file.close()
        
        print "<<<<<<<< Warping from talrch using 'Vecwarp'  >>>>>>>>>>>>> "+time.ctime()
        os.system("Vecwarp -matvec "+self.options.loc+"/volume.tal."+self.options.id+".1D -forward -input vent.seed.tal.1D -output "+self.options.loc+"/vent.seed.1D")
        print "<<<<<<<< 3dUndump to get ventricles seed >>>>>>>>>>>>> "+time.ctime()
        os.system("3dUndump -xyz -orient RAI -prefix "+self.options.loc+"/vent.seed."+self.options.id+" -master "+frac_mask+" -srad 8 "+self.options.loc+"/vent.seed.1D")
        print "<<<<<<<< 3dcalc to get inverted vent volume seed  >>>>>>>>>>>>> "+time.ctime()
        os.system("3dcalc -a "+self.options.loc+"/volume.aroundVent.blur."+self.options.id+"+orig -b "+frac_mask+" -c "+self.options.loc+"/vent.seed."+self.options.id+"+orig -expr 'step(b)*iszero(step(a))*(1+100*step(c))' -prefix "+self.options.loc+"/volume.aroundVent.inv."+self.options.id)
        print "<<<<<<<< 3dmerge to cluster around the vent >>>>>>>>>>>>> "+time.ctime()
        os.system("3dmerge -dxyz=1 -1clust_max 2 1 -prefix "+self.options.loc+"/volume.aroundVent.clust."+self.options.id+" "+self.options.loc+"/volume.aroundVent.inv."+self.options.id+"+orig")
        print "<<<<<<<< 3dcalc to get masked volume ventricles >>>>>>>>>>>>> "+time.ctime()
        os.system("3dcalc -datum byte -a "+self.options.loc+"/volume.aroundVent.clust."+self.options.id+"+orig -expr '100*step(a-1)' -prefix "+self.options.loc+"/volume.vent.init."+self.options.id)
        print "<<<<<<<< 3dmerge to get masked volume ventricles blur >>>>>>>>>>>>> "+time.ctime()
        os.system("3dmerge -1filter_nzmean 5 -prefix "+self.options.loc+"/volume.vent.init.blur."+self.options.id+" "+self.options.loc+"/volume.vent.init."+self.options.id+"+orig")
        print "<<<<<<<< 3dcalc to grab masked volume ventricles using the blurred >>>>>>>>>>>>> "+time.ctime()
        os.system("3dcalc -a "+self.options.loc+"/volume.aroundVent.preblur."+self.options.id+"+orig -b "+self.options.loc+"/volume.vent.init.blur."+self.options.id+"+orig -c "+self.options.loc+"/volume.masked."+self.options.id+"+orig -expr 'iszero(a)*iszero(b)*step(c)' -prefix "+self.options.loc+"/volume.aroundVent.init."+self.options.id)
        print "<<<<<<<< 3dmerge to get init volume around ventricles >>>>>>>>>>>>> "+time.ctime()
        os.system("3dmerge -dxyz=1 -1clust_order 2 1 -prefix "+self.options.loc+"/volume.aroundVent.init.clust."+self.options.id+" "+self.options.loc+"/volume.aroundVent.init."+self.options.id+"+orig")
        print "<<<<<<<< 3dcalc to get init preclustered volume around ventricles >>>>>>>>>>>>> "+time.ctime()
        os.system("3dcalc -a "+self.options.loc+"/volume.aroundVent.init.clust."+self.options.id+"+orig -b "+self.options.loc+"/volume.vent.init."+self.options.id+"+orig -c "+self.options.loc+"/volume.aroundVent.preblur."+self.options.id+"+orig -d "+self.options.loc+"/volume.masked."+self.options.id+"+orig -expr 'iszero(c)*iszero(equals(a,1))*(1+100*step(b))*step(d)' -prefix "+self.options.loc+"/volume.vent.init.preclust."+self.options.id)
        print "<<<<<<<< 3dmerge to get initial clustered volume around ventricles >>>>>>>>>>>>> "+time.ctime()
        os.system("3dmerge -dxyz=1 -1clust_max 2 1 -prefix "+self.options.loc+"/volume.vent.init.clust."+self.options.id+" "+self.options.loc+"/volume.vent.init.preclust."+self.options.id+"+orig")
        
        """
        Finally getting the ventricles mask
        """
        print "<<<<<<<< 3dcalc and 3dfractionize to get ventricles mask >>>>>>>>>>>>> "+time.ctime()
        os.system("3dcalc -datum byte -a "+self.options.loc+"/volume.vent.init.clust."+self.options.id+"+orig -expr 'step(a-1)' -prefix "+self.options.loc+"/volume.VENT."+self.options.id)
        
        """
        Finally getting the white matter mask
        """
        print "<<<<<<<< 3dcalc and 3dfractionize to get white matter mask >>>>>>>>>>>>> "+time.ctime()
        os.system("3dcalc -datum byte -a "+self.options.loc+"/volume."+self.options.id+"_seg.nii.gz -expr 'equals(a,3)' -prefix "+self.options.loc+"/volume.WM."+self.options.id)
        
    def Clipper(self):
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


mm = MaskOps()
mm.get_opts()
if mm.options.doautobox == "y" or mm.options.doautobox == "yes":
    mm.Autobox()
    vol = mm.options.loc+"/volume.box."+mm.options.id+"+orig"
elif mm.options.doautobox == "n" or mm.options.doautobox == None:
    vol = mm.options.vol
mm.TLRC_algn()
mm.CalcMaskedVol(vol)
mm.Clipper()
