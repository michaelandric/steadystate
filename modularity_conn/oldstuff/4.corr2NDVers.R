library(Rmpi)
library(snow)
library(bct)

args <- commandArgs(trailingOnly=TRUE)
subj <- args[1]
print(subj)
#nvox <- 8
nvox <- as.numeric(args[2])
ntp <- as.numeric(args[3])
cluster <- makeMPIcluster(16)

## assumes voxels are 0-ordered
correlateall <- function(i,ss,nvox,ntp)
{
    library(bct)
    basedir <- Sys.getenv("state")
    tsHEAD <- paste(basedir,"/",ss,"/reg.",i,".",ss,".steadystate+orig.HEAD",sep="")
    tsBRIK <- paste(basedir,"/",ss,"/reg.",i,".",ss,".steadystate+orig.BRIK",sep="")
    motionfile <- paste(basedir,"/",ss,"/motion.",i,".",ss,".steadystate",sep="")
    maskHEAD <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.HEAD",sep="")
    maskBRIK <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.BRIK",sep="")
    bucketfile <- paste(basedir,"/",ss,"/dirtyTS.masked.Cond",i,".",ss,sep="")
    errts <- paste(basedir,"/",ss,"/cleanTS.masked.Cond",i,".",ss,sep="")

    ## clean the time series, regressing against motion estimates
    afnicmd1 <- paste("3dDeconvolve -input ",tsBRIK," -polort 1 -num_stimts 6 -stim_file 1 ",motionfile,"'[1]' -stim_file 2 ",motionfile,"'[2]' -stim_file 3 ",motionfile,"'[3]' -stim_file 4 ",motionfile,"'[4]' -stim_file 5 ",motionfile,"'[5]' -stim_file 6 ",motionfile,"'[6]' -rout -bucket ",bucketfile," -errts ",errts,sep="")
    print(afnicmd1)
    system(afnicmd1)

    ## now dump the clean time series to text file
    tstxt <- paste(basedir,"/",ss,"/cleanTS.Cond",i,".",ss,".steadystate.noijk_dump",sep="")
    afnicmd2 <- paste("3dmaskdump -mask ",maskBRIK," -noijk ",errts,"+orig.BRIK > ",tstxt,sep="")
    print(afnicmd2)
    system(afnicmd2)

    ## now correlate voxel by voxel matrix
    fcorr(tstxt,nvox,ntp)
}


parSapply(cluster,1:4,correlateall,subj,nvox,ntp)
stopCluster(cluster)
