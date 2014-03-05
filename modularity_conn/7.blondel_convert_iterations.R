## take the bin and make into link format for the blondel method to find communities
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
thresh <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

library(bct)

threshes <- c(15, 12, 8, 5)   # Doing at different proprotion of links preserved; 8 approximate name for median completeness, actually ~8.7%
for (t in threshes)
{
    thresh_mat <- paste(Sys.getenv("state"),"/links_files",t,"p/",subj,".",cond,".",t,"p_r",thresh,"_linksthresh_proportion.out", sep="")
    blondel_mat <- paste(Sys.getenv("state"),"/links_files",t,"p/",subj,".",cond,".",t,"p_r",thresh,"_linksthresh_proportion.out.srcdst", sep="")
    blondel_convert(thresh_mat, blondel_mat)
}


