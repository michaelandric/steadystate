## this version does not use fcorr function
## does blur TS
library(Rmpi)
library(snow)
library(bct)

args <- commandArgs(trailingOnly=TRUE)
subj <- args[1]
print(subj)
nvox <- as.numeric(args[2])
cluster <- makeMPIcluster(22)

## assumes voxels are 0-ordered
correlateall <- function(vox,ss)
{
    for (i in 1:4)
    {
        basedir <- Sys.getenv("state")
        tsHEAD <- paste(basedir,"/",ss,"/blur.",i,".",ss,".steadystate.TRIM+orig.HEAD",sep="")
        tsBRIK <- paste(basedir,"/",ss,"/blur.",i,".",ss,".steadystate.TRIM+orig.BRIK",sep="")
        tstxt <- paste(basedir,"/",ss,"/blur.",i,".",ss,".steadystate.TRIM.noijk_dump",sep="")
        motionfile <- paste(basedir,"/",ss,"/motion.",i,".",ss,".steadystate.TRIM",sep="")
        maskHEAD <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.HEAD",sep="")
        maskBRIK <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.BRIK",sep="")

        vox_1d <- as.matrix(read.table(tstxt,nrows=1,skip=vox))
        dfile <- paste(basedir,"/",ss,"/corrTRIM_AFNIversion/voxel",vox,"TS.1D",sep="")
        bucketfile <- paste(basedir,"/",ss,"/corrTRIM_AFNIversion/bucket.voxel",vox,ss,sep="")
        write(vox_1d,dfile,sep="\n")

        afnicmd1 <- paste("3dDeconvolve -input ",tsBRIK," -polort 1 -num_stimts 7 -stim_file 1 ",dfile," -stim_file 2 ",motionfile,"'[1]' -stim_base 2 -stim_file 3 ",motionfile,"'[2]' -stim_base 3 -stim_file 4 ",motionfile,"'[3]' -stim_base 4 -stim_file 5 ",motionfile,"'[4]' -stim_base 5 -stim_file 6 ",motionfile,"'[5]' -stim_base 6 -stim_file 7 ",motionfile,"'[6]' -stim_base 7 -rout -bucket ",bucketfile,sep="")
        print(afnicmd1)
        system(afnicmd1)

        corroutfile <- paste(basedir,"/",ss,"/corrTRIM_AFNIversion/corrvals.voxel",vox,ss,sep="")
        afnicmd2 <- paste("3dcalc -a ",bucketfile,"+orig.BRIK'[3]' -b ",bucketfile,"+orig.BRIK'[2]' -expr 'ispositive(b)*sqrt(a)-isnegative(b)*sqrt(a)' -prefix ",corroutfile,sep="")
        print(afnicmd2)
        system(afnicmd2)

        voxtxt <- paste(basedir,"/",ss,"/corrTRIM_AFNIversion/corrvals.voxel",vox,".",i,".",ss,"noijk.txt",sep="")
        afnicmd3 <- paste("3dmaskdump -mask ",maskBRIK," -noijk ",corroutfile,"+orig.BRIK | awk '{print $1}' > ",voxtxt,sep="")
        print(afnicmd3)
        system(afnicmd3)

        system(paste("rm ",dfile))
        system(paste("rm ",bucketfile,"*",sep=""))
        system(paste("rm ",corroutfile,"+orig.*",sep=""))
    }
}

parallelCorr <- function(numVox,ss)
{
    parSapply(cluster,0:numVox,correlateall,ss)
}

parallelCorr(nvox-1,subj)
stopCluster(cluster)
