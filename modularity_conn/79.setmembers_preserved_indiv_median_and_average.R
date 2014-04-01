## After using 78.*setmembers* to do 100 iterations of set consistency here creating a median representative
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

link_density <- "5p"
niters <- 100   # did 100 iterations

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity",link_density,"/set_consistency/", sep = ""))
    ss_mat <- matrix(nrow = dim(read.table(paste("iter1_",ss,"_preserved.txt", sep = "")))[1], ncol = niters)
    for (i in 1:100)
    {
        ss_mat[,i] <- as.matrix(read.table(paste("iter",i,"_",ss,"_preserved.txt", sep = "")))
    }
    ss_median <- apply(ss_mat, 1, median)
    ss_average <- apply(ss_mat, 1, mean)
    write.table(ss_median, paste("preserved_",ss,"_median",link_density,".txt", sep = ""), row.names = F, col.names = F, quote = F)
    write.table(ss_average, paste("preserved_",ss,"_average",link_density,".txt", sep = ""), row.names = F, col.names = F, quote = F)
}

