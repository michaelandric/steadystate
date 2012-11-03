library(Rmpi)
library(snow)
library(bct)

args <- commandArgs(trailingOnly=TRUE)
subj <- args[1]
print(subj)
#nvox <- 8
nvox <- as.numeric(args[2])
cluster <- makeMPIcluster(16)

## assumes voxels are 0-ordered
correlateall <- function(vox,ss)
{
    for (i in 1:4)
    {
        basedir <- Sys.getenv("state")
        tsHEAD <- paste(basedir,"/",ss,"/reg.",i,".",ss,".steadystate+orig.HEAD",sep="")
        tsBRIK <- paste(basedir,"/",ss,"/reg.",i,".",ss,".steadystate+orig.BRIK",sep="")
        tstxt <- paste(basedir,"/",ss,"/reg.",i,".",ss,".steadystate.noijk_dump",sep="")
        motionfile <- paste(basedir,"/",ss,"/motion.",i,".",ss,".steadystate",sep="")
        maskHEAD <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.HEAD",sep="")
        maskBRIK <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.BRIK",sep="")

        vox_1d <- as.matrix(read.table(tstxt,nrows=1,skip=vox))
        dfile <- paste("voxel",vox,"TS.1D",sep="")
        bucketfile <- paste(basedir,"/",ss,"/corrTask.masked.voxel",vox,ss,sep="")
        write(vox_1d,dfile,sep="\n")

        afnicmd1 <- paste("3dDeconvolve -input ",tsBRIK," -polort 1 -num_stimts 7 -stim_file 1 ",dfile," -stim_file 2 ",motionfile,"'[1]' -stim_base 2 -stim_file 3 ",motionfile,"'[2]' -stim_base 3 -stim_file 4 ",motionfile,"'[3]' -stim_base 4 -stim_file 5 ",motionfile,"'[4]' -stim_base 5 -stim_file 6 ",motionfile,"'[5]' -stim_base 6 -stim_file 7 ",motionfile,"'[6]' -stim_base 7 -rout -bucket ",bucketfile,sep="")
        print(afnicmd1)
        system(afnicmd1)

        voxtxt <- paste(basedir,"/",ss,"/TaskOutCor_Cond",i,"Files/CorrTask.masked.voxel",vox,".",i,".",ss,"noijk.txt",sep="")
        afnicmd2 <- paste("3dmaskdump -mask ",maskBRIK," -noijk ",bucketfile,"+orig.BRIK | awk '{print $1}' > ",voxtxt,sep="")
        print(afnicmd2)
        system(afnicmd2)
        system(paste("rm ",dfile))
        system(paste("rm ",bucketfile,"*",sep=""))
    }
}

parallelCorr <- function(numVox,ss)
{
    parSapply(cluster,0:numVox,correlateall,ss)
}

parallelCorr(nvox-1,subj)
stopCluster(cluster)
