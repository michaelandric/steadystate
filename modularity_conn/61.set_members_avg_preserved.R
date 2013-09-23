##Get average preserved across participants
##Data in tlrc space with coordinates in first three columns
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

subj_mat <- matrix(ncol = length(subjects), nrow = 231203) ## these are nrows correspond to tlrc space
for (i in 1:length(subjects))
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",subjects[i],"/corrTRIM_BLUR/", sep = ""))
    subj_mat[,i] <- as.matrix(read.table(paste("preserved_",subjects[i],"_tlrc_dump.txt", sep = "")))[,4]
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")

out_vec <- rowMeans(subj_mat)
write.table(round(out_vec, 4), "preserved_group_avg.txt", row.names = F, col.names = F, quote = F)
