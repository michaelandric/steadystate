## get histograms for preserved* and iters*
## preserved* == true SNSC between Highly ordered and Random across the group
## iters* == null SNSC between condition against itself in different modularity solutions 

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
gg <- read.table("preserved_group_median5p_warped_median.txt")$V1
ii <- read.table("iters_group_median5p_warped_median.txt")$V1
newgg <- gg[!seq(length(gg)) %in% which(gg == 0 & ii == 0)]   # removing where both sets are 0 (a lot of zeros from the tlrc space)
newii <- ii[!seq(length(ii)) %in% which(gg == 0 & ii == 0)]

pdf("preserved_group_iters_hists.pdf", paper = "USr", width = 11)
hist(newgg, breaks = c(seq(0,1,.025)), main = "Preserved between Highly ordered and Random", xlab = "SNSC")
hist(newii, breaks = c(seq(0,1,.025)), main = "Within condition (null)", xlab = "SNSC")
dev.off()

