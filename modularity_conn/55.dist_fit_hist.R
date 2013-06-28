# plot data histogram with estimated gamma fit, also get R^2 between them
library(MASS)
library(RColorBrewer)
#subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
subjects <- c("ANGO")
conditions <- seq(4)
condition_names = c("Highly ordered", "Some order", "Random", "Almost Random")

thepal = colorRampPalette(brewer.pal(9,"Set2"))(9)
thepalOrder = thepal[c(1,2,4,3)]

pdf(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/Distance_density_fits.pdf",sep=""), paper="a4r", width=10.5)
par(mfrow = c(2,4))

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep=""))
    dd <- read.table(paste("distance_gammafits_",ss,".txt", sep=""), header=T)
    for (i in conditions)
    {
        dist_dat <- as.matrix(read.table(paste("distance_noavgs_Filter20_",ss,"_Cond",i,".txt", sep="")))
        dist_dat <- dist_dat[!dist_dat == 0]
        b = rgamma(length(dist_dat), shape = dd$shape[i], rate = dd$rate[i])
        Rsq = summary(lm(sort(dist_dat) ~ sort(b)))$r.squared
        ddh = hist(dist_dat, probability = TRUE, ylim = c(range(density(b)$y)), main = paste(ss," ",condition_names[i]," // R^2=",round(Rsq,4), sep=""))
        lines(density(b, from = ddh$breaks[1], to = ddh$breaks[length(ddh$breaks)]), col = thepalOrder[i], lwd = 2)
    }
}
dev.off()