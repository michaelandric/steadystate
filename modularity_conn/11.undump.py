#!/usr/bin/python

from subprocess import call
from optparse import OptionParser

class AFNIproc_undump:

    def get_opts(self):
        desc = """rogram for pasting ijk coordinates to input text files and doing 3dUndump"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Nov.2012")
        self.parser.add_option("--inputfile", dest="input",
                               help="input text file")
        self.parser.add_option("--ijkfile", dest="ijk",
                               help="the ijk coordinates text file")
        self.parser.add_option("--master", dest="mstr",
                               help="file with desired functional parameters")
        self.parser.add_option("--datatype", dest="datum",
                               help="Choose data type. 'short' or 'float'")
        self.parser.add_option("--outputname", dest="outname",
                               help="output name")

        (self.options, args) = self.parser.parse_args()

    def get_data(self):
        """
        Adding '1' to every community to not have '0' as a community label.
        """
        inputf = open(self.options.input,'r')
        voxelnum = []
        community = []
        for line in inputf:
            a, b = line.split()
            voxelnum.append(a)
            community.append(b)

        communityint = map(int, community)
        newcomm = []
        for i in range(len(communityint)):
            newcomm.append(communityint[i]+1)

        justcomm = ""
        for i in range(len(newcomm)):
            justcomm += `newcomm[i]`+"\n"

        outname = self.options.input+".justcomm"
        outf = open(outname,"w")
        outf.write(justcomm)
        outf.close()

    def paste_ijk(self):
    	"""
    	This function works from the naming convention given in 'get_data' function. 
    	Use 'paste_ijk2' if giving the full input filename.
    	"""
        print call("paste -d ' ' "+self.options.ijk+" "+self.options.input+".justcomm > "+self.options.input+".ijk.txt",shell=True)

    def paste_ijk2(self):
    	"""
    	If specifying the full input name, can use this paste function.
    	"""
        print call("paste -d ' ' "+self.options.ijk+" "+self.options.input+" > "+self.options.input+".ijk.txt",shell=True)

    def undump(self):
        print call("3dUndump -prefix "+self.options.outname+" -ijk -datum "+self.options.datum+" -master "+self.options.mstr+" "+self.options.input+".ijk.txt", shell=True)


def main():
    UD = AFNIproc_undump()
    UD.get_opts()
    UD.get_data()
    UD.paste_ijk()
    UD.undump()

if __name__ == "__main__":
    main()
