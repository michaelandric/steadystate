#!/usr/bin/python

import os
from optparse import OptionParser

class AFNIproc_undump:

    def get_opts(self):
        desc = """rogram for pasting ijk coordinates to input text files and doing 3dUndump"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Sep.2012")
        self.parser.add_option("--input_prefix", dest="input",
                               help="input prefix")
        self.parser.add_option("--ijkfile", dest="ijk",
                               help="the ijk coordinates text file")
        self.parser.add_option("--master", dest="mstr",
                               help="file with desired functional parameters")
        self.parser.add_option("--output_prefix", dest="outname",
                               help="output name prefix")

        (self.options, args) = self.parser.parse_args()


    def paste_ijk(self):
        inputf = open(self.options.input+".sorted.txt","r")
        voxelnum = []
        stat = []
        pval = []
        inversepval = []
        for line in inputf:
            a, b, c, d = line.split()
            stat.append(b)
            pval.append(c)
            inversepval.append(d)

        ijkcoords = open(self.options.ijk,"r")
        xcoord = []
        ycoord = []
        zcoord = []
        for line in ijkcoords:
            x, y, z = line.split()
            xcoord.append(x)
            ycoord.append(y)
            zcoord.append(z)

        statlist = ""
        for i in range(len(stat)):
            statlist += xcoord[i]+" "+ycoord[i]+" "+zcoord[i]+" "+stat[i]+"\n"

        pvallist = ""
        for i in range(len(pval)):
            pvallist += xcoord[i]+" "+ycoord[i]+" "+zcoord[i]+" "+pval[i]+"\n"

        inversepvallist = ""
        for i in range(len(inversepval)):
            inversepvallist += xcoord[i]+" "+ycoord[i]+" "+zcoord[i]+" "+inversepval[i]+"\n"

        outstat = open(self.options.input+"_stat.ijk.txt","w")
        outstat.write(statlist)
        outstat.close()

        outpval = open(self.options.input+"_pval.ijk.txt","w")
        outpval.write(pvallist)
        outpval.close()

        outinvpval = open(self.options.input+"_invpval.ijk.txt","w")
        outinvpval.write(inversepvallist)
        outinvpval.close()


    def paste_ijkMESS(self):
        inputf = open(self.options.input+".sorted.txt","r")
        list1 = ['la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk', 'll', 'lm', 'ln', 'lo']
        ncols = 15
        list_sets = [[] for x in xrange(ncols)]
        for i in range(len(d)):
            d[i].append(i)

        elements = a, b, c, d, e, f, g, h, i, j, k, l, m, n, o

        for line in inputf:
            elements = line.split()
            for i in range(len(elements)):
                list_sets[i].append(elements[i])


        ijkcoords = open(self.options.ijk,"r")
        xcoord = []
        ycoord = []
        zcoord = []
        for line in ijkcoords:
            x, y, z = line.split()
            xcoord.append(x)
            ycoord.append(y)
            zcoord.append(z)


    def paste_ijk2(self,sub,i):
        os.chdir(os.environ["state"]+"/groupstats/")
        os.system("awk '{print $"+`i+1`+"}' friedmanposthoc_complete.sorted.txt > tmp.txt")
        os.system("paste -d ' ' "+self.options.ijk+" tmp.txt > "+self.options.input+"."+sub+".sorted.ijk.txt")
        os.system("rm -rf tmp.txt")

    def paste_ijkINV(self):
        os.chdir(os.environ["state"]+"/groupstats/")
        compares = ["c1v2","c1v3","c1v4","c2v3","c2v4","c3v4"]
        for cc in compares:
            inputf = open("friedmanposthoc_complete."+cc+".sorted.ijk.txt","r")
            xcoord = []
            ycoord = []
            zcoord = []
            val = []
            for line in inputf:
                a, b, c, d = line.split()
                xcoord.append(a)
                ycoord.append(b)
                zcoord.append(c)
                val.append(d)

            floatval = map(float,val)
            #print type(floatval)
            #print type(floatval[0])
            newlist = []
            for nn in floatval:
                if nn > 0:
                    newlist.append('%.4f' % (1-nn))
                else:
                    newlist.append(`nn`)

            outf = ""
            for i in range(len(newlist)):
                outf += xcoord[i]+" "+ycoord[i]+" "+zcoord[i]+" "+newlist[i]+"\n"

            outname = open("friedmanposthoc_complete.inv_"+cc+".sorted.ijk.txt","w")
            outname.write(outf)
            outname.close()




    def undump(self):
        subbriks = ["stat","pval","invpval"]
        for b in subbriks:
            print os.system("3dUndump -prefix "+self.options.outname+"_"+b+".ijk -ijk -datum float -master "+self.options.mstr+" "+self.options.input+"_"+b+".ijk.txt")

    def undump2(self,sub):
        print os.system("3dUndump -prefix "+self.options.outname+"."+sub+" -ijk -datum float -master "+self.options.mstr+" "+self.options.input+"."+sub+".sorted.ijk.txt")

    def undumpINV(self,sub):
        print os.system("3dUndump -prefix "+self.options.outname+"_"+sub+" -ijk -datum float -master "+self.options.mstr+" "+self.options.input+".inv_"+sub+".sorted.ijk.txt")

    def bucket(self):
        print os.system("3dbucket -prefix "+self.options.outname+"_bucket.ijk "+self.options.outname+"_stat.ijk+tlrc "+self.options.outname+"_pval.ijk+tlrc "+self.options.outname+"_invpval.ijk+tlrc")

    def bucket2(self):
        print "this"


subbriks = ["voxel","c1v2", "c1v3", "c1v4", "c2v3", "c2v4", "c3v4", "median1", "median2", "median3", "median4", "sum1", "sum2", "sum3", "sum4"]

UD = AFNIproc_undump()
UD.get_opts()
#for i in range(len(subbriks)):
    #UD.paste_ijk2(subbriks[i],i)
    #UD.undump2(subbriks[i])
#UD.paste_ijkINV()
compares = ["c1v2","c1v3","c1v4","c2v3","c2v4","c3v4"]
for cc in range(len(compares)):
    UD.undumpINV(compares[cc])
                   
#UD.bucket()
