## get the z score for each voxel
library(Rmpi)
library(snow)
library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
ss <- noquote(strsplit(Args," ")[[1]][1])
nVoxArg <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
#CommSet <- c(as.numeric(noquote(strsplit(Args," ")[[1]][4:length(noquote(strsplit(Args," ")[[1]]))])))
Comm <- c(as.numeric(noquote(strsplit(Args," ")[[1]][4])))
print(Cond)
print(nVoxArg)
#print(CommSet)
print(.libPaths())

#cluster <- makeMPIcluster(8)

WriteScores <- function(x, ss, i)
{
    inmatrix <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".corrmatrix.bin.thresh",sep="")
    cifile <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".comm.tree3.justcomm",sep="")
    ci <- as.matrix(read.table(cifile))
    library(bct)
    par_fmodule_degree_zscore(inmatrix, ci, x)
}

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
#parallelFmod <- function(CommSet, nVox, ss, Cond)
#{
#    comm.zscores <- parSapply(cluster, CommSet, WriteScores, ss, Cond)
#    Zscores = zfile_concat(c(comm.zscores),nVox)
#}


comm.zscores = WriteScores(Comm,ss,Cond)
Zscores = zfile_concat(c(comm.zscores),nVox)
#parallelFmod(CommSet, nVoxArg, ss, Cond)
#stopCluster(cluster)
#mpi.exit()

