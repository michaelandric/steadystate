## get the z score for each voxel
## 02.Oct.2012 Making a stupid version of this that just finds the Z score for every voxel with a community assignment
library(Rmpi)
library(snow)
library(bct)

cluster <- makeMPIcluster(16)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
ss <- noquote(strsplit(Args," ")[[1]][1])
nVoxArg <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
print(Cond)
print(nVoxArg)

inmatrix <- paste(Sys.getenv("state"),"/",ss,"/connectivity/",ss,".",Cond,".corrmatrix.bin.thresh",sep="")
cifile <- paste(Sys.getenv("state"),"/",ss,"/connectivity/",ss,".",Cond,".comm.tree3.justcomm",sep="")
ci <- as.matrix(read.table(cifile))
CommSet <- unique(ci)
print(length(CommSet))

outname <- paste(Sys.getenv("state"),"/",ss,"/connectivity/",ss,".",Cond,".tree3.allZscores.txt",sep="")


## run the zscore function
WriteScores <- function(x, inmatrix, ci)
{
    library(bct)
    par_fmodule_degree_zscore(inmatrix, ci, x)
}

## concatentate the zbin out files from par_fmodule_degree_zscore
zfile_concat <- function(filelist, size)
{
    Z = mat.or.vec(size, 1)
    ## overwrite any zero value with new value
    for (f in filelist)
    {
        zz <- file(f, "rb")
        zarray <- readBin(zz, numeric(), size)
        idx = 0
        for (ii in zarray)
        {
            if (ii != 0)
            {
                Z[idx] = ii
            }
            idx = idx + 1
        }
        close(zz)
    }
    return(Z)
}

##Compute z scores in paralell
parallelFmod <- function(CommSet, nVox, inmatrix, ci, outname)
{
    comm.zscores <- parSapply(cluster, CommSet, WriteScores, inmatrix, ci)
    Zscores <- zfile_concat(c(comm.zscores),nVox)
    write.table(Zscores,outname,row.names=F,col.names=F,quote=F)
}



parallelFmod(CommSet, nVoxArg, inmatrix, ci, outname)
stopCluster(cluster)
mpi.exit()
