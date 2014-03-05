# assess the modularity values at different thresholds
library(epicalc) # has "aggregate.plot"
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
condition_names = c("A", "B", "D", "C")
thresh <- 0.5   # this corresponds to a Pearson threshold but does not apply here since thresholding by links
thresholds <- c(15, 12, 8, 5)  #These are densities. % of complete graph


## THIS A BIT F'D UP BECAUSE I STARTED MODIFYING -- CHECK A PREVIOUS VERSION ON GIT
dat <- c()
for (t in 1:(length(thresholds)))
{
    for (ss in subjects)
    {
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/links_files",thresholds[t],"p/", sep=""))
        for (i in conditions)
        {
            dat <- c(dat, round(read.table(paste("mod_score.",ss,".",i,".",thresholds[t],"p_r",thresh,"_linksthresh_proportion.txt", sep=""))[[1]], 4))
        }
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")

condition_vec <- rep(rep(condition_names, 19), 4)
subjects_vec <- rep(rep(subjects, each=4), 4)
thresh_levels <- rep(thresholds, each = length(subjects) * length(conditions))
mod_score_frame <- data.frame(dat, condition_vec, subjects_vec, thresh_levels)
colnames(mod_score_frame) <- c("modularity", "condition", "subject", "thresh")

error_vec <- c()
means_mat <- matrix(nrow = length(thresholds), ncol = length(conditions))
for (t in 1:length(thresholds))
{
    means_mat[t,] <- colMeans(matrix(subset(mod_score_frame$modularity, mod_score_frame$thresh == thresholds[t]), nrow = 19, byrow = TRUE))
    #means_mat[t,] <- tapply(mod_score_frame$modularity, list(mod_score_frame$condition, mod_score_frame$thresh==thresholds[t]), mean)[,2]   # This re-orders to "A, B, C, D" rather than "A, B, D, C"
    tmp <- subset(mod_score_frame, mod_score_frame$thresh == thresholds[t])
    for (i in conditions)
    {
        er <- sd(matrix(tmp$modularity, ncol = 4, byrow = T)[,i] - tapply(tmp$modularity, tmp$subject, mean)) / (sqrt(length(subjects)))
        error_vec <- c(error_vec, er)
    }
}
error_vec_mat = matrix(error_vec, nrow = length(conditions), byrow = T)

## aggregate.plot deconstructed for my own w/in person error bars
pdf("agplot_linkthresh_mod_scores.pdf")
aa = tapply(mod_score_frame$modularity, list(mod_score_frame$condition, mod_score_frame$thresh), mean)
trans_means <- t(apply(means_mat[,c(1,2,4,3)], 2, rev))
trans_errs <- t(apply(error_vec_mat[,c(1,2,4,3)], 2, rev))
ylim <- c(0, 1.01 * max(aa + trans_errs))
ab = barplot(aa, beside = TRUE, ylim = ylim, ylab = "Modularity (Q)")
segments(x0 = ab, x1 = ab, y0 = trans_means, y1 = trans_means + trans_errs)
segments(x0 = ab - .2, x1 = ab + .2, y0 = trans_means + trans_errs, y1 = trans_means + trans_errs)

bar.col <- grey.colors(length(levels(factor(list(mod_score_frame$condition, mod_score_frame$thresh)[[1]]))))
#legend("topleft", levels(factor(list(mod_score_frame$condition, mod_score_frame$thresh)[[1]])), fill = bar.col, box.lwd = 0)
title("Modularity by graph density")
dev.off()

