# Make modularity bar graphs with proper within-subject error bars
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
condition_names = c("Highly ordered", "Some order", "Random", "Almost Random")

library(RColorBrewer)
thepal = colorRampPalette(brewer.pal(9,"YlGnBu"))(9)[1,3,5,7]

dat_orig <- c()
for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep=""))
    for (i in conditions)
    {
        dat_orig <- c(dat_orig, round(read.table(paste("mod_score.",ss,".Cond",i,".txt", sep=""))[[1]], 4))
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats")

condition_vec <- rep(condition_names, 19)
subjects_vec <- rep(subjects, each=4)
mod_score_frame <- data.frame(dat_orig, condition_vec, subjects_vec)
colnames(mod_score_frame) <- c("modularity", "condition", "subject")

tmp <- mod_score_frame
error_vec <- c()
for (i in conditions)
{
    er <- sd(matrix(tmp$modularity, ncol = 4, byrow = T)[,i] - tapply(tmp$modularity, tmp$subject, mean)) / (sqrt(length(subjects)))
    error_vec <- c(error_vec, er)   # These end up same order as condition_names ("Highly ordered, Some order, Random, Almost Random")
}

par(mfrow = c(1,2))
aa <- tapply(mod_score_frame$modularity, list(mod_score_frame$condition), mean)   # This gives alphabetical ("Almost random", "Highly ordered", "Some order", "Random")
ylim <- c(0, 1.01 * max(aa + error_vec))
aa_ordered <- aa[c(2, 4, 1, 3)]
error_vec_ordered <- error_vec[c(1, 2, 4, 3)]

thepal = colorRampPalette(brewer.pal(9,"Blues"))(9)[c(7, 5, 3, 1)]
#bar.col <- grey.colors(length(levels(factor(list(mod_score_frame$condition)[[1]]))))  # alternative (removal of) colors
pdf("modularity_bargraph.pdf")
ab <- barplot(aa_ordered, beside = TRUE, ylim = ylim, ylab = "Modularity (Q)", col = thepal)
segments(x0 = ab, x1 = ab, y0 = aa_ordered, y1 = aa_ordered + error_vec_ordered)
segments(x0 = ab - .2, x1 = ab + .2, y0 = aa_ordered + error_vec_ordered, y1 = aa_ordered + error_vec_ordered)
dev.off()