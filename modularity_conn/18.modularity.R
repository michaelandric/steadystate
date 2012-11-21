## repeated measures ANOVA on modularity scores

#subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)

mod_data <- c()
subject_frame <- c()
condition_frame <- c()

for (ss in subjects)
{
    for (i in conditions)
    {
        modscore <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/mod_score.",ss,".Cond",i,".txt",sep="")
        mod_data <- c(mod_data,as.matrix(read.table(modscore))[1])
        subject_frame <- c(subject_frame,ss)
        condition_frame <- c(condition_frame,paste("cond",i,sep=""))
    }
}


mod_score_frame <- data.frame(mod_data,subject_frame,condition_frame)
colnames(mod_score_frame) <- c("modularity","subject","condition")
print(summary(aov(modularity ~ condition + Error(subject/condition), data=mod_score_frame)))
cond_means <- tapply(mod_score_frame$modularity, mod_score_frame$condition, mean)
print(cond_means)
attach(mod_score_frame)
print(pairwise.t.test(modularity, condition, p.adjust.method="bonferroni",paired=T))
#with(mod_score_frame, pairwise.t.test(modularity, condition, p.adjust.method="fdr", paired=T))
c1 = c(modularity[which(condition=="cond1")])
c2 = c(modularity[which(condition=="cond2")])
c3 = c(modularity[which(condition=="cond3")])
c4 = c(modularity[which(condition=="cond4")])
print(t.test(c1,c2,paired=T))
print(t.test(c1,c3,paired=T))
print(t.test(c1,c4,paired=T))
print(t.test(c2,c3,paired=T))
print(t.test(c2,c4,paired=T))
print(t.test(c3,c4,paired=T))
## non-parametric 
#friedman.test(modularity ~ condition | subject)
#wilcox.test(c1,c3,paired=T)
