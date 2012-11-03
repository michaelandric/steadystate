library(Rmpi)
library(snow)
library(bct)

cluster <- makeMPIcluster(16)

args = commandArgs(trailingOnly=TRUE)
ss = args[1]


blondel_meth <- function(i,ss)
{
    library(bct)
    srcdst <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".corrmatrix.bin.thresh.srcdst",sep="")
    tree <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".comm.tree",sep="")
    modularity_score = blondel_community(srcdst,tree)
    return(modularity_score)
    print(modularity_score)
}


parSapply(cluster,1:4,blondel_meth,ss)
stopCluster(cluster)
