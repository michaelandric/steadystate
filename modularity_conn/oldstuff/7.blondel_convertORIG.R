library(Rmpi)
library(snow)
library(bct)

cluster <- makeMPIcluster(16)

args = commandArgs(trailingOnly=TRUE)
ss = args[1]

convert_func <- function(i,ss)
{
    library(bct)
    thresh_mat <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".corrmatrix.bin.thresh",sep="")
    blondel_mat <- paste(Sys.getenv("state"),"/",ss,"/TaskOutCor_Cond",i,"Files/",ss,".",i,".corrmatrix.bin.thresh.srcdst",sep="")
    blondel_convert(thresh_mat,.25,blondel_mat)
}


parSapply(cluster,1:4,convert_func,ss)
stopCluster(cluster)
