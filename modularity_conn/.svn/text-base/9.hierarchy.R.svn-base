library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
nlevels <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))



blondel_hier <- function(i,ss,nlevels)
{
    subjdir <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep="")
    #subjdir <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/thresh.6/",sep="")
    setwd(paste(subjdir))
    tree <- paste("cleanTS.Cond",i,".",ss,".noijk_dump.bin.corr.thresh.tree",sep="")
    for (lvl in 0:nlevels)
    {
        communities = blondel_hierarchy(tree,lvl)
    }

}


blondel_hier(cond,subj,nlevels)
