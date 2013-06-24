# test gamma dist shape param 
library(nortest)   # this library contains anderson-darling test for normality
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

dist_dat <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep=""))
    dd <- read.table(paste("distance_gammafits_",ss,".txt", sep=""), header=T)
    dist_dat <- c(dist_dat, dd[,1])
}

setwd(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/", sep=""))

dist_df <- data.frame(dist_dat, as.factor(rep(seq(4), 19)), rep(subjects, each=4))
colnames(dist_df) <- c("dists", "condition", "subject")
dist_mat <- matrix(dist_dat, ncol=4, byrow=T)

print(aggregate(dist_df$dists, list(dist_df$condition), summary))
print(aggregate(dist_df$dists, list(dist_df$subject), summary))
print(ad.test(dist_df$dists)) # normality test
print(summary(aov(dists ~ condition + Error(subject/condition), data=dist_df)))
print(friedman.test(dist_mat))