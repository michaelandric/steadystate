##generate histograms for each person in each condition.
##average histograms across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
br = 100
c1_mat <- matrix(nrow=length(subjects),ncol=br)
c2_mat <- matrix(nrow=length(subjects),ncol=br)
c4_mat <- matrix(nrow=length(subjects),ncol=br)
c3_mat <- matrix(nrow=length(subjects),ncol=br)
library(RColorBrewer)
thepal = colorRampPalette(brewer.pal(4,"RdPu"))(4)

n=1
for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR",sep=""))
    dat <- c()
    for (i in conditions)
    {
        dat <- c(dat, as.matrix(read.table(paste(ss,".",i,".degrees_gray",sep=""))))
    }
    dat_matrix <- matrix(dat, ncol=4)
    pdf(file=paste("degree_histograms_",ss,".pdf",sep=""))
    par(mfrow=c(2,2))
    c1 = hist(rank(dat_matrix[,1])/dim(dat_matrix)[1],breaks=br,col=thepal[1],main="Highly ordered",xlab="Rank %")$counts
    c2 = hist(rank(dat_matrix[,2])/dim(dat_matrix)[1],breaks=br,col=thepal[2],main="Some order",xlab="Rank %")$counts
    c4 = hist(rank(dat_matrix[,4])/dim(dat_matrix)[1],breaks=br,col=thepal[3],main="Almost random",xlab="Rank %")$counts
    c3 = hist(rank(dat_matrix[,3])/dim(dat_matrix)[1],breaks=br,col=thepal[4],main="Random",xlab="Rank %")$counts
    dev.off()
    c1_mat[n,] <- c1
    c2_mat[n,] <- c2
    c4_mat[n,] <- c4
    c3_mat[n,] <- c3
    n = n+1
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
print(getwd())

pdf(file="degree_avg_histograms.pdf")
par(mfrow=c(2,2))
barplot(colMeans(c1_mat),col=thepal[1],xlab="Rank %",ylab="Average Count Freq",main="Highly ordered")
barplot(colMeans(c2_mat),col=thepal[2],xlab="Rank %",ylab="Average Count Freq",main="Some order")
barplot(colMeans(c4_mat),col=thepal[3],xlab="Rank %",ylab="Average Count Freq",main="Almost random")
barplot(colMeans(c3_mat),col=thepal[4],xlab="Rank %",ylab="Average Count Freq",main="Random")
dev.off()

