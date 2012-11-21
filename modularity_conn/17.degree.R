## getting the degree of each voxel
library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
nVoxArg <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
print(cond)
print(nVoxArg)

setwd(paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/",sep=""))
inmatrix <- paste("cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh",sep="")
outname <- paste(subj,".",cond,".degrees_gray",sep="")

outdegrees <- fdegrees_und(inmatrix,nVoxArg)
write(outdegrees,outname,sep="\n")
