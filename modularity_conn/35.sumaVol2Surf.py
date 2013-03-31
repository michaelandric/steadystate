#!/usr/bin/python

import os
from optparse import OptionParser
from subprocess import call

class Vol2Surf:

    def get_opts(self):
        desc = """
        This is for doing 3dVol2Surf.
        """
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Morch.2013")
        self.parser.add_option("--subject", dest="SS",
	    			help="specify subject identifier")
    	self.parser.add_option("--hemi", dest="H",
    				help="Hemisphere id")
        self.parser.add_option("--condition", dest="cc",
	    			help="Give the condition identifier, e.g., '1'")

       	(self.options, args) = self.parser.parse_args()


    def volsurfcmd(self):
        """
        This is projecting to the individual surfaces. 
        The modules* grid parent files kinda look like shit when warped into TLRC space.
        """
        os.chdir(os.environ["state"]+"/"+self.options.SS+"/surfacedata/")
        print os.getcwd()
        PARENT = os.environ["state"]+"/"+self.options.SS+"/corrTRIM_BLUR/modules_"+self.options.SS+"_Cond"+self.options.cc+"+orig"
        SV = self.options.SS+"_SurfVol_Alnd_Exp+orig"
        print self.options.SS+" -- Cond"+self.options.cc+" -- "+self.options.H
        print call("3dVol2Surf -spec ./"+self.options.SS+"_"+self.options.H+".spec -surf_A ./"+self.options.H+".smoothwm.asc -surf_B ./"+self.options.H+".pial.asc \
                    -sv "+SV+" -grid_parent "+PARENT+" -map_func max -f_steps 10 -f_index voxels -f_p1_fr -0.3 -f_pn_fr 0.3 \
                    -outcols_NSD_format -oob_index -1 -oob_value 0.0 -out_1D modules_"+self.options.SS+"_"+self.options.H+"_Cond"+self.options.cc+".1D", shell=True)

def main():
    VS = Vol2Surf()
    VS.get_opts()
    VS.volsurfcmd()

if __name__ == "__main__":
    main()
