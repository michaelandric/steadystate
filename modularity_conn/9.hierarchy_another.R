# Get hierarchy from tree 
library(bct)
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
nlevels <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

setwd(paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/another/", sep = ""))

tree <- paste("cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh.tree", sep="")
for (lvl in 0:nlevels)
{
    communities = blondel_hierarchy(tree, lvl)
}

