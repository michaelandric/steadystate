# Examine voxel-wise distances across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

dist_data <- c()
subject_ids <- c()

for (ss in subjects)
{
    for (i in conditions)
    {
        dist_scores <- paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/distance_",ss,"_Cond",i,".txt",sep="")
        avg_dist_data <- c(avg_dist_data, mean(dist_scores))
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
avg_dist_mat <- matrix(c(avg_dist_data), ncol=4, byrow=T)
print(avg_dist_mat)
print(colMeans(avg_dist_mat))
print(apply(avg_dist_mat, 2, median))
print(shapiro.test(avg_dist_mat))
print(friedman.test(avg_dist_mat))