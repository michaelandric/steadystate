## Q values differ from random Q values

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

#densities <- c("5p", "8p", "12p", "15p")   # only have random Q vals for 5p right now (29.March.2014)
de <- "5p"

Qdata <- c()
RNDdata <- c()
subject_frame <- c()
condition_frame <- c()
for (ss in subjects)
{
    for (i in conditions)
    {   
        Qscores <- c() 
        RNDscores <- c()
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity",de,"/", sep = ""))   # have to reset the dir becase glob2rx doesn't take dir arg, needs local
        filelistQ <- list.files(pattern = glob2rx(paste("*",ss,".",i,"*.Qval", sep = "")))
        for (f in filelistQ)
        {
            Qscores <- c(Qscores, as.matrix(read.table(f)))
        }
        setwd("/mnt/tier2/urihas/Andric/steadystate/links_files5p/rando/")
        filelistRND <- list.files(pattern = glob2rx(paste("*",ss,"_",i,"*", sep = "")))
        for (f in filelistRND)
        {
            RNDscores <- c(RNDscores, as.matrix(read.table(f)))
        }
        Qdata <- c(Qdata, sort(Qscores)[51])
        RNDdata <- c(RNDdata, sort(RNDscores)[51])
        subject_frame <- c(subject_frame, ss)
        condition_frame <- c(condition_frame, paste("cond",i,sep=""))
    }
}

dat_frame <- data.frame(Qdata, RNDdata, subject_frame, condition_frame)         
vals_frame <- data.frame(c(Qdata, RNDdata), c(rep("Qval", length(Qdata)), rep("RNDval", length(RNDdata))), rep(subject_frame, 2), rep(condition_frame, 2))
colnames(vals_frame) <- c("Q", "categ", "subject", "condition") 
attach(vals_frame)
print(aggregate(Q, list(categ, condition), summary))
print(aggregate(Q, list(categ, condition), sd))


print(with(subset(vals_frame, categ == "RNDval"), friedman.test(Q ~ condition | subject)))

print(with(subset(vals_frame, condition == "cond1"), wilcox.test(Q ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond2"), wilcox.test(Q ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond3"), wilcox.test(Q ~ categ, paired = T)))
print(with(subset(vals_frame, condition == "cond4"), wilcox.test(Q ~ categ, paired = T)))


 
