## generate role tables

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

for (ss in subjects)
{
    setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
    print(getwd())
    role_mat <- matrix(nrow=7,ncol=4)
    for (cc in conditions)
    {
        dat <- as.matrix(read.table(paste(ss,".",cc,".node_roles",sep="")))
        for (i in seq(7))
        {
          role_mat[i,cc] = length(which(dat == i))
        }
    }
    write.table(role_mat, paste(ss,"_roletable.txt",sep=""),row.names=F,col.names=F,quote=F)
}


