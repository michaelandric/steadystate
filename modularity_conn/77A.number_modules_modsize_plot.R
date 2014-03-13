# assess the modularity values at different thresholds


### I have already written out 'uniqmods' to file via 77.number_modules_modsize_plot.R
### generating uniqmods (median number of modules from all iterations is the part that takes a while



subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
condition_names = c("A", "B", "D", "C")
#thresh <- 0.5   # this corresponds to a Pearson threshold but does not apply here since thresholding by links
thresholds <- c(15, 12, 8, 5)  #These are densities. % of complete graph
cutoff <- 1

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")

uniqmods <- read.table("uniqmods")$V1
condition_vec <- rep(rep(condition_names, 19), 4)
subjects_vec <- rep(rep(subjects, each=4), 4)
thresh_levels <- rep(thresholds, each = length(subjects) * length(conditions))
mod_score_frame <- data.frame(uniqmods, condition_vec, subjects_vec, thresh_levels)
colnames(mod_score_frame) <- c("modularity", "condition", "subject", "thresh")

error_vec <- c()
medians_mat <- matrix(nrow = length(thresholds), ncol = length(conditions))
for (t in 1:length(thresholds))
{
    medians_mat[t,] <- tapply(mod_score_frame$modularity, list(mod_score_frame$condition, mod_score_frame$thresh==thresholds[t]), median)[,2]   # This re-orders to "A, B, C, D" rather than "A, B, D, C"
    tmp <- subset(mod_score_frame, mod_score_frame$thresh == thresholds[t])
    for (i in conditions)
    {
        er <- sd(matrix(tmp$modularity, ncol = 4, byrow = T)[,i] - tapply(tmp$modularity, tmp$subject, mean)) / (sqrt(length(subjects)))
        error_vec <- c(error_vec, er)
    }
}
error_vec_mat = matrix(error_vec, nrow = length(conditions), byrow = T)

## aggregate.plot deconstructed for my own w/in person error bars
pdf("agplot_fromiters_linkthresh_number_modules.pdf")
aa = tapply(mod_score_frame$modularity, list(mod_score_frame$condition, mod_score_frame$thresh), median)
trans_medians <- t(apply(medians_mat, 2, rev))
trans_errs <- t(apply(error_vec_mat, 2, rev))
ylim <- c(0, 1.01 * max(aa + trans_errs) + 1)
ab = barplot(aa, beside = TRUE, ylim = ylim, ylab = "Median number of Modules")
segments(x0 = ab, x1 = ab, y0 = trans_medians, y1 = trans_medians + trans_errs)
segments(x0 = ab - .2, x1 = ab + .2, y0 = trans_medians + trans_errs, y1 = trans_medians + trans_errs)

bar.col <- grey.colors(length(levels(factor(list(mod_score_frame$condition, mod_score_frame$thresh)[[1]]))))
title("Number modules by graph density")
dev.off()

