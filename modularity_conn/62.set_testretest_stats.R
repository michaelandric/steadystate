## Get summary stat (mean, sd) for the preserved between orig and second run of modularity partitioning WMSC in Random condition
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

avgs <- c()
orig_mod <- c()
another_mod <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/another/", sep = ""))
    pr <- as.matrix(read.table(paste("preserved_",ss,"_another.txt", sep = "")))
    avgs <- c(avgs, mean(pr))
    orig_mod <- c(orig_mod, as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/mod_score.",ss,".Cond3.txt", sep = ""))))
    another_mod <- c(another_mod, as.matrix(read.table(paste("mod_score.",ss,".Cond3thresh_0.5.txt", sep = ""))))
}

print(length(avgs))
print(avgs)
print(summary(avgs))
print(sd(avgs))

print(cor(orig_mod, another_mod))
print(wilcox.test(orig_mod, another_mod, paired = T))


