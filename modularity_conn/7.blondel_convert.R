## take the bin and make into link format for the blondel method to find communities
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))


library(bct)
thresh_mat <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh",sep="")
blondel_mat <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh.srcdst",sep="")
blondel_convert(thresh_mat,blondel_mat)


