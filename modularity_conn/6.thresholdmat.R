## This is to threshold the N x N connectivity matrix
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))


library(bct)
corrmat <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr",sep="")
outname <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh_0.5",sep="")
fthreshold_absolute(corrmat,outname,.5,0)

