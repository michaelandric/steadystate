## LOOK AT NUMBER OF MODULES IN TWO WAYS:
## 1. CORRESPONDS TO THE TREE IN THE QVAL ANALYSIS 
## 2. CORRESPONDS TO A MEDIAN NUMBER OF MODULES OVER ALL ITERATIONS FOR EACH

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
cutoff <- 1
densities <- c("5p", "8p", "12p", "15p")

for (de in densities)
{   # graph links density
    num_mods <- c()
    uniqmods <- c()
    tree_modsizes_means <- c()
    tree_modsizes_medians <- c()
    modsizes_means <- c()
    modsizes_medians <- c()
    #stddev_data <- c()
    subject_frame <- c()
    condition_frame <- c()
    print(paste("GRAPH LINK DENSITY ",de, sep = ""))
    for (ss in subjects)
    {
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity",de,"/", sep = "")) 
        for (i in conditions)
        {
            modscores <- c()
            filelist = list.files(pattern = glob2rx(paste("*",ss,".",i,"*.Qval", sep = "")))
            for (f in filelist)
            {
                modscores <- c(modscores, as.matrix(read.table(f)))
            }
            fname <- filelist[which(modscores == sort(modscores)[51])]   # for #1 above, corresponds to Qval
            pref <- unlist(strsplit(fname, ".", fixed = TRUE))[1]   # grabbing the iter prefix
            infile <- list.files(pattern = glob2rx(paste(pref,".",ss,".",i,".*.maxlevel_tree", sep = "")))
            tree <- as.matrix(read.table(infile))   # for #1 above, corresponds to Qval
            tree_nn <- length(aggregate(tree[,2], list(tree[,2]), length)[,1][aggregate(tree[,2], list(tree[,2]), length)$x > cutoff])
            tree_modsize_mean <- mean(aggregate(tree[,2], list(tree[,2]), length)[,2][aggregate(tree[,2], list(tree[,2]), length)$x > cutoff])
            tree_modsize_med <- median(aggregate(tree[,2], list(tree[,2]), length)[,2][aggregate(tree[,2], list(tree[,2]), length)$x > cutoff])
            num_mods <- c(num_mods, tree_nn)
            tree_modsizes_means <- c(tree_modsizes_means, tree_modsize_mean)
            tree_modsizes_medians <- c(tree_modsizes_medians, tree_modsize_med)
            #stddev_data <- c(stddev_data, sd(modscores))
            filelist2 = list.files(pattern = glob2rx(paste("*",ss,".",i,"*.maxlevel_tree", sep = "")))
            imods <- c()
            modsize_mean <- c()
            modsize_med <- c()
            for (ff in filelist2)
            {
                ffdat <- as.matrix(read.table(ff))
                nn <- length(aggregate(ffdat[,2], list(ffdat[,2]), length)[,1][aggregate(ffdat[,2], list(ffdat[,2]), length)$x > cutoff])
                modsize_mean <- mean(aggregate(ffdat[,2], list(ffdat[,2]), length)[,2][aggregate(ffdat[,2], list(ffdat[,2]), length)$x > cutoff])
                modsize_med <- median(aggregate(ffdat[,2], list(ffdat[,2]), length)[,2][aggregate(ffdat[,2], list(ffdat[,2]), length)$x > cutoff])
                imods <- c(imods, nn)
            }
            uniqmods <- c(uniqmods, median(imods))
            modsizes_means <- c(modsizes_means, mean(modsize_mean))
            modsizes_medians <- c(modsizes_medians, median(modsize_med))
            subject_frame <- c(subject_frame, ss)
            condition_frame <- c(condition_frame, paste("cond",i,sep=""))
        }
    }


    mod_score_frame <- data.frame(num_mods, uniqmods, tree_modsizes_means, tree_modsizes_medians, modsizes_means, modsizes_medians, subject_frame, condition_frame)   # "num_mods" corresponds to number of modules from tree of median Qval; "uniqmods" corresponds to median of module count across all 100 iterations per participant and condition; "modsizes_means" corresponds to average module size (# of voxels) in all iterations; "modsizes_medians" corresponds to median module size (#of voxels) in all iterations.
    colnames(mod_score_frame) <- c("num_modules", "iterall_mods", "single_mean_modsizes", "single_median_modsizes", "alliter_mean_modsizes", "alliter_median_modsizes", "subject", "condition")
    #write.table(mod_score_frame, paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/number_modules_frame",de,"_fromiters.txt", sep = ""), row.names = F, quote = F)
    write.table(mod_score_frame, paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/number_modules_frame",de,"_fromiters2.txt", sep = ""), row.names = F, quote = F)
    #print(summary(aov(num_modules ~ condition + Error(subject/condition), data=mod_score_frame)))
    cond_means1 <- tapply(mod_score_frame$num_modules, mod_score_frame$condition, mean)
    print(cond_means1)
    cond_means2 <- tapply(mod_score_frame$iterall_mods, mod_score_frame$condition, mean)
    print(cond_means2)
    cond_meds <- tapply(mod_score_frame$num_modules, mod_score_frame$condition, median)
    print(cond_meds)
    cond_meds2 <- tapply(mod_score_frame$iterall_mods, mod_score_frame$condition, median)
    print(cond_meds2)
    attach(mod_score_frame)
    print(pairwise.t.test(num_modules, condition, p.adjust.method="bonferroni", paired=T))
    c1 = c(num_modules[which(condition=="cond1")])
    c2 = c(num_modules[which(condition=="cond2")])
    c3 = c(num_modules[which(condition=="cond3")])
    c4 = c(num_modules[which(condition=="cond4")])
    print(pairwise.t.test(iterall_mods, condition, p.adjust.method="bonferroni", paired=T))
    c1m = c(iterall_mods[which(condition=="cond1")])
    c2m = c(iterall_mods[which(condition=="cond2")])
    c3m = c(iterall_mods[which(condition=="cond3")])
    c4m = c(iterall_mods[which(condition=="cond4")])
    ## non-parametric 
    print(friedman.test(num_modules ~ condition | subject))
    print(wilcox.test(c1,c2,paired=T))
    print(wilcox.test(c1,c3,paired=T))
    print(wilcox.test(c1,c4,paired=T))
    print(wilcox.test(c2,c3,paired=T))
    print(wilcox.test(c2,c4,paired=T))
    print(wilcox.test(c3,c4,paired=T))
    print(friedman.test(iterall_mods ~ condition | subject))
    print(wilcox.test(c1m,c2m,paired=T))
    print(wilcox.test(c1m,c3m,paired=T))
    print(wilcox.test(c1m,c4m,paired=T))
    print(wilcox.test(c2m,c3m,paired=T))
    print(wilcox.test(c2m,c4m,paired=T))
    print(wilcox.test(c3m,c4m,paired=T))
}

