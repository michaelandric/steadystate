## assess normalized mutual information between two partitions
library(infotheo)

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

# This function derives the normalized mutual information
mi <- function(a, b)
{
    2*(mutinformation(a, b)) / (entropy(a) + entropy(b))
}

NMIvals <- c()
avgs <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep = ""))
    orig_coms <- as.matrix(read.table(list.files(pattern=paste("cleanTS.3.*.justcomm",sep=""))))
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/another/", sep = ""))
    another_coms <- as.matrix(read.table(list.files(pattern=paste("cleanTS.3.*.justcomm",sep=""))))
    NMIvals <- c(NMIvals, mi(orig_coms, another_coms))

    pr <- as.matrix(read.table(paste("preserved_",ss,"_another.txt", sep = "")))   # also now getting the preserved to compare with WMSC
    avgs <- c(avgs, mean(pr))
}

print(NMIvals)
print(summary(NMIvals))
print(sd(NMIvals))

print(avgs)
print(summary(avgs))
print(sd(avgs))

print(cor(NMIvals, avgs))

