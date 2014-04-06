## After using 78.*setmembers* to do 100 iterations of set consistency here creating a median representative
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

## "*_20vxFltr" refers to preserved filtered by modules with < 20 voxels

link_density <- "5p"
niters <- 100   # did 100 iterations

fltmedian <- function(x) if (777 %in% x) return(777) else return(median(x))   # function to keep row with value of 777 if it shows up in any row. 
fltmean <- function(x) if (777 %in% x) return(777) else return(mean(x))
# 777 is a randomly chosen numeric identifier that this voxel was in a module smaller than 20 voxels.
# Derived inputs for this script with 78.voxel_module_setmembers2.py

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity",link_density,"/set_consistency2/", sep = ""))
    ss_mat <- matrix(nrow = dim(read.table(paste("iter1_",ss,"_preserved.txt", sep = "")))[1], ncol = niters)
    for (i in 1:100)
    {
        ss_mat[,i] <- as.matrix(read.table(paste("iter",i,"_",ss,"_preserved.txt", sep = "")))
    }
    ss_median <- apply(ss_mat, 1, fltmedian)
    ss_average <- apply(ss_mat, 1, fltmean)
    write.table(ss_median, paste("preserved_",ss,"_median",link_density,"_20vxFltr.txt", sep = ""), row.names = F, col.names = F, quote = F)
    write.table(ss_average, paste("preserved_",ss,"_average",link_density,"_20vxFltr.txt", sep = ""), row.names = F, col.names = F, quote = F)
}

