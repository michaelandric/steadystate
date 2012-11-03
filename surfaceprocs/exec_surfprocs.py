#!/usr/bin/python

import surfprocs
from optparse import OptionParser


subjects = ["ANGO","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"]
conditions = range(1,5)
## this is the dictionary that maps nvox to subject
dictionary = {'EZCR': '31902', 'FLTM': '32555', 'MRZM': '23081', 'MRMC': '29045', 'ANMS': '25009', 'MRAG': '26830', 'ANGO': '22170', 'PIGL': '26253', 'CLFR': '24883', 'CRFO': '28632', 'EEPA': '30432', 'TRCO': '28705', 'MRMK': '26331', 'SNNW': '27839', 'BARS': '28340', 'LDMW': '27133', 'LRVN': '26562', 'MRVV': '24476', 'DNLN': '25884', 'MYTP': '26202', 'MNGO': '28266'}
## this dictionary gives the highest level (at .5 corr threshold)
dictionary2 = {'MYTP':(4,3,3,3), 'TRCO':(4,4,4,3), 'CLFR':(4,3,4,3), 'PIGL':(4,4,4,4), 'SNNW':(3,4,3,3)}



def get_opts():
    parser = OptionParser(description=desc, version="%prog Oct.2012")
    parser.add_option("--suma_dir", dest="sumadir",
                      help="specify the SUMA directory that holds the spec and surf files")
    parser.add_option("--spec_file", dest="spec",
                      help="specify the spec file")
    parser.add_option("--surfA", dest="surfA",
                      help="typically the smoothwm surface")
    parser.add_option("--surfB", dest="surfB",
                      help="typically the pial surface")
    parser.add_option("--map_function", dest="mapfunc",
                      help="the mapping function")
    parser.add_option("--surfvol", dest="surfvol",
                      help="the surface volume")
    parser.add_option("--grid_parent", dest="gridparent",
                      help="the grid parent BRIK")
    parser.add_option("--outputname", dest="outname",
                      help="output name")

    (options, args) = parser.parse_args()
                                                                                


for ss in subjects:
    get_opts()
    surfprocs.Vol2Surf(options.spec, options.surfA, options.surfB, options.mapfunc, options.surfvol, options.gridparent, options.outname)
