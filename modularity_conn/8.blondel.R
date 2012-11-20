library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))


blondel_meth <- function(i,ss)
{
    library(bct)
    srcdst <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh.srcdst",sep="")
    tree <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/cleanTS.",cond,".",subj,"_graymask_dump.bin.corr.thresh.tree",sep="")
    modularity_score = blondel_community(srcdst,tree)
    return(modularity_score)
    print(modularity_score)
}

mod = blondel_meth(cond,subj)
print(mod)
modout <- paste(Sys.getenv("state"),"/",subj,"/corrTRIM_BLUR/mod_score.",subj,".Cond",cond,".txt",sep="")
write.table(mod,modout,row.names=F,col.names=F,quote=F)
