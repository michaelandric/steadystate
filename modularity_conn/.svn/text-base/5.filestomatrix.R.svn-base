library(Rmpi)
library(snow)
library(bct)

cluster <- makeMPIcluster(16)

args = commandArgs(trailingOnly=TRUE)
ss = args[1]
nvox = as.numeric(args[2])
print(ss)
print(nvox)
print(str(nvox))

filestomat <- function(i,ss,nvox)
{
    library(bct)
    prefix <- paste(Sys.getenv("state"),"/",ss,"/corrORIG_versionTRIM/CorrTask.masked.voxel",sep="")
    suffix <- paste(".",i,".",ss,"noijk.txt",sep="")
    out <- paste(Sys.getenv("state"),"/",ss,"/corrORIG_versionTRIM/",ss,".",i,".corrmatrix.bin",sep="")
    filestomatrix(prefix,nvox,suffix,out)
}


#for (i in 1:4)
#{
#    pref <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/CorrTask.masked.voxel",sep="")
#    suf <- paste(".",i,".",ss,"noijk.txt",sep="")
#    out <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".corrmatrix.bin",sep="")
#    clusterCall(cluster,FUN=filestomatrix,pref,nvox,suf,out)
#}

parSapply(cluster,1:4,filestomat,ss,nvox)
stopCluster(cluster)
