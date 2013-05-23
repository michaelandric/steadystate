## This is to get the count of voxels in modules for each condition
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
cutoff = 100

average_counts <- c()

for (ss in subjects)
{
    for (i in conditions)
    {
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR",sep=""))
        dat <- as.matrix(read.table(list.files(pattern=paste("cleanTS.",i,".*.justcomm",sep=""))))
        avg_count <- mean(aggregate(dat, list(dat), length)$V1[which(aggregate(dat, list(dat), length)$V1 > cutoff)])
        average_counts <- c(average_counts, avg_count)
    }
}

setwd(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats",sep=""))
average_count_mat <- matrix(average_counts, nrow=length(subjects), ncol=length(conditions), byrow=T)

