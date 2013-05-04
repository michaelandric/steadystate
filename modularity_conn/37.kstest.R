##This is to test distrubition differences between participant and random data

## This is to make the equivalent of /mnt/tier2/urihas/Andric/steadystate/groupstats/mod_score_table.txt but with random subjects
#subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN") # not using MRMC because the random networks in conditions 1 and 2 for this subject are not done -- HUGE links files is the presumed reason for why they dragging. This is why below I do this subj separately.
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRAG","MNGO","LRVN")
conditions <- seq(4)

mod_data <- c()
randmod_data <- c()
subject_frame <- c()
condition_frame <- c()

for (ss in subjects)
{
    for (i in conditions)
    {
        randmodscore <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/rand.",i,".",ss,".mod_score",sep="")
        randmod_data <- c(randmod_data,as.matrix(read.table(randmodscore))[1])
        subject_frame <- c(subject_frame,ss)
        condition_frame <- c(condition_frame,paste("cond",i,sep=""))
        modscore <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/mod_score.",ss,".Cond",i,".txt",sep="")
        mod_data <- c(mod_data,as.matrix(read.table(modscore))[1])
    }
}

randmod_score_frame <- data.frame(randmod_data,subject_frame,condition_frame)
mod_score_frame <- data.frame(mod_data,subject_frame,condition_frame)
colnames(randmod_score_frame) <- c("randmodularity","subject","condition")
colnames(mod_score_frame) <- c("modularity","subject","condition")

print(mean(randmod_score_frame$randmodularity))
print(mean(mod_score_frame$modularity))
print(sd(randmod_score_frame$randmodularity))
print(sd(mod_score_frame$modularity))
print(ks.test(mod_score_frame$modularity, randmod_score_frame$randmodularity))
#write.table(mod_score_frame,"mod_score_table.txt",row.names=F,col.names=F,quote=F)
