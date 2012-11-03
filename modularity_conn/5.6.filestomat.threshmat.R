## this is a combined version of 5.filestomatrix.R and 6.thresholdmat.R
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
subj <- noquote(strsplit(Args," ")[[1]][1])
nvox <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

filestomat <- function(i,ss,nvox)
{
    library(bct)
    prefix <- paste(Sys.getenv("state"),"/",ss,"/corrORIG_versionTRIM/CorrTask.masked.voxel",sep="")
    suffix <- paste(".",i,".",ss,"noijk.txt",sep="")
    out <- paste(Sys.getenv("state"),"/",ss,"/corrORIG_versionTRIM/",ss,".",i,".corrmatrix.bin",sep="")
    filestomatrix(prefix,nvox,suffix,out)
}

thresh_func <- function(i,ss)
{
    library(bct)
    corrmat <- paste(Sys.getenv("state"),"/",ss,"/corrORIG_versionTRIM/",subj,".",i,".corrmatrix.bin",sep="")
    fthreshold_absolute(corrmat,.25,1)
}



filestomat(cond,subj,nvox)
thresh_func(cond,subj)
