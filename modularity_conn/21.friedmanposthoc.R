# post hoc comparisons for friedman test
# set up to run on voxels that were p <= .05 
# for voxel-by-voxel analysis
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
group <- noquote(strsplit(Args," ")[[1]][1])

voxels <- as.matrix(read.table(paste(Sys.getenv("state"),"/groupstats/group",group,".txt",sep="")))
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)


data_build <- function(vox,subjects,conditions)
{
    voxeldata <- c()
    subject_frame <- c()
    condition_frame <- c()
    for (ss in subjects)
    {
        for (i in conditions)
        {
            #print(c(ss,i,vox))
            val <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",ss,".",i,".degrees.ijkSHORTtlrc.txt",sep="")
            voxeldata <- c(voxeldata,as.matrix(read.table(val,nrows=1,skip=vox-1)))
            subject_frame <- c(subject_frame,ss)
            condition_frame <- c(condition_frame,paste("cond",i,sep=""))
        }
    }
    data_frame <- data.frame(rep(vox,length(voxeldata)),voxeldata, subject_frame, condition_frame)
    colnames(data_frame) <- c("vox", "vals", "subject", "condition")
    return(data_frame)
}
    
friedman_posthoc <- function(x)
{
    pw <- pairwise.wilcox.test(x$vals, x$condition, paired=T, exact=F, p.adj="fdr")
    pw_result <- round(c(pw[[3]][1], pw[[3]][2], pw[[3]][3], pw[[3]][5], pw[[3]][6], pw[[3]][9]),3)
    median_result <- c(aggregate(x$vals, list(x$condition), median)[,2])
    sum_result <- c(aggregate(x$vals, list(x$condition), sum)[,2])
    return(c(pw_result, median_result, sum_result))
}



mmout <- c()
for (vv in voxels)
{
    print(vv)
    val_frame <- data_build(vv, subjects, conditions)
    out <- c(vv,friedman_posthoc(val_frame))
    mmout <- c(mmout,out)
}

mmout_mat <- matrix(mmout,nrow=length(voxels),byrow=T)

outname <- paste(Sys.getenv("state"),"/groupstats/friedmanposthoc_out.",voxels[1],".txt",sep="")
write.table(round(mmout_mat,4),outname,row.names=F,col.names=F,quote=F)
