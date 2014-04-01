## Get a representative image from the 2450 samples of every iteration against every other
## in the same condition (condition 1)
Args <- Sys.getenv("R_ARGS")
ss <- noquote(strsplit(Args," ")[[1]][1])

setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity5p/set_consistency/", sep = ""))

filelist <- list.files(pattern = glob2rx(paste("preserved_iters_*.txt", sep = "")))

link_density <- "5p"   # for now, just doing the 5% density
niters <- 2450   # this derives from doing 50*50 and removing the diagonal, setting this also gives a check that there are 2450 files. 'for' loop should break if not. 
ss_mat <- matrix(nrow = dim(read.table(paste("preserved_iters_1_2_",ss,".txt", sep = "")))[1], ncol = niters)

for (i in 1:niters)
{
    ss_mat[,i] <- as.matrix(read.table(filelist[i]))
}

iters_median <- apply(ss_mat, 1, median)
iters_average <- apply(ss_mat, 1, mean)

ss_median <- as.matrix(read.table(paste("preserved_",ss,"_median",link_density,".txt", sep = "")))
ss_average <- as.matrix(read.table(paste("preserved_",ss,"_average",link_density,".txt", sep = "")))

diff_median <- ss_median - iters_median
diff_average <- ss_average - iters_average

write.table(diff_median, paste("preserved_diff_",ss,"_median",link_density,".txt", sep = ""), row.names = F, col.names = F, quote = F)
write.table(diff_average, paste("preserved_diff_",ss,"_average",link_density,".txt", sep = ""), row.names = F, col.names = F, quote = F)

