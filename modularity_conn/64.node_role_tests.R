# find whether number of voxels with a certain role differ
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

for (role in seq(7))
{
    ss_role <- c()
    print(" -------------------------------------------- ")
    print(paste("THE ROLE IS",role))

    for (ss in subjects)
    {
        ss_table <- as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/",ss,"_roletable.txt", sep="")))
        for (i in conditions)
        {
            ss_role <- c(ss_role, ss_table[role, i])
        }
    }

    grp_mat <- matrix(ss_role, nrow = length(subjects), byrow = TRUE)
    print(grp_mat)
    print(apply(grp_mat, 2, sum))
    print(apply(grp_mat, 2, median))
    print(friedman.test(grp_mat))
    print(wilcox.test(grp_mat[,1], grp_mat[,3], paired = TRUE))
}

