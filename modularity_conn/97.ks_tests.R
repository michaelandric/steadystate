# test whether distributions are different

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

# test SNSC against null 
setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
gg1 <- read.table("preserved_group_median5p_20vxFltr_warped_median.out")$V1
gg2 <- read.table("iters_group_median5p_20vxFltr_warped_median.out")$V1
newgg1 <- gg1[which(gg1 > 0 & gg1 < 777)]
newgg2 <- gg2[which(gg2 > 0 & gg2 < 777)]

print(ks.test(newgg1, newgg2))

# construct vectors for adj rand index and nmi 
adjrand_btwn_all <- c()   # this is for all the upper.tri (unique pairs) values instead of just their mean
adjrand_1_all <- c()
nmi_btwn_all <- c()
nmi_1_all <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity5p/similarity_measures/", sep = ""))
    adjrand_btwn_mat <- as.matrix(read.table(paste("adjrands_mat_btwn.",ss,".txt", sep = "")))
    adjrand_btwn_all <- c(adjrand_btwn_all, c(adjrand_btwn_mat[upper.tri(adjrand_btwn_mat)]))
    adjrand_1_mat <- as.matrix(read.table(paste("adjrands_mat1.",ss,".txt", sep = "")))
    adjrand_1_all <- c(adjrand_1_all, c(adjrand_1_mat[upper.tri(adjrand_1_mat)]))
    nmi_btwn_mat <- (as.matrix(read.table(paste("nmi_mat_btwn.",ss,".txt", sep = ""))))
    nmi_btwn_all <- c(nmi_btwn_all, c(nmi_btwn_mat[upper.tri(nmi_btwn_mat)]))
    nmi_1_mat <- as.matrix(read.table(paste("nmi_mat1.",ss,".txt", sep = "")))
    nmi_1_all <- c(nmi_1_all, c(nmi_1_mat[upper.tri(nmi_1_mat)]))
}


# test adjusted Rand Index distribution against null
print(ks.test(adjrand_btwn_all, adjrand_1_all))
print(summary(adjrand_btwn_all))
print(summary(adjrand_1_all))
# test normalized mutual info against null
print(ks.test(nmi_btwn_all, nmi_1_all))
print(summary(nmi_btwn_all))
print(summary(nmi_1_all))

