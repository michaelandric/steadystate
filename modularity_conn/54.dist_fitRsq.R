# get an R^2 value from distribution w/ fit parameters and data
library(MASS)
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

Rsq_vec <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/"))
    for (i in conditions)
    {
        dist_dat <- as.matrix(read.table(paste("distance_xyz_Filter20_",ss,"_Cond",i,".txt", sep="")))
        dist_dat <- dist_dat[!dist_dat == 0]   # remove where distance did not have value pass filter
        shape = fitdistr(dist_dat, "gamma")$estimate[["shape"]]
        rate = fitdistr(dist_dat, "gamma")$estimate[["rate"]]
        b = rgamma(length(dist_dat), shape=shape, rate=rate)
        Rsq = summary(lm(sort(dist_dat) ~ sort(b)))$r.squared
        Rsq_vec <- c(Rsq_vec, Rsq)
    }
}

setwd(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/", sep=""))

Rsq_df <- data.frame(Rsq_vec, as.factor(rep(seq(4), 19)), rep(subjects, each=4))
colnames(Rsq_df) <- c("RsqVals", "condition", "subject")

print(mean(Rsq_vec))
print(aggregate(Rsq_df$RsqVals, list(Rsq_df$condition), summary))