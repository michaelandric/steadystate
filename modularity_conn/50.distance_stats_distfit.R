# Examine voxel-wise distances across conditions
# Find whether shape parameter differs by condition across the group
library(MASS)
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
dist_fits <- c()

for (ss in subjects)
{
    for (i in conditions)
    {
        dist_scores <- paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/distance_",ss,"_Cond",i,".txt",sep="")
        dist_dat <- as.matrix(read.table(dist_scores))
        dist_dat <- dist_dat[!dist_dat == 0]   # remove where distance did not have value pass filter
        dist_fits <- c(dist_fits, fitdistr(dist_dat, "gamma")$estimate[[1]])   # this 'estimate' the gamma shape parameter
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
dist_fits_mat <- matrix(c(dist_fits), ncol=4, byrow=T)
dist_df <- data.frame(dist_fits, rep(seq(4), 19), rep(subjects, each=4))
colnames(dist_df) <- c("dists", "condition", "subject")
print(summary(aov(dists ~ condition + Error(subject/condition), data=dist_df)))
print(dist_fits_mat)
print(colMeans(dist_fits_mat))
print(apply(dist_fits_mat, 2, median))
print(shapiro.test(dist_fits_mat))
print(friedman.test(dist_fits_mat))
