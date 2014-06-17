# get an R^2 value from distribution w/ fit parameters and data
library(MASS)
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

Rsq_vec <- c()
shape_param_vec <- c()
for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity5p/distances/", sep=""))
    dd <- read.table(paste("distance_gammafits_",ss,".txt", sep=""), header=T)
    for (i in conditions)
    {
        print(date())
        dist_dat <- as.matrix(read.table(paste("distances_xyz_filt20_",ss,"_Cond",i,".txt", sep="")))
        dist_dat <- dist_dat[!dist_dat == 0]   # remove where distance did not have value pass filter
        est_shape = dd$shape[i]
        est_rate = dd$rate[i]
        b = rgamma(length(dist_dat), shape=est_shape, rate=est_rate)
        Rsq = summary(lm(sort(dist_dat) ~ sort(b)))$r.squared
        Rsq_vec <- c(Rsq_vec, Rsq)
        shape_param_vec <- c(shape_param_vec, est_shape)
    }
}

setwd(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/", sep=""))
print("=====For distributions without average at each voxel======")
print(matrix(Rsq_vec, ncol=4, byrow=T))
print(matrix(shape_param_vec, ncol=4, byrow=T))
shape_df <- data.frame(shape_param_vec, as.factor(rep(seq(4), 19)), rep(subjects, each=4))
Rsq_df <- data.frame(Rsq_vec, as.factor(rep(seq(4), 19)), rep(subjects, each=4))
colnames(shape_df) <- c("shapes", "condition", "subject")
colnames(Rsq_df) <- c("RsqVals", "condition", "subject")

print(mean(Rsq_vec))
print(aggregate(Rsq_df$RsqVals, list(Rsq_df$condition), summary))
