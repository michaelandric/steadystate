## This accompanies 40.pwr_funcs.R
## It uses 'fitting*.txt' outputs from 40.pwr_funcs.R to do stats across the group
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
#subjects <- c("ANGO")
conditions <- seq(4)

library(RColorBrewer)
thepal = colorRampPalette(brewer.pal(9,"Set2"))(9)

dat_matA = matrix(nrow=length(subjects),ncol=4)
dat_matB = matrix(nrow=length(subjects),ncol=4)
dat_matG = matrix(nrow=length(subjects),ncol=4)
for (ss in 1:length(subjects))
{
    for (i in conditions)
    {
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",subjects[ss],"/corrTRIM_BLUR/",sep=""))
        dat_matA[ss,i] = as.numeric(strsplit(levels(read.delim(paste("fitting_cond",i,".txt",sep=""))[1,])[4]," ")[[1]][4]) ## this is for alpha
        dat_matB[ss,i] = as.numeric(strsplit(levels(read.delim(paste("fitting_cond",i,".txt",sep=""))[1,])[5]," ")[[1]][4]) ## this is for beta
        dat_matG[ss,i] = as.numeric(strsplit(levels(read.delim(paste("fitting_cond",i,".txt",sep=""))[1,])[6]," ")[[1]][4]) ## this is for gamma 
    }
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats")

friedmanA <- friedman.test(dat_matA)
friedmanB <- friedman.test(dat_matB)
friedmanG <- friedman.test(dat_matG)
print(friedmanA)
print(friedmanB)
print(friedmanG)

print(apply(dat_matA,2,median))
print(apply(dat_matB,2,median))
print(apply(dat_matG,2,median))
