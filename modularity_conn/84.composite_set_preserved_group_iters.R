## read set preserved and get median at every voxel. 
## goes across the group data, so uses tlrc space data
## thus doing this in batches

## !!!!!!! THIS IS MUCH LIKE '61.set_members_avg_preserved.R'. 
## Different bcs getting median image for the 'iters' which are the null (condition against itself) and minor coding diffs
## Above line is no longer true. Now using this to get for real participant data, i.e., true 'SNSC' across group

fltmedian <- function(x) if (777 %in% x) return(777) else return(median(x))   # function to keep row with value of 777 if it shows up in any row.
fltmean <- function(x) if (777 %in% x) return(777) else return(mean(x))

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
nvoxels <- 231203
null_mat <- matrix(nrow = nvoxels, ncol = length(subjects))

cc <- c()
for (ss in 1:length(subjects))
{
    #ss_null <- paste("/mnt/tier2/urihas/Andric/steadystate/",subjects[ss],"/corrTRIM_BLUR/preserved_",subjects[ss],"_median5p_20vxFltr_warped_tlrc_dump.txt", sep = "")
    ss_null <- paste("/mnt/tier2/urihas/Andric/steadystate/",subjects[ss],"/corrTRIM_BLUR/iters_",subjects[ss],"_median5p_20vxFltr_warped_tlrc_dump.txt", sep = "")
    null_mat[,ss] <- scan(ss_null, quiet = TRUE)[seq(4, nvoxels*4, 4)]
    cc <- c(cc, length(which(null_mat[,ss] == 777))/nvoxels)
}

print(paste("Percent of vovxels in each column (each subject) that are 777"))
print(cc * 100)
median_vec <- apply(null_mat, 1, fltmedian)   # applying function to mark voxel as 777 if any voxel across subjects is 777. 777 carries from voxels in modules where n < 20
average_vec <- apply(null_mat, 1, fltmean)

print(paste(round(((length(which(median_vec == 777)) / nvoxels) * 100), 4)," % of voxels in median group vec that are 777 ", sep = ""))
print(paste(round(((length(which(average_vec == 777)) / nvoxels) * 100), 4)," % of voxels in average group vec that are 777 ", sep = ""))


setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats")

write.table(round(median_vec, 4), "iters_group_median5p_20vxFltr_warped_median.txt", row.names = F, col.names = F, quote = F)
write.table(round(average_vec, 4), "iters_group_median5p_20vxFltr_warped_average.txt", row.names = F, col.names = F, quote = F)

