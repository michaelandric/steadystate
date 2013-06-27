# test gamma dist shape param 
library(nortest)   # this library contains anderson-darling test for normality
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

gamma_dat <- c()
rate_dat <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep=""))
    dd <- read.table(paste("distance_gammafits_",ss,".txt", sep=""), header=T)
    gamma_dat <- c(gamma_dat, dd[,1])   # dd[,1] are the four shape parameters (one for each of four conditions)
    rate_dat <- c(rate_dat, dd[,2])   # dd[,1] are the four shape parameters (one for each of four conditions)
}

setwd(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/", sep=""))

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