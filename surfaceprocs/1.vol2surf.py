#!/usr/bin/python

#used with condor
import os
import shutil
from optparse import OptionParser

class SurfProc:

    def get_opts(self):
        desc = """simple program for doing 3dmaskdump"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Oct.2012")
        self.parser.add_option("--suma_dir", dest="sumadir",
                               help="specify the SUMA directory that holds the spec and surf files")
        self.parser.add_option("--spec_file", dest="spec",
                               help="specify the spec file")
        self.parser.add_option("--surfA", dest="surfA",
                               help="typically the smoothwm surface")
        self.parser.add_option("--surfB", dest="surfB",
                               help="typically the pial surface")
        self.parser.add_option("--map_function", dest="mapfunc",
                               help="the mapping function")
        self.parser.add_option("--surfvol", dest="surfvol",
                               help="the surface volume")
        self.parser.add_option("--grid_parent", dest="gridparent",
                               help="the grid parent BRIK")
        self.parser.add_option("--outputname", dest="outname",
                               help="output name")

        (self.options, args) = self.parser.parse_args()

    def cp_files(self):
        shutil.copy2(self.options.sumadir+self.options.spec, os.getcwd())
        shutil.copy2(self.options.sumadir+self.options.surfA, os.getcwd())
        shutil.copy2(self.options.sumadir+self.options.surfB, os.getcwd())

    def rm_files(self):
        os.remove(os.getcwd()+"/"+self.options.spec)
        os.remove(os.getcwd()+"/"+self.options.surfA)
        os.remove(os.getcwd()+"/"+self.options.surfB)

    def Vol2Surf(self):
        print os.system("3dVol2Surf -spec "+self.options.spec+" -surf_A "+self.options.surfA+" -surf_B "+self.options.surfB+" \
                                    -map_func "+self.options.mapfunc+" -f_index voxels -oob_index -1 -oob_value 0 -no_headers \
                                    -outcols_NSD_format -sv "+self.options.surfvol+" -grid_parent "+self.options.gridparent+" \
                                    -out_1D "+self.options.outname)

    def Vol2Surf_ext(self):
        print os.system("3dVol2Surf -spec "+self.options.spec+" -surf_A "+self.options.surfA+" -surf_B "+self.options.surfB+" \
                                    -map_func "+self.options.mapfunc+" -f_steps 10 -f_index voxels -f_p1_fr -0.1 -f_pn_fr 0.1 \
                                    -oob_index -1 -oob_value 0 -no_headers \
                                    -outcols_NSD_format -sv "+self.options.surfvol+" -grid_parent "+self.options.gridparent+" \
                                    -out_1D "+self.options.outname)


SP = SurfProc()
SP.get_opts()
SP.cp_files()
SP.Vol2Surf_ext()
SP.rm_files()
