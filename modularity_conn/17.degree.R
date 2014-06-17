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

setwd(paste(Sys.getenv("state"),"/links_files5p/",sep=""))   # now doing this on matrices thresholded by edge density. 5p == 5 %
inmatrix <- paste(subj,".",cond,".5p_r0.5_linksthresh_proportion.out",sep="")
outname <- paste(subj,".",cond,".5p_linksthresh_proportion.degrees_gray",sep="")

outdegrees <- fdegrees_und(inmatrix,nVoxArg)
write(outdegrees,outname,sep="\n")
