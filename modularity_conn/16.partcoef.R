## getting the degree of each voxel
library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
ss <- noquote(strsplit(Args," ")[[1]][1])
Tree <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
print(c(ss,Tree,Cond))

setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
threshmat <- paste("cleanTS.Cond",Cond,".",ss,".noijk_dump.bin.corr.thresh",sep="")
comms <- paste("cleanTS.Cond",Cond,".",ss,".noijk_dump.bin.corr.thresh.tree",Tree,".justcomm",sep="")
part_coef <- fparticipation_coef(threshmat,as.matrix(read.table(comms)))

outname <- paste(ss,".",Cond,".part_coef",sep="")
write(round(part_coef,4),outname,sep="\n")
