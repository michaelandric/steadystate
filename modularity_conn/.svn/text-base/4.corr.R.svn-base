## this version set up to run on condor cluster

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
nvox <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
ntp <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][4]))

library(bct)

## assumes voxels are 0-ordered
correlateall <- function(i,ss,nvox,ntp)
{
    library(bct)
    basedir <- Sys.getenv("state")
    tsHEAD <- paste(basedir,"/",ss,"/blur.",i,".",ss,".steadystate.TRIM+orig.HEAD",sep="")
    tsBRIK <- paste(basedir,"/",ss,"/blur.",i,".",ss,".steadystate.TRIM+orig.BRIK",sep="")
    motionfile <- paste(basedir,"/",ss,"/motion.",i,".",ss,".steadystate.TRIM",sep="")
    maskHEAD <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.HEAD",sep="")
    maskBRIK <- paste(basedir,"/",ss,"/automask_d3_",ss,"+orig.BRIK",sep="")
    bucketfile <- paste(basedir,"/",ss,"/corrTRIM_BLUR/dirtyTS.masked.Cond",i,".",ss,sep="")
    errts <- paste(basedir,"/",ss,"/corrTRIM_BLUR/cleanTS.masked.Cond",i,".",ss,sep="")

    ## clean the time series, regressing against motion estimates
    afnicmd1 <- paste("3dDeconvolve -input ",tsBRIK," -polort A -num_stimts 6 -stim_file 1 ",motionfile,"'[1]' -stim_file 2 ",motionfile,"'[2]' -stim_file 3 ",motionfile,"'[3]' -stim_file 4 ",motionfile,"'[4]' -stim_file 5 ",motionfile,"'[5]' -stim_file 6 ",motionfile,"'[6]' -rout -bucket ",bucketfile," -errts ",errts,sep="")
    print(afnicmd1)
    system(afnicmd1)

    ## now dump the clean time series to text file
    tstxt <- paste(basedir,"/",ss,"/corrTRIM_BLUR/cleanTS.Cond",i,".",ss,".noijk_dump",sep="")
    afnicmd2 <- paste("3dmaskdump -mask ",maskBRIK," -noijk ",errts,"+orig.BRIK > ",tstxt,sep="")
    print(afnicmd2)
    system(afnicmd2)

    ## now correlate voxel by voxel matrix
    fcorr(tstxt,nvox,ntp)
}

correlateall(cond,subj,nvox,ntp)

