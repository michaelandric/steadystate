## take the bin and make into link format for the blondel method to find communities
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
thresh <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

library(bct)

thresh_mat <- paste(Sys.getenv("state"),"/links_files/",subj,".",cond,".",thresh,"median_linksthresh.out", sep="")
blondel_mat <- paste(Sys.getenv("state"),"/links_files/modularity/",subj,".",cond,".",thresh,"median_linksthresh.out.srcdst", sep="")
blondel_convert(thresh_mat, blondel_mat)


