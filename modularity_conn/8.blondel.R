## This now includes 'thresh' variable 
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
thresh <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

library(bct)
srcdst <- paste(Sys.getenv("state"),"/links_files/modularity/",subj,".",cond,".",thresh,"median_linksthresh.out.srcdst", sep="") 
tree <- paste(Sys.getenv("state"),"/links_files/modularity/",subj,".",cond,".",thresh,"median_linksthresh.out.tree", sep="")
modularity_score = blondel_community(srcdst, tree)
print(modularity_score)

modout <- paste(Sys.getenv("state"),"/links_files/modularity/mod_score.",subj,".",cond,".",thresh,"median_linksthresh.txt",sep="")
write.table(modularity_score, modout, row.names=F, col.names=F, quote=F)

