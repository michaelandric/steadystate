##Get average preserved across participants
##Data in tlrc space with coordinates in first three columns
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

subj_mat <- matrix(ncol = length(subjects), nrow = 231203) ## these are nrows correspond to tlrc space
for (i in 1:length(subjects))
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",subjects[i],"/corrTRIM_BLUR/", sep = ""))
    #subj_mat[,i] <- as.matrix(read.table(paste("preserved_",subjects[i],"_tlrc_dump.txt", sep = "")))[,4]
    subj_mat[,i] <- as.matrix(read.table(paste("preserved_",subjects[i],"_median5p_warped_tlrc_dump.txt", sep = "")))[,4]
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")

#out_vec_avg <- rowMeans(subj_mat)
out_vec_med <- apply(subj_mat, 1, median)
#write.table(round(out_vec_avg, 4), "preserved_warped_group_avg.txt", row.names = F, col.names = F, quote = F)
#write.table(round(out_vec_med, 4), "preserved_group_median.txt", row.names = F, col.names = F, quote = F)
write.table(round(out_vec_med, 4), "preserved_group_median5p_warped_median.txt", row.names = F, col.names = F, quote = F)

