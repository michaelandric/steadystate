## This is to generate random networks and determine their modularity
library(bct)
ss <- noquote(strsplit(Args," ")[[1]][1])
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
input_links <- paste("cleanTS.",Cond,".",ss,"_graymask_dump.bin.corr.thresh.links",sep="")
out_random_links <- paste("rand.",Cond,".",ss,".links",sep="")
setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
rand_bin_und(input_links,out_random_links,.9)

