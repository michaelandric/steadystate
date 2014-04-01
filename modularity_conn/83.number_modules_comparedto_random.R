## comparing number of modules in random

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

de <- "5p"
cutoff <- 1

uniqmods <- c()
uniqmodsRND <- c()
uniqmods_avg <- c()
uniqmodsRND_avg <- c()
subject_frame <- c()
condition_frame <- c()

for (ss in subjects)
{
    print(ss)
    for (i in conditions)
    {
        print(i)
        modsize_med <- c()

        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity",de,"/", sep = ""))
        filelist = list.files(pattern = glob2rx(paste("*",ss,".",i,"*.maxlevel_tree", sep = "")))
        imods <- c()
        for (ff in filelist)
        {
            ffdat <- as.matrix(read.table(ff))
            nn <- length(aggregate(ffdat[,2], list(ffdat[,2]), length)[,1][aggregate(ffdat[,2], list(ffdat[,2]), length)$x > cutoff])
            imods <- c(imods, nn)
        }
        uniqmods <- c(uniqmods, median(imods))   # here get median of the number of modules
        uniqmods_avg <- c(uniqmods_avg, mean(imods))   # here get average of the number of modules

        setwd("/mnt/tier2/urihas/Andric/steadystate/links_files5p/rando_trees/")
        filelistRND <- list.files(pattern = glob2rx(paste("*",ss,"_",i,"*", sep = "")))
        imodsRND <- c()
        for (ff in filelistRND)
        {
            ffdatRND <- as.matrix(read.table(ff))
            nnRND <- length(aggregate(ffdatRND[,1], list(ffdatRND[,1]), length)[,1][aggregate(ffdatRND[,1], list(ffdatRND[,1]), length)$x > cutoff])
            imodsRND <- c(imodsRND, nnRND)
        }
        uniqmodsRND <- c(uniqmodsRND, median(imodsRND))
        uniqmodsRND_avg <- c(uniqmodsRND_avg, mean(imodsRND))
        print(uniqmodsRND)
        print(uniqmodsRND_avg)

        subject_frame <- c(subject_frame, ss)
        condition_frame <- c(condition_frame, paste("cond",i,sep=""))
    }
}

#dat_frame <- data.frame(uniqmods, uniqmodsRND, subject_frame, condition_frame)
vals_frame <- data.frame(c(uniqmods, uniqmodsRND), c(rep("n_mods", length(uniqmods)), rep("n_modsRND", length(uniqmodsRND))), rep(subject_frame, 2), rep(condition_frame, 2))
vals_frame_avg <- data.frame(c(uniqmods_avg, uniqmodsRND_avg), c(rep("n_mods", length(uniqmods)), rep("n_modsRND", length(uniqmodsRND))), rep(subject_frame, 2), rep(condition_frame, 2))
colnames(vals_frame) <- c("N", "categ", "subject", "condition")
colnames(vals_frame_avg) <- c("N", "categ", "subject", "condition")
attach(vals_frame)
print(aggregate(N, list(categ, condition), summary))
print(aggregate(N, list(categ, condition), sd))

print(with(subset(vals_frame, categ == "n_modsRND"), friedman.test(N ~ condition | subject)))

print(with(subset(vals_frame, condition == "cond1"), wilcox.test(N ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond2"), wilcox.test(N ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond3"), wilcox.test(N ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond4"), wilcox.test(N ~ categ, paired = T)))

detach(vals_frame)

attach(vals_frame_avg)
print(aggregate(N, list(categ, condition), summary))
print(aggregate(N, list(categ, condition), sd))

print(with(subset(vals_frame, categ == "n_modsRND"), friedman.test(N ~ condition | subject)))

print(with(subset(vals_frame, condition == "cond1"), wilcox.test(N ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond2"), wilcox.test(N ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond3"), wilcox.test(N ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond4"), wilcox.test(N ~ categ, paired = T)))


