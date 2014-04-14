## do a combined histogram
setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
gg1 <- read.table("preserved_group_median5p_20vxFltr_warped_median.out")$V1
gg2 <- read.table("iters_group_median5p_20vxFltr_warped_median.out")$V1
newgg1 <- gg1[which(gg1 > 0 & gg1 < 777)]
newgg2 <- gg2[which(gg2 > 0 & gg2 < 777)]

stck <- c(newgg1, newgg2)
snsc_frame <- data.frame(stck, c(rep("observed", length(newgg1)), rep("null", length(newgg2))))
colnames(snsc_frame) <- c("SNSC", "set")


library(ggplot2)
cbbPalette <- c("#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")
pdf("preserved_group_iters_hists_with20vxFltr_complete.out.Density.pdf", paper = "USr", width = 11)
qplot(SNSC, data = snsc_frame, geom = "density", fill = set, position = "stack") + scale_fill_manual(values = c("grey","black")) + theme(panel.background = element_rect(fill = "white", colour = "black"))
dev.off()

