#!/usr/bin/python

import os
from optparse import OptionParser

class AFNIsnr:

    def get_opts(self):
        desc = """simple program for doing SNR"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog 10.October.2012")
        self.parser.add_option("--WorkDir", dest="workdir",
                               help="specify the output directory")
        self.parser.add_option("--InputTSprefix", dest="pref",
                               help="specify the input prefix. everything before '+orig'")
#        self.parser.add_option("--SubjectID", dest="subject",
#                               help="specity the subject identifier")
#        self.parser.add_option("--ConditionID", dest="Cond",
#                               help="specify the condition identifier")

        (self.options, args) = self.parser.parse_args()

    def AFNImean(self):
        print os.system("3dTstat -mean -prefix "+self.options.workdir+"/mean."+self.options.pref+" \
                        "+self.options.workdir+"/"+self.options.pref+"+orig.BRIK")

    def AFNIstdev(self):
        print os.system("3dTstat -stdev -prefix "+self.options.workdir+"/stdev."+self.options.pref+" \
                        "+self.options.workdir+"/detrend."+self.options.pref+"+orig.BRIK")

    def AFNIdetrend(self):
        print os.system("3dDetrend -polort 3 -prefix "+self.options.workdir+"/detrend."+self.options.pref+" \
                        "+self.options.workdir+"/"+self.options.pref+"+orig.BRIK")

    def AFNIratio(self):
        print os.system("3dcalc -verbose -a "+self.options.workdir+"/mean."+self.options.pref+"+orig.BRIK \
                        -b "+self.options.workdir+"/stdev."+self.options.pref+"+orig.BRIK \
                        -expr '(a/b)' -prefix "+self.options.workdir+"/snr."+self.options.pref)



SNR = AFNIsnr()
SNR.get_opts()
SNR.AFNImean()
SNR.AFNIdetrend()
SNR.AFNIstdev()
SNR.AFNIratio()

