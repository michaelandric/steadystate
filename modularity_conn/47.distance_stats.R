# Examine voxel-wise distances across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

avg_dist_data <- c()

for (ss in subjects)
{
    for (i in conditions)
    {
        dist_scores <- paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/distance_",ss,"_Cond",i,".txt",sep="")
        avg_dist_data <- c(avg_dist_data, mean(as.matrix(read.table(dist_scores))))
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
avg_dist_mat <- matrix(c(avg_dist_data), ncol=4, byrow=T)
dist_df <- data.frame(avg_dist_data, rep(seq(4), 19), rep(subjects, each=4))
colnames(dist_df) <- c("dists", "condition", "subject")
print(summary(aov(dists ~ condition + Error(subject/condition), data=dist_df)))
print(avg_dist_mat)
print(colMeans(avg_dist_mat))
print(apply(avg_dist_mat, 2, median))
print(shapiro.test(avg_dist_mat))
print(friedman.test(avg_dist_mat))
