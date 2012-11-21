# non-parametric repeated measures anova
# for voxel-by-voxel analysis
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
startvox <- as.numeric(noquote(strsplit(Args," ")[[1]][1]))
endvox <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)



friedman_func <- function(vox,subjects,conditions)
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
            voxeldata <- c(voxeldata,as.matrix(read.table(val,nrows=1,skip=vox)))
            subject_frame <- c(subject_frame,ss)
            condition_frame <- c(condition_frame,paste("cond",i,sep=""))
        }
    }
    val_frame <- data.frame(voxeldata, subject_frame, condition_frame)
    colnames(val_frame) <- c("vals", "subject", "condition")
    friedmanresult <- friedman.test(vals ~ condition | subject, data=val_frame)
    #print(summary(friedmanresult))
    friedmanstat <- friedmanresult$statistic[[1]]
    friedmanpval <- friedmanresult$p.value
    friedmanInvpval <- 1-friedmanpval
    #print(c(friedmanstat,friedmanpval,friedmanInvpval))
    return(c(friedmanstat,friedmanpval,friedmanInvpval))
}


outmat <- matrix(nrow=length(seq(startvox,endvox)),ncol=4)
cnt=1
for (vox in seq(startvox,endvox))
{
    outmat[cnt,] = c(vox,friedman_func(vox,subjects,conditions))
    cnt = cnt+1
}

outname <- paste(Sys.getenv("state"),"/groupstats/friedman_out.",startvox,".txt",sep="")
write.table(round(outmat,4),outname,row.names=F,col.names=F,quote=F)
