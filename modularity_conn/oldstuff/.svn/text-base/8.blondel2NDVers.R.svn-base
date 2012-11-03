library(bct)

args = commandArgs(trailingOnly=TRUE)
ss = args[1]
Cond = args[2]

blondel_meth <- function(i,ss)
{
    library(bct)
    subjdir <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",sep="")
    system(paste("cd",subjdir))
    print(getwd())
    srcdst <- paste(ss,".",i,".corrmatrix.bin.thresh.srcdst",sep="")
    tree <- paste(ss,".",i,".comm.tree",sep="")
    modularity_score = blondel_community(srcdst,tree)
    return(modularity_score)
    print(modularity_score)
}


blondel_meth(Cond,ss)
