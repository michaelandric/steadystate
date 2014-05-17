## Determine whether SNSC correlates with Degrees

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

cor_values1 <- c()
cor_values3 <- c()
for (ss in subjects)
{
    d1 <- as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/links_files5p/",ss,".1.5p_linksthresh_proportion.degrees_gray", sep = "")))   # these are the degrees
    d3 <- as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/links_files5p/",ss,".3.5p_linksthresh_proportion.degrees_gray", sep = "")))   # these are the degrees
    snsc_with_filtvals <- as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity5p/set_consistency2/preserved_",ss,"_median5p_20vxFltr.txt", sep = "")))
    print(c(ss, length(which(snsc_with_filtvals == 777)), round(length(which(snsc_with_filtvals == 777))/length(snsc_with_filtvals),3)))
    snsc <- snsc_with_filtvals
    snsc[which(snsc_with_filtvals == 777)] = NA
    cor_values1 <- c(cor_values1, cor(snsc, d1, use = "complete.obs")[[1]])
    cor_values3 <- c(cor_values3, cor(snsc, d3, use = "complete.obs")[[1]])
    print(c(cor.test(snsc,d1)$p.value, cor.test(snsc,d3)$p.value))
}

print(t.test(atanh(cor_values1)))   # fisher transform correlation values & test significance against 'Highly ordered' condition degrees
print(t.test(atanh(cor_values3)))   # fisher transform correlation values & test significance against 'Random' condition degrees

