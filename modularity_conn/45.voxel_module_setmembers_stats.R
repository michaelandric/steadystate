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


