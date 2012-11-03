library(Rmpi)
library(snow)
library(bct)

cluster <- makeMPIcluster(16)

args = commandArgs(trailingOnly=TRUE)
ss = args[1]

thresh_func <- function(i,ss)
{
    library(bct)
    corrmat <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".corrmatrix.bin",sep="")
    fthreshold_absolute(corrmat,.25,1)
}


parSapply(cluster,2:4,thresh_func,ss)
stopCluster(cluster)
