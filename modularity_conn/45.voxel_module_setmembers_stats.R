## analyze proprotion remains in modules by voxels
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

ss_means <- c()
mod_means_tot <- c()
mod_vox_count_tot <- c()
for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR",sep=""))
    dat3 <- as.matrix(read.table(list.files(pattern=paste("cleanTS.3.*.justcomm",sep=""))))
    dat1 <- as.matrix(read.table(list.files(pattern=paste("cleanTS.1.*.justcomm",sep=""))))
    pres <- as.matrix(read.table(paste("preserved_",ss,".txt",sep="")))
    mod_presr_means <- c()
    mod_vox_count <- c()
    for (i in unique(dat3))
    {
        mod_presr_means <- c(mod_presr_means, mean(pres[which(dat3==i)]))
        mod_vox_count <- c(mod_vox_count, length(which(dat3==i)))
    }
    mod_means_tot <- c(mod_means_tot, mod_presr_means)
    mod_vox_count_tot <- c(mod_vox_count_tot, mod_vox_count)
#    ss_means <- c(ss_means, weighted.mean(mod_presr_means, mod_vox_count))
    ss_means <- c(ss_means, weighted.mean(mod_presr_means[which(mod_vox_count >2 )], mod_vox_count[which(mod_vox_count>2)])) ## ignore 1 voxel modules
}

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats/")
print(ss_means)
print(summary(ss_means)) 

pdf(file="preserved_hists.pdf", paper="USr",width=11)
par(mfrow=c(1,2))
hist(mod_means_tot, breaks=length(mod_means_tot)/4, col="orange")
hist(mod_means_tot[which(mod_vox_count_tot > 2)], breaks=length(mod_means_tot[which(mod_vox_count_tot > 2)]) / 4, col="yellow")
hist(mod_means_tot[which(mod_vox_count_tot > 64)], breaks=length(mod_means_tot[which(mod_vox_count_tot > 64)]) / 4, col="magenta1")
hist(mod_means_tot[which(mod_vox_count_tot > 100)], breaks=length(mod_means_tot[which(mod_vox_count_tot > 100)]) / 4, col="dodgerblue")
dev.off()


fh <- hist(mod_means_tot[which(mod_vox_count_tot > 2)], breaks=length(mod_means_tot[which(mod_vox_count_tot > 2)]) / 4, col="yellow", plot=F)
#aggregate(mod_vox_count_tot, list(cut(mod_means_tot, fh$breaks, labels=FALSE)), mean)
#which(!seq(43) %in% b)
mm=matrix(nrow=length(fh$counts),ncol=3)
med_ag = aggregate(mod_vox_count_tot[which(mod_vox_count_tot > 2)], list(cut(mod_means_tot[which(mod_vox_count_tot > 2)], fh$breaks, labels=FALSE)), median)
#med_ag = aggregate(mod_vox_count_tot, list(cut(mod_means_tot, fh$breaks, labels=FALSE)), median)
mm[,1] = fh$counts
mm[med_ag$Group.1,2] = med_ag$x

library(RColorBrewer)
thepal=colorRampPalette(brewer.pal(9,"YlGnBu"))(length(mm[,1]))
#pdf("preserved_hist2.pdf", paper="USr",width=11)
#b=barplot(mm[,1],names.arg=fh$breaks[-1],ylim=c(min(mm[,1]), max(mm[,1])+5), col=thepal, main="Proportion preserved in Highly Ordered and Random",sub="(with median module size in voxels above each bin)")
pdf("preserved_hist2BW.pdf", paper="USr",width=11)
b=barplot(mm[,1],names.arg=fh$breaks[-1],ylim=c(min(mm[,1]), max(mm[,1])+5), main="Proportion preserved in Highly Ordered and Random", ylab="Count module averages" )
#text(x=b, mm[,1]+1, as.character(mm[,2]),srt=90, cex=.75)
b2=barplot(mm[,2],names.arg=fh$breaks[-1], main="Median module size for bins in proportion preserved in Highly Ordered and Random", ylab="Median module size in voxels")
dev.off()

