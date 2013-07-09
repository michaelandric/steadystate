## This is to threshold the N x N connectivity matrix
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
thresh <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
 
library(bct)

corrmat <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr",sep="")
outname <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh_",thresh,sep="")
fthreshold_absolute(corrmat,outname,thresh,0)

## take the bin and make into link format for the blondel method to find communities
thresh_mat <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh_",thresh,sep="")
blondel_mat <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh_",thresh,".srcdst",sep="")
blondel_convert(thresh_mat,blondel_mat)

