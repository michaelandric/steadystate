# Examine voxel-wise distances across conditions
# Find whether shape parameter differs by condition across the group
# Find whether rate parameter differs by condition across the group
library(MASS)
library(nortest)
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

gamma_dat <- c()
rate_dat <- c()


for (ss in subjects)
{
    for (i in conditions)
    {
        dist_scores <- paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/distance_xyz_Filter20_",ss,"_Cond",i,".txt", sep="")
        dist_dat <- as.matrix(read.table(dist_scores))
        dist_dat <- dist_dat[!dist_dat == 0]   # remove where distance did not have value pass filter
        gamma_dat <- c(gamma_dat, fitdistr(dist_dat, "gamma")$estimate[[1]])   # this 'estimate' the gamma shape parameter
        rate_dat <- c(rate_dat, fitdistr(dist_dat, "gamma")$estimate[[2]])   # this 'estimate' the gamma rate parameter
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")

gamma_df <- data.frame(gamma_dat, as.factor(rep(seq(4), 19)), rep(subjects, each=4))
rate_df <- data.frame(rate_dat, as.factor(rep(seq(4), 19)), rep(subjects, each=4))
colnames(gamma_df) <- c("gamma", "condition", "subject")
colnames(rate_df) <- c("rate", "condition", "subject")
gamma_mat <- matrix(gamma_dat, ncol=4, byrow=T)
rate_mat <- matrix(rate_dat, ncol=4, byrow=T)

for (n in c("gamma", "rate"))
{
    dist_df <- get(paste(n,"_df", sep=""))
    dist_mat <- get(paste(n,"_mat", sep=""))
    print(aggregate(dist_df[,1], list(dist_df$condition), summary))
    print(aggregate(dist_df[,1], list(dist_df$subject), summary))
    print(ad.test(dist_df[,1]))   # normality test
    print(summary(aov(dist_df[,1] ~ condition + Error(subject/condition), data=dist_df)))
    print(friedman.test(dist_mat))
}

