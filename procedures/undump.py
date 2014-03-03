#!/usr/bin/python

import os
from subprocess import call
from optparse import OptionParser
from glob import glob

class Undump:

    def get_opts(self):
        desc = """
        program for getting data from txt and putting to afni format
        """
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Dec.2012")
        self.parser.add_option("--input", dest="input",
                               help="specify the input")
        self.parser.add_option("--ijkfile", dest="ijk",
                               help="the ijk coordinates file")
        self.parser.add_option("--master", dest= "mstr",
                               help="file with desired functional parameters")
        self.parser.add_option("--datatype", dest="datum",
                               help="Choose data type. 'short' or 'float'")
        self.parser.add_option("--outputname", dest="outname",
                               help="output name")

        (self.options, args) = self.parser.parse_args()

    def get_data(self):
        inputf = open(self.options.input,"r")
        self.list1 = []
        self.list2 = []
        for line in inputf:
            a, b, c = line.split()
            self.list1.append(b)
            self.list2.append(c)

    def undumpAFNI(self):
        ijkcoords = open(self.options.ijk,"r")
        icoord = []
        jcoord = []
        kcoord = []
        for line in ijkcoords:
            i, j, k = line.split()
            icoord.append(i)
            jcoord.append(j)
            kcoord.append(k)

        list1f = ""
        list2f = ""
        for v in range(len(self.list1)):
            list1f += icoord[v]+" "+jcoord[v]+" "+kcoord[v]+" "+self.list1[v]+"\n"
            list2f += icoord[v]+" "+jcoord[v]+" "+kcoord[v]+" "+self.list2[v]+"\n"

        list1out = open("_templist1","w")
        list1out.write(list1f)
        list2out = open("_templist2","w")
        list2out.write(list2f)
        list1out.close()
        list2out.close()

        outname1 = "_temp_noderole"
        outname2 = "_temp_numss"

        call("3dUndump -prefix "+outname1+" -ijk -datum "+self.options.datum+" -master "+self.options.mstr+" _templist1", shell=True)
        call("3dUndump -prefix "+outname2+" -ijk -datum "+self.options.datum+" -master "+self.options.mstr+" _templist2", shell=True)

        """
        now bucket the two AFNI files
        """
        call("3dbucket -prefix "+self.options.outname+" "+outname1+"+tlrc "+outname2+"+tlrc", shell=True)

        """
        remove the _temp* files
        """
        files = glob("_temp*")
        for f in files:
            os.remove(f)
        
        

def main():
    os.chdir(os.environ["state"]+"/groupstats/")
    print os.getcwd()
    UD = Undump()
    UD.get_opts()
    UD.get_data()
    UD.undumpAFNI()

if __name__ == "__main__":
    main()
