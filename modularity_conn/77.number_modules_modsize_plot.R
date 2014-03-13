# assess the modularity values at different thresholds
library(epicalc) # has "aggregate.plot"
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
condition_names = c("A", "B", "D", "C")
#thresh <- 0.5   # this corresponds to a Pearson threshold but does not apply here since thresholding by links
thresholds <- c(15, 12, 8, 5)  #These are densities. % of complete graph
cutoff <- 1


#dat <- c()
uniqmods <- c()
for (t in 1:(length(thresholds)))
{
    for (ss in subjects)
    {
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity",thresholds[t],"p/", sep = ""))
        for (i in conditions)
        {
            #modscores <- c()
            #filelist = list.files(pattern = glob2rx(paste("*",ss,".",i,"*.Qval", sep = "")))
            filelist = list.files(pattern = glob2rx(paste("*",ss,".",i,"*.maxlevel_tree", sep = "")))
            imods <- c()
            for (ff in filelist)
            {
                ffdat <- as.matrix(read.table(ff))
                nn <- length(aggregate(ffdat[,2], list(ffdat[,2]), length)[,1][aggregate(ffdat[,2], list(ffdat[,2]), length)$x > cutoff])
                imods <- c(imods, nn)
                #modscores <- c(modscores, as.matrix(read.table(f)))
            }
            uniqmods <- c(uniqmods, median(imods))
            #dat <- c(dat, sort(modscores)[51])
        }
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")

condition_vec <- rep(rep(condition_names, 19), 4)
subjects_vec <- rep(rep(subjects, each=4), 4)
thresh_levels <- rep(thresholds, each = length(subjects) * length(conditions))
#mod_score_frame <- data.frame(dat, condition_vec, subjects_vec, thresh_levels)
mod_score_frame <- data.frame(uniqmods, condition_vec, subjects_vec, thresh_levels)
colnames(mod_score_frame) <- c("modularity", "condition", "subject", "thresh")

error_vec <- c()
#means_mat <- matrix(nrow = length(thresholds), ncol = length(conditions))
#for (t in 1:length(thresholds))
#{
#    means_mat[t,] <- colMeans(matrix(subset(mod_score_frame$modularity, mod_score_frame$thresh == thresholds[t]), nrow = 19, byrow = TRUE))
    #means_mat[t,] <- tapply(mod_score_frame$modularity, list(mod_score_frame$condition, mod_score_frame$thresh==thresholds[t]), mean)[,2]   # This re-orders to "A, B, C, D" rather than "A, B, D, C"
#    tmp <- subset(mod_score_frame, mod_score_frame$thresh == thresholds[t])
#    for (i in conditions)
#    {
#        er <- sd(matrix(tmp$modularity, ncol = 4, byrow = T)[,i] - tapply(tmp$modularity, tmp$subject, mean)) / (sqrt(length(subjects)))
#        error_vec <- c(error_vec, er)
#    }
#}
#error_vec_mat = matrix(error_vec, nrow = length(conditions), byrow = T)

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
#aa = tapply(mod_score_frame$modularity, list(mod_score_frame$condition, mod_score_frame$thresh), mean)
aa = tapply(mod_score_frame$modularity, list(mod_score_frame$condition, mod_score_frame$thresh), median)
#trans_means <- t(apply(means_mat[,c(1,2,4,3)], 2, rev))
trans_medians <- t(apply(medians_mat[,c(1,2,3,4)], 2, rev))
trans_errs <- t(apply(error_vec_mat[,c(1,2,3,4)], 2, rev))
ylim <- c(0, 1.01 * max(aa + trans_errs))
ab = barplot(aa, beside = TRUE, ylim = ylim, ylab = "Number of Modules")
#segments(x0 = ab, x1 = ab, y0 = trans_means, y1 = trans_means + trans_errs)
segments(x0 = ab, x1 = ab, y0 = trans_medians, y1 = trans_medians + trans_errs)
#segments(x0 = ab - .2, x1 = ab + .2, y0 = trans_means + trans_errs, y1 = trans_means + trans_errs)
segments(x0 = ab - .2, x1 = ab + .2, y0 = trans_medians + trans_errs, y1 = trans_medians + trans_errs)

bar.col <- grey.colors(length(levels(factor(list(mod_score_frame$condition, mod_score_frame$thresh)[[1]]))))
#legend("topleft", levels(factor(list(mod_score_frame$condition, mod_score_frame$thresh)[[1]])), fill = bar.col, box.lwd = 0)
title("Modularity by graph density")
dev.off()

