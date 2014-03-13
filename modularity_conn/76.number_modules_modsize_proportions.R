# Get module size proportions

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
densities <- c("5p", "8p", "12p", "15p")
vox_nums <- read.table("/mnt/tier2/urihas/Andric/steadystate/codebase/procedures/subject_graymattermask_voxnum.txt")

setwd("/mnt/tier2/urihas/Andric/steadystate/groupstats")
print(getwd())

for (de in densities)
{
    print(paste("GRAPH LINK DENSITY ",de, sep = ""))
    out <- c()
    nummods <- read.table(paste("number_modules_frame",de,"_fromiters2.txt", sep = ""), header = T)
    for (ss in subjects)
    {
        a = subset(nummods, nummods$subject == ss)$alliter_mean_modsizes / vox_nums[,2][vox_nums[,1]==ss]
        out <- c(out, a)
    }
    out_df <- data.frame(matrix(out, nrow = length(subjects), byrow = T), subjects)
    colnames(out_df) <- c("cond1", "cond2", "cond3", "cond4", "subjects")
    print(out_df)
    print("Mean proportion of median/mean (check code) module size at each condition:")
    print(apply(matrix(out, nrow = length(subjects), byrow = T), 2, mean))
    print("Median proportion of median/mean (check code) module size at each condition:")
    print(apply(matrix(out, nrow = length(subjects), byrow = T), 2, median))
    print(friedman.test(matrix(out, nrow = length(subjects), byrow = T)))
}

