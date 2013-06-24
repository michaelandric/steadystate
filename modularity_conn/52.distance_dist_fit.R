# get parameters for distribution fit
library(MASS)
ss <- noquote(strsplit(Args," ")[[1]][1])
conditions <- seq(4)
dist_fit <- c()

setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep="")

for (i in conditions)
{
    dist_name <- paste("distance_noavgs_Filter20_",ss,"_Cond",i,".txt", sep="")
    dist_scores <- as.matrix(read.table(dist_name))
    dist_scores <- dist_scores[!dist_scores < 20]   # filters final couple voxels that got 0 in original filter
    dist_fit <- rbind(dist_fit, fitdistr(dist_scores, "gamma")$estimate)
}

write.table(dist_fit, paste("distance_gammafits_",ss,".txt",sep=""), row.names=F, quote=F)
