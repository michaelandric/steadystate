#!/usr/bin/python

"""
Get the modularity (community) Q vals and hierarchy
"""

import os
import sys
import subprocess

subject = sys.argv[1]
links_density = sys.argv[2]
cc = sys.argv[3]   # condition

fname = os.environ["state"]+"/links_files"+links_density+"/"+subject+"."+cc+"."+links_density+"_r0.5_linksthresh_proportion.out.srcdst"

for i in range(1,101):
    p = subprocess.Popen(["community", fname, "-l", "-1", "-v"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    pout, pcom = p.communicate()

    foutfile = ""
    for line in pout:
        foutfile += line

    outname = os.environ["state"]+"/"+subject+"/modularity"+links_density+"/iter"+`i`+"."+subject+"."+cc+"."+links_density+"_r0.5_linksthresh_proportion.out.tmptree" 
    fo = open(outname, "w")
    fo.write(pout)
    fo.close()

    Qval = float(pcom.split('\n')[len(pcom.split('\n')) - 2])
    Qval_fname = os.environ["state"]+"/"+subject+"/modularity"+links_density+"/iter"+`i`+"."+subject+"."+cc+"."+links_density+"_r0.5_linksthresh_proportion.out.Qval" 
    Qval_file = open(Qval_fname, "w")
    Qval_file.write('%.5f' % Qval+"\n")
    Qval_file.close()
    lvls = (ll for ll in pcom.split('\n') if "level" in ll)
    max_level = max(map(int, (lv.split()[1].split(':')[0] for lv in lvls))) 

    hierarchy = subprocess.Popen(["hierarchy", outname, "-l", `max_level`], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    hierarchy_out, hierarchy_err = hierarchy.communicate()

    houtfile = ""
    for line in hierarchy_out:
        houtfile += line

    houtname = os.environ["state"]+"/"+subject+"/modularity"+links_density+"/iter"+`i`+"."+subject+"."+cc+"."+links_density+"_r0.5_linksthresh_proportion.out.maxlevel_tree"
    ho = open(houtname, "w")
    ho.write(houtfile)
    ho.close()
    os.remove(outname)

