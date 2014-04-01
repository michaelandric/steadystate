## Test if there are voxel-wise effects for differences in preserved 

link_density <- "5p"
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats")

nvox <- 231203   # This the number of voxels in the tlrc space brain I use for groupstats
subj_mat <- matrix(ncol = 3, nrow = nvox) ## these are nrows correspond to tlrc space

for (vox in 1:nvox)
{
    #print(vox)
    vox_dat <- c()
    for (ss in subjects)
    {
        vox_dat <- c(vox_dat, scan(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/preserved_diff_",ss,"_median",link_density,"_warped_tlrc_dump.txt", sep = ""), skip = (vox-1), nlines = 1, quiet = T)[4])
    }
    #print(vox_dat)
    if (all(vox_dat == 0))
    {
        subj_mat[vox,] <- c(0, 0, 1)
    }else
    {    
        wv <- wilcox.test(vox_dat)
        #print(wv)
        subj_mat[vox,] <- c(wv$statistic[[1]], round(1-wv$p.value[[1]], 3), round(wv$p.value[[1]], 3))
        #print(subj_mat)
    }
}

write.table(subj_mat, "preserved_diff_group_median5p_warped_effects.txt", row.names = F, col.names = F, quote = F)

