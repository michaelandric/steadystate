## This now includes 'thresh' variable 
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
thresh <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

library(bct)
srcdst <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh_",thresh,".srcdst",sep="")
tree <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh_",thresh,".tree",sep="")
modularity_score = blondel_community(srcdst, tree)
print(modularity_score)

modout <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/mod_score.",subj,".Cond",cond,"thresh_",thresh,".txt",sep="")
write.table(modularity_score, modout, row.names=F, col.names=F, quote=F)

