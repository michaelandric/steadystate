## This now includes 'thresh' variable 
## DIDN'T HAVE TO USE THIS: SEE 70.community_iterations.py INSTEAD

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
thresh <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

library(bct)

threshes <- c(15, 12, 8, 5)   # Doing at different proprotion of links preserved; 8 approximate name for median completeness, actually ~8.7%
for (t in threshes)
{
    srcdst <- paste(Sys.getenv("state"),"/links_files",t,"p/",subj,".",cond,".",t,"p_r",thresh,"_linksthresh_proportion.out.srcdst", sep="")
    tree <- paste(Sys.getenv("state"),"/links_files",t,"p/",subj,".",cond,".",t,"p_r",thresh,"_linksthresh_proportion.out.tree", sep="")
    modularity_score = blondel_community(srcdst, tree)
    print(modularity_score)

    modout <- paste(Sys.getenv("state"),"/links_files",t,"p/mod_score.",subj,".",cond,".",t,"p_r",thresh,"_linksthresh_proportion.txt",sep="")
    write.table(modularity_score, modout, row.names=F, col.names=F, quote=F)
}

