## This is to make the equivalent of /mnt/tier2/urihas/Andric/steadystate/groupstats/mod_score_table.txt but with random subjects
#subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN") # not using MRMC because the random networks in conditions 1 and 2 for this subject are not done -- HUGE links files is the presumed reason for why they dragging. This is why below I do this subj separately.
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRAG","MNGO","LRVN")
conditions <- seq(4)

mod_data <- c()
subject_frame <- c()
condition_frame <- c()

for (ss in subjects)
{
    for (i in conditions)
    {
        modscore <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/rand.",i,".",ss,".mod_score",sep="")
        mod_data <- c(mod_data,as.matrix(read.table(modscore))[1])
        subject_frame <- c(subject_frame,ss)
        condition_frame <- c(condition_frame,paste("cond",i,sep=""))
    }
}

for (i in c(3:4))
{
    ss = "MRMC"
    modscore <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/rand.",i,".",ss,".mod_score",sep="")
    mod_data <- c(mod_data,as.matrix(read.table(modscore))[1])
    subject_frame <- c(subject_frame,ss)
    condition_frame <- c(condition_frame,paste("cond",i,sep=""))
}

mod_score_frame <- data.frame(mod_data,subject_frame,condition_frame)
colnames(mod_score_frame) <- c("modularity","subject","condition")
#write.table(mod_score_frame,"mod_score_table.txt",row.names=F,col.names=F,quote=F)
