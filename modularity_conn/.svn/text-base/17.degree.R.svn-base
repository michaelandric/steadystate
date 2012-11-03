## getting the degree of each voxel
library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
ss <- noquote(strsplit(Args," ")[[1]][1])
nVoxArg <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
print(Cond)
print(nVoxArg)

setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
outname <- paste(ss,".",Cond,".degrees",sep="")
inmatrix <- paste("cleanTS.Cond",Cond,".",ss,".noijk_dump.bin.corr.thresh",sep="")

outdegrees <- fdegrees_und(inmatrix,nVoxArg)
write(outdegrees,outname,sep="\n")
