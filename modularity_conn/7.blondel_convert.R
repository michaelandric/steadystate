## take the bin and make into link format for the blondel method to find communities
library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))


convert_func <- function(i,ss)
{
    library(bct)
    thresh_mat <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/cleanTS.Cond",i,".",ss,".noijk_dump.bin.corr.thresh",sep="")
    blondel_mat <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/cleanTS.Cond",i,".",ss,".noijk_dump.bin.corr.thresh.srcdst",sep="")
    blondel_convert(thresh_mat,blondel_mat)
}


convert_func(cond,subj)

