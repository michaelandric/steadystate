## read set preserved and get median at every voxel. 
## goes across the group data, so uses tlrc space data
## thus doing this in batches

## !!!!!!! THIS IS MUCH LIKE '61.set_members_avg_preserved.R'. 
## Different bcs getting median image for the 'iters' which are the null (condition against itself) and minor coding diffs

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
nvoxels <- 231203
null_mat <- matrix(nrow = nvoxels, ncol = length(subjects))

for (ss in 1:length(subjects))
{
    ss_null <- paste("/mnt/tier2/urihas/Andric/steadystate/",subjects[ss],"/corrTRIM_BLUR/iters_",subjects[ss],"_median5p_warped_tlrc_dump.txt", sep = "")
    null_mat[,ss] <- scan(ss_null, quiet = TRUE)[seq(4, nvoxels*4, 4)]
}

null_median_vec <- apply(null_mat, 1, median)
null_average_vec <- apply(null_mat, 1, mean)

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats")

write.table(round(null_median_vec, 4), "iters_group_median5p_warped_median.txt", row.names = F, col.names = F, quote = F)
write.table(round(null_average_vec, 4), "iters_group_median5p_warped_average.txt", row.names = F, col.names = F, quote = F)

