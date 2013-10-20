## Get summary stat (mean, sd) for the preserved between orig and second run of modularity partitioning WMSC in Random condition
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

avgs <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/another/", sep = ""))
    pr <- as.matrix(read.table(paste("preserved_",ss,"_another.txt", sep = "")))
    avgs <- c(avgs, mean(pr))   
}

print(length(avgs))
print(avgs)
print(summary(avgs))
print(sd(avgs))

