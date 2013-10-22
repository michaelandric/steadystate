## assess normalized mutual information between two partitions
library(infotheo)

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

# This function derives the normalized mutual information
mi <- function(a, b)
{
    2*(mutinformation(a, b)) / (entropy(a) + entropy(b))
}

NMIvals <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep = ""))
    orig_coms <- as.matrix(read.table(list.files(pattern=paste("cleanTS.3.*.justcomm",sep=""))))
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/another/", sep = ""))
    another_coms <- as.matrix(read.table(list.files(pattern=paste("cleanTS.3.*.justcomm",sep=""))))
    NMIvals <- c(NMIvals, mi(orig_coms, another_coms))
}

print(NMIvals)
print(summary(NMIvals))
print(sd(NMIvals))

