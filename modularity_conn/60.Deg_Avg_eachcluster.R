## plot average in each cluster
library(gplots)
setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats")
conditions <- seq(4)
deg = read.table("deg_means_frame.txt")
Clsts=rep(seq(20),19*4)
degClst = data.frame(deg,Clsts)

errs <- c()
means <- c()
for (i in unique(Clsts))
{
    tmpMat = matrix(subset(degClst, degClst[,4]==i)[,1], nrow=19, byrow=T)
    #sd((tmpMat - rowMeans(tmpMat)) / sqrt(19))
    errs = c(errs, apply((tmpMat - rowMeans(tmpMat)) / sqrt(19), 2, sd))
    means = c(means, apply(tmpMat, 2, mean))
}

ylimit = c(0, 1.01 * max(means + errs))
pdf("Deg_Avg_eachcluster.pdf")
cond1Means = means[seq(1,length(means),4)]
cond1Errs = errs[seq(1,length(means),4)]
plotCond1 <- barplot2(cond1Means, beside = TRUE, ylim = ylimit, ylab = "Degrees (k)", col = "#1A1A1A", plot.grid = TRUE)
segments(x0 = plotCond1, x1 = plotCond1, y0 = cond1Means, y1 = cond1Means + cond1Errs)
segments(x0 = plotCond1 - .2, x1 = plotCond1 + .2, y0 = cond1Means + cond1Errs, y1 = cond1Means + cond1Errs)

cond2Means = means[seq(2,length(means),4)]
cond2Errs = errs[seq(2,length(means),4)]
plotCond1 <- barplot2(cond2Means, beside = TRUE, ylim = ylimit, ylab = "Degrees (k)", col = "#666666", plot.grid = TRUE)
segments(x0 = plotCond1, x1 = plotCond1, y0 = cond2Means, y1 = cond2Means + cond2Errs)
segments(x0 = plotCond1 - .2, x1 = plotCond1 + .2, y0 = cond2Means + cond2Errs, y1 = cond2Means + cond2Errs)

cond4Means = means[seq(4,length(means),4)]
cond4Errs = errs[seq(4,length(means),4)]
plotCond1 <- barplot2(cond4Means, beside = TRUE, ylim = ylimit, ylab = "Degrees (k)", col = "#B3B3B3", plot.grid = TRUE)
segments(x0 = plotCond1, x1 = plotCond1, y0 = cond4Means, y1 = cond4Means + cond4Errs)
segments(x0 = plotCond1 - .2, x1 = plotCond1 + .2, y0 = cond4Means + cond4Errs, y1 = cond4Means + cond4Errs)

cond3Means = means[seq(3,length(means),4)]
cond3Errs = errs[seq(3,length(means),4)]
plotCond1 <- barplot2(cond3Means, beside = TRUE, ylim = ylimit, ylab = "Degrees (k)", col = "#F2F2F2", plot.grid = TRUE)
segments(x0 = plotCond1, x1 = plotCond1, y0 = cond3Means, y1 = cond3Means + cond3Errs)
segments(x0 = plotCond1 - .2, x1 = plotCond1 + .2, y0 = cond3Means + cond3Errs, y1 = cond3Means + cond3Errs)

dev.off()