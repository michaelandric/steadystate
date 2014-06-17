## get similarity metric between partitions

## previously did 63.mutuInfo.R, but that looks whether two consecutive modularity solutions on same mat aggree.
## this is a more thorough look, over the 100 iterations

Args <- Sys.getenv("R_ARGS")
subj <- noquote(strsplit(Args," ")[[1]][1])

library(igraph)

combinations <- combn(100, 2)
setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",subj,"/modularity5p/", sep = ""))
N <- dim(read.table(paste("iter1.",subj,".1.5p_r0.5_linksthresh_proportion.out.maxlevel_tree", sep = "")))[1]
#cond <- 1


for (cond in c(1,3))
{ 
    tree_iters_mat <- matrix(nrow = N, ncol = 100)
    for (i in seq(100))
    {
        tree_iters_mat[,i] <- as.matrix(read.table(paste("iter",i,".",subj,".",cond,".5p_r0.5_linksthresh_proportion.out.maxlevel_tree", sep = ""))$V2)
    }
    assign(paste("tree_iters_mat",cond, sep = ""), tree_iters_mat)


    adjrands <- c()
    adjrands_mat <- matrix(c(rep(0, 100*100)), nrow = 100)
    nmi_vals <- c()
    nmi_mat <- matrix(c(rep(0, 100*100)), nrow = 100)
    for (i in seq(dim(combinations)[2]))
    {
        rw <- combinations[,i][1]
        cl <- combinations[,i][2]
        rw_cl_adjrand <- compare(get(paste("tree_iters_mat",cond, sep = ""))[,rw], get(paste("tree_iters_mat",cond, sep = ""))[,cl], method = "adjusted.rand")
        adjrands <- c(adjrands, rw_cl_adjrand)
        adjrands_mat[rw,cl] <- rw_cl_adjrand
        adjrands_mat[cl,rw] <- rw_cl_adjrand
        rw_cl_nmi <- compare(get(paste("tree_iters_mat",cond, sep = ""))[,rw], get(paste("tree_iters_mat",cond, sep = ""))[,cl], method = "nmi")
        nmi_vals <- c(nmi_vals, rw_cl_nmi)
        nmi_mat[rw,cl] <- rw_cl_nmi
        nmi_mat[cl,rw] <- rw_cl_nmi
    }
    assign(paste("adjrands",cond, sep = ""), adjrands)
    assign(paste("adjrands_mat",cond, sep = ""), adjrands_mat)
    write.table(round(get(paste("adjrands_mat",cond, sep = "")), 3), paste("similarity_measures/adjrands_mat",cond,".",subj,".txt", sep = ""), row.names = F, col.names = F, quote = F)   # adjusted rand index
    assign(paste("nmi_vals",cond, sep = ""), nmi_vals)
    assign(paste("nmi_mat",cond, sep = ""), nmi_mat)
    write.table(round(get(paste("nmi_mat",cond, sep = "")), 3), paste("similarity_measures/nmi_mat",cond,".",subj,".txt", sep = ""), row.names = F, col.names = F, quote = F)   # normalized mutual information
}



## Now looking at these metrics between conditions
adjrands_btwn <- c()
adjrands_mat_btwn <- matrix(c(rep(0, 100*100)), nrow = 100)
nmi_vals_btwn <- c()
nmi_mat_btwn <- matrix(c(rep(0, 100*100)), nrow = 100)
for (i in seq(dim(combinations)[2]))
{
    rw <- combinations[,i][1]
    cl <- combinations[,i][2]
    rw_cl_adjrand_btwn <- compare(tree_iters_mat1[,rw], tree_iters_mat3[,cl], method = "adjusted.rand")
    adjrands_btwn <- c(adjrands_btwn, rw_cl_adjrand_btwn)
    adjrands_mat_btwn[rw,cl] <- rw_cl_adjrand_btwn
    adjrands_mat_btwn[cl,rw] <- rw_cl_adjrand_btwn
    rw_cl_nmi_btwn <- compare(tree_iters_mat1[,rw], tree_iters_mat3[,cl], method = "nmi")
    nmi_vals_btwn <- c(nmi_vals_btwn, rw_cl_nmi_btwn)
    nmi_mat_btwn[rw,cl] <- rw_cl_nmi_btwn
    nmi_mat_btwn[cl,rw] <- rw_cl_nmi_btwn
}
write.table(round(adjrands_mat_btwn, 3), paste("similarity_measures/adjrands_mat_btwn.",subj,".txt", sep = ""), row.names = F, col.names = F, quote = F)   # adjusted rand index
write.table(round(nmi_mat_btwn, 3), paste("similarity_measures/nmi_mat_btwn.",subj,".txt", sep = ""), row.names = F, col.names = F, quote = F)   # adjusted rand index

