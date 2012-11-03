#!/usr/bin/python

import os

os.chdir(os.environ["state"]+"/groupstats")
print os.getcwd()
#print os.system("3dclust -prefix "+os.environ["state"]+"/groupstats/friedman_out_clusters -noabs -1thresh 11.3 4 300 friedman_out_bucket.ijk+tlrc'[0]' > friedman_out_clusters.1D")
#print os.system("3dmerge -1clust 4 155 -1thresh 11.3 -prefix friedman_out_clusters friedman_out_bucket.ijk+tlrc'[0]'")
#print os.system("3dclust -prefix friedman_out_clustmask -1thresh -dxyz=2 4 155 friedman_out_bucket.ijk+tlrc'[0]'")
print os.system("3dmerge -1dindex 2 -1tindex 2 -2thresh -0.99 0.99 -dxyz=2 1.01 156 /mnt/tier2/urihas/Andric/steadystate/groupstats/friedman_out_bucket.ijk+tlrc.HEAD -prefix friedman_out_clusters")
