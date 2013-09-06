## plot average in each cluster
library(gplots)
library(ggplot2)
library(RColorBrewer)
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
#pdf("Deg_Avg_eachcluster.pdf")
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

#dev.off()


condition_names = c("Highly ordered", "Some order", "Random", "Almost random")
mean_frame = data.frame(means, rep(condition_names, 20), rep(seq(20), each = 4))

cond1Means = means[seq(1,length(means),4)]
cond2Means = means[seq(2,length(means),4)]
cond4Means = means[seq(4,length(means),4)]
cond3Means = means[seq(3,length(means),4)]
mean_frame2 = data.frame(c(cond1Means, cond2Means, cond4Means, cond3Means), rep(seq(4), 20), rep(seq(20), each = 4))
colnames(mean_frame2) <- c("ClustMean", "Condition", "Cluster")
#ggplot(mean_frame2, aes(x = Condition, y = ClustMean, group = Cluster, color = Cluster)) + geom_line() + theme(panel.background = element_rect(fill = "white"))

ylimit = c(0, 1.1 * max(means))
## Color Version
thepal = colorRampPalette(brewer.pal(8,"Dark2"))(20)
pdf("Deg_Avg_eachcluster_linesColor.pdf")
plot(mean_frame2[c(1:4),1], ylim = ylimit, type = "b", pch = 1, col = thepal[1], ylab = "Mean Degrees (k)", xaxt = "n", bty = "n", lwd = 2)
axis(side = 1, at = c(seq(4)))
for (i in unique(Clsts)[1:(length(unique(Clsts)) - 1)])
{
    lines(mean_frame2[c(1:4)+(4*i),1], type = "b", pch = i, col = thepal[i], lwd = 2)
}
dev.off()

## BW Version
pdf("Deg_Avg_eachcluster_linesBW.pdf")
plot(mean_frame2[c(1:4),1], ylim = ylimit, type = "b", lty = 1, pch = 1, ylab = "Mean Degrees (k)", xaxt = "n", bty = "n", lwd = 2)
axis(side = 1, at = c(seq(4)))
for (i in unique(Clsts)[1:(length(unique(Clsts)) - 1)])
{
    lines(mean_frame2[c(1:4)+(4*i),1], type = "b", lty = i, pch = i, lwd = 2)
}
dev.off()

## Color Version 2 — cleaner, same pch for all
pdf("Deg_Avg_eachcluster_linesColor2.pdf")
plot(mean_frame2[c(1:4),1], ylim = ylimit, type = "b", pch = 16, col = thepal[1], ylab = "Mean Degrees (k)", xaxt = "n", bty = "n", lwd = 2)
axis(side = 1, at = c(seq(4)))
for (i in unique(Clsts)[1:(length(unique(Clsts)) - 1)])
{
    lines(mean_frame2[c(1:4)+(4*i),1], type = "b", pch = 16, col = thepal[i], lwd = 2)
}
dev.off()

## TREND INFORMATION
trends <- vector(mode = "list", length = length(unique(Clsts)))
names(trends) <- c(letters[1:length(unique(Clsts))])

for (i in unique(Clsts))
{
    print(c(i, mean_frame2[c(1:4) + (4 * (i - 1)), 1]))
    print(rank(mean_frame2[c(1:4) + (4 * (i - 1)), 1]))
    trends[[letters[i]]] = c(rank(mean_frame2[c(1:4) + (4 * (i - 1)), 1]))
}

uniq <- unique(trends)
clust_types <- vector(mode = "list", length = length(uniq))
cnt = 0
for (a in uniq)
{
    cnt = cnt+1
    i = 0
    ident <- c()
    for (t in 1:length(trends))
    {
        if (identical(a,trends[[t]]))
        {
            i = i+1
            ident <- c(ident, t)
        }
    }
    #print(ident)
    clust_types[[cnt]] = ident
    #print(clust_types)
    #print(c(a, i))
}


for (x in 1:length(clust_types))
{
    pdf(paste("Deg_Trends",x,".pdf", sep = ""))
    #mean_frame2[c(1:4) + (4 * (clust_types[[x]][1] - 1)), 1]
    #clust_types[[x]][1]
    plot(mean_frame2[c(1:4) + (4 * (clust_types[[x]][1] - 1)), 1], ylim = ylimit, type = "b", pch = 16, col = thepal[clust_types[[x]][1]], ylab = "Mean Degrees (k)", xaxt = "n", bty = "n", lwd = 2, main = paste("Trend",x))
    axis(side = 1, at = c(seq(4)))
    for (i in 2:length(clust_types[[x]]))
    {
        lines(mean_frame2[c(1:4) + (4 * (clust_types[[x]][i] - 1)), 1], type = "b", pch = 16, col = thepal[clust_types[[x]][i]], lwd = 2)
    }
    dev.off()
}