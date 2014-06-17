## previous code (95.partition_similarity) used to get the partition similarity via adjusted rand index and normalized mutual info

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

adjrand_btwn <- c()
adjrand_btwn_all <- c()   # this is for all the upper.tri (unique pairs) values instead of just their mean
adjrand_1 <- c()
adjrand_1_all <- c()
adjrand_3 <- c()
nmi_btwn <- c()
nmi_btwn_all <- c()   # like above, this is for all unique values, instead of just the mean
nmi_1 <- c()
nmi_1_all <- c()
nmi_3 <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity5p/similarity_measures/", sep = ""))
    nmi_btwn_mat <- (as.matrix(read.table(paste("nmi_mat_btwn.",ss,".txt", sep = ""))))
    nmi_btwn <- c(nmi_btwn, mean(nmi_btwn_mat[upper.tri(nmi_btwn_mat)]))
    nmi_btwn_all <- c(nmi_btwn_all, c(nmi_btwn_mat[upper.tri(nmi_btwn_mat)]))
    nmi_1_mat <- as.matrix(read.table(paste("nmi_mat1.",ss,".txt", sep = "")))
    nmi_1 <- c(nmi_1, mean(nmi_1_mat[upper.tri(nmi_1_mat)]))
    nmi_1_all <- c(nmi_1_all, c(nmi_1_mat[upper.tri(nmi_1_mat)]))
    nmi_3_mat <- as.matrix(read.table(paste("nmi_mat3.",ss,".txt", sep = "")))
    nmi_3 <- c(nmi_3, mean(nmi_3_mat[upper.tri(nmi_3_mat)]))
    adjrand_btwn_mat <- as.matrix(read.table(paste("adjrands_mat_btwn.",ss,".txt", sep = "")))
    adjrand_btwn <- c(adjrand_btwn, mean(adjrand_btwn_mat[upper.tri(adjrand_btwn_mat)]))
    adjrand_btwn_all <- c(adjrand_btwn_all, c(adjrand_btwn_mat[upper.tri(adjrand_btwn_mat)]))
    adjrand_1_mat <- as.matrix(read.table(paste("adjrands_mat1.",ss,".txt", sep = "")))
    adjrand_1 <- c(adjrand_1, mean(adjrand_1_mat[upper.tri(adjrand_1_mat)]))
    adjrand_1_all <- c(adjrand_1_all, c(adjrand_1_mat[upper.tri(adjrand_1_mat)]))
    adjrand_3_mat <- as.matrix(read.table(paste("adjrands_mat3.",ss,".txt", sep = "")))
    adjrand_3 <- c(adjrand_3, mean(adjrand_3_mat[upper.tri(adjrand_3_mat)]))
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
print(summary(adjrand_btwn))
print(summary(adjrand_1))
print(summary(adjrand_3))
print(t.test(adjrand_btwn, adjrand_1, paired = T))
print(t.test(adjrand_btwn, adjrand_3, paired = T))

print(summary(nmi_btwn))
print(summary(nmi_1))
print(summary(nmi_3))
print(t.test(nmi_btwn, nmi_1, paired = T))
print(t.test(nmi_btwn, nmi_3, paired = T))

## This section is playing with empirical cumulative distribution function representation
#ecdf.adjrand_btwn <- ecdf(adjrand_btwn)
#ecdf.adjrand_1 <- ecdf(adjrand_1)
#ecdf.adjrand_3 <- ecdf(adjrand_3)
#ecdf.nmi_btwn <- ecdf(nmi_btwn)
#ecdf.nmi_1 <- ecdf(nmi_1)
#ecdf.nmi_3 <- ecdf(nmi_3)
#plot(ecdf.adjrand_btwn, verticals = T, pch = 46, lwd = 2, xlim = c(0,1), col = "seagreen", xlab = "Similarity measure")
#lines(ecdf.adjrand_1, verticals = T, pch = 46, lwd = 2, col = "palegreen2")
#lines(ecdf.nmi_btwn, verticals = T, pch = 46, lwd = 2, col = "navy")
#lines(ecdf.nmi_1, verticals = T, pch = 46, lwd = 2, col = "skyblue")

#sim_frame <- data.frame(c(adjrand_btwn, adjrand_1), c(rep("Between_conditions", length(adjrand_btwn)), rep("Same_condition", length(adjrand_1))))
sim_frame <- data.frame(c(adjrand_btwn_all, adjrand_1_all), c(rep("Between_conditions", length(adjrand_btwn_all)), rep("Same_condition", length(adjrand_1_all))))
colnames(sim_frame) <- c("AdjRandIndex", "set")
sim_frame2 <- data.frame(c(nmi_btwn_all, nmi_1_all), c(rep("Between_conditions", length(nmi_btwn_all)), rep("Same_condition", length(nmi_1_all))))
colnames(sim_frame2) <- c("NMI", "set")

library(ggplot2)
#cbbPalette <- c("#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")
pdf("preserved_similarity_measures_group.Density.pdf", paper = "USr", width = 11)
qplot(AdjRandIndex, data = sim_frame, geom = "density", fill = set, position = "stack", xlab = "Adjusted Rand Index") + scale_fill_manual(values = c("grey","black")) + theme(panel.background = element_rect(fill = "white", colour = "black"))
qplot(NMI, data = sim_frame2, geom = "density", fill = set, position = "stack", xlab = "Normalized Mutual Info") + scale_fill_manual(values = c("grey","black")) + theme(panel.background = element_rect(fill = "white", colour = "black"))
dev.off()


