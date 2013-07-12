# assess the modularity values at different thresholds
library(epicalc) # has "aggregate.plot"
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
condition_names = c("Highly ordered", "Some order", "Random", "Almost Random")
thresholds <- c("0.2", "0.3", "0.4", "0.5")

dat <- c()
for (t in 1:(length(thresholds)-1)) # 0.5 is the main data. It is under different name than the others so it's in next loop
{
    for (ss in subjects)
    {
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep=""))
        for (i in conditions)
        {
            dat <- c(dat, round(read.table(paste("mod_score.",ss,".Cond",i,"thresh_",thresholds[t],".txt", sep=""))[[1]], 4))
        }
    }
}

dat_orig <- c()
for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep=""))
    for (i in conditions)
    {
        dat_orig <- c(dat_orig, round(read.table(paste("mod_score.",ss,".Cond",i,".txt", sep=""))[[1]], 4))
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")

dat <- c(dat, dat_orig)
#condition_vec <- rep(as.factor(rep(seq(4), 19)), 4)
condition_vec <- rep(rep(condition_names, 19), 4)
subjects_vec <- rep(rep(subjects, each=4), 4)
thresh_levels <- rep(thresholds, each = length(subjects) * length(conditions))
mod_score_frame <- data.frame(dat, condition_vec, subjects_vec, thresh_levels)
colnames(mod_score_frame) <- c("modularity", "condition", "subject", "thresh")

## Now analyze modularity variance at each correlation matrix threshold 
for (t in levels(mod_score_frame$thresh))
{
    print(paste("===== At correlation matrix threshold: ",t," =====",sep=""))
    tmp <- subset(mod_score_frame, thresh == t)
    print(summary(aov(modularity ~ condition + Error(subject/condition), data=tmp)))
    print(aggregate(tmp$modularity, list(tmp$condition), mean))
}

## Barplots for the scores in each condition at different thresholds 
pdf("agplot_mod_scores.pdf")
aggregate.plot(mod_score_frame$modularity, list(mod_score_frame$thresh, mod_score_frame$condition), mean, main = F, legend.site = "topleft")
title("Modularity by connection threshold (Pearson's r)")
dev.off()