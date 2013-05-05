##generate histograms for each person in each condition.
##average histograms across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
br = seq(0.01,1,.01)
c1_mat <- matrix(nrow=length(subjects),ncol=length(br))
c2_mat <- matrix(nrow=length(subjects),ncol=length(br))
c4_mat <- matrix(nrow=length(subjects),ncol=length(br))
c3_mat <- matrix(nrow=length(subjects),ncol=length(br))
library(RColorBrewer)
thepal = colorRampPalette(brewer.pal(9,"Set2"))(9)

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
    tmp1 <- findInterval(rank(sort(dat_matrix[,1]))/dim(dat_matrix)[1], br)
    tmp2 <- findInterval(rank(sort(dat_matrix[,2]))/dim(dat_matrix)[1], br)
    tmp4 <- findInterval(rank(sort(dat_matrix[,4]))/dim(dat_matrix)[1], br)
    tmp3 <- findInterval(rank(sort(dat_matrix[,3]))/dim(dat_matrix)[1], br)
    an1 <- c()
    an2 <- c()
    an4 <- c()
    an3 <- c()
    for (i in seq(100))
    {
        an1 = c(an1, mean(sort(dat_matrix[,1])[which(tmp1==i)]))
        an2 = c(an2, mean(sort(dat_matrix[,2])[which(tmp2==i)]))
        an4 = c(an4, mean(sort(dat_matrix[,4])[which(tmp4==i)]))
        an3 = c(an3, mean(sort(dat_matrix[,3])[which(tmp3==i)]))
    }
    x1=seq(100)[which(!is.na(an1))]
    x2=seq(100)[which(!is.na(an2))]
    x4=seq(100)[which(!is.na(an4))]
    x3=seq(100)[which(!is.na(an3))]

    pdf(file=paste("degree_plots_",ss,".pdf",sep=""))
    par(mfrow=c(2,2))
    plot(x1,sort(an1,decreasing=T), col=thepal[1],lwd=2, type="b", cex=.5, main="Highly ordered",xlab="Rank %") 
    plot(x2,sort(an2,decreasing=T), col=thepal[2],lwd=2, type="b", cex=.5, main="Some order",xlab="Rank %") 
    plot(x4,sort(an4,decreasing=T), col=thepal[3],lwd=2, type="b", cex=.5, main="Almost random",xlab="Rank %") 
    plot(x3,sort(an3,decreasing=T), col=thepal[4],lwd=2, type="b", cex=.5, main="Random",xlab="Rank %") 
    dev.off()
    c1_mat[n,] <- an1
    c2_mat[n,] <- an2
    c4_mat[n,] <- an4
    c3_mat[n,] <- an3
    n = n+1
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
print(getwd())

cc1=colMeans(c1_mat,na.rm=T)
cc2=colMeans(c2_mat,na.rm=T)
cc4=colMeans(c4_mat,na.rm=T)
cc3=colMeans(c3_mat,na.rm=T)
pdf(file="degree_plot.pdf")
plot(sort(cc1,decreasing=T), type="b", ylim=range(cc1,cc2,cc3,cc4),col=thepal[1])
points(sort(cc2,decreasing=T), type="b", col=thepal[2])
points(sort(cc4,decreasing=T), type="b", col=thepal[3])
points(sort(cc3,decreasing=T), type="b", col=thepal[4])
legend("topright",legend=c("Highly ordered","Some order", "Almost random", "Random"),pch=15,col=c(thepal[1:4]))
dev.off()
pdf(file="degree_avg_barplots.pdf")
par(mfrow=c(2,2))
barplot(sort(colMeans(c1_mat,na.rm=T),decreasing=T),col=thepal[1],xlab="Rank %",ylab="Average Count Freq",main="Highly ordered")
barplot(sort(colMeans(c2_mat,na.rm=T),decreasing=T),col=thepal[2],xlab="Rank %",ylab="Average Count Freq",main="Some order")
barplot(sort(colMeans(c4_mat,na.rm=T),decreasing=T),col=thepal[3],xlab="Rank %",ylab="Average Count Freq",main="Almost random")
barplot(sort(colMeans(c3_mat,na.rm=T),decreasing=T),col=thepal[4],xlab="Rank %",ylab="Average Count Freq",main="Random")
dev.off()

