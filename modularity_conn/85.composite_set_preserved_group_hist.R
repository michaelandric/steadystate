## get histograms for preserved* and iters*
## preserved* == true SNSC between Highly ordered and Random across the group
## iters* == null SNSC between condition against itself in different modularity solutions 

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
gg1 <- read.table("preserved_group_median5p_20vxFltr_warped_median.out")$V1
gg2 <- read.table("iters_group_median5p_20vxFltr_warped_median.out")$V1
#newgg <- gg[!seq(length(gg)) %in% which(gg == 0 & ii == 0)]   # removing where both sets are 0 (a lot of zeros from the tlrc space)
#newii <- ii[!seq(length(ii)) %in% which(gg == 0 & ii == 0)]
newgg1 <- gg1[which(gg1 > 0 & gg1 < 777)]   # this filter is now outdated because none end up 777 after taking only those rows where at least half the participants had 777. It was typically that only 1 participant would have 777 at a given row (differeing between participants as to which row it was).
newgg2 <- gg2[which(gg2 > 0 & gg2 < 777)]
print(length(newgg1))
print(length(newgg2))

pdf("preserved_group_iters_hists_with20vxFltr_complete.out.pdf", paper = "USr", width = 11)
hist(newgg1, breaks = c(seq(0,1,.025)), main = "Preserved in Highly ordered and Random -- 20 vx filter", xlab = "SNSC")
hist(newgg2, breaks = c(seq(0,1,.025)), main = "Preserved null in same condition -- 20vx filter", xlab = "SNSC")
dev.off()

