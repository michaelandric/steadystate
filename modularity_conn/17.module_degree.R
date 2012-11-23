## getting the degree of each voxel
library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Tree <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
print(c(subj,cond,Tree))

setwd(paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/",sep=""))
threshmat <- paste("cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh",sep="")
comms <- paste("cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh.tree",Tree,".justcomm",sep="")

mod_degree <- fmodule_degree_zscore(threshmat,as.matrix(read.table(comms)))

outname <- paste(subj,".",cond,".mod_degree",sep="")
write(round(mod_degree,4),outname,sep="\n")
