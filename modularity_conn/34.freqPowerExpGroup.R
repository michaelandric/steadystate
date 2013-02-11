## Group analysis for the power law exponent across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
exp_data <- c()
subject_frame <- c()
condition_frame <- c()

module_voxelnum_limit = 50

for (ss in subjects)
{
    setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
    print(getwd())
    for (Cond in conditions)
    {
        mods_filename <- list.files(pattern=paste("cleanTS.",Cond,".*.justcomm",sep=""))
        mods <- as.matrix(read.table(mods_filename))
        exps <- read.table(paste("modules.",Cond,".",ss,"_powerexp",sep=""))
        contributing_mods <- aggregate(mods, list(mods), length)[which(aggregate(mods,list(mods), length)[,2] > module_voxelnum_limit),1]
        exp_meanval <- mean(subset(exps, exps[,1]%in%contributing_mods)[,3])
        print(paste(ss,"condition",Cond,"exp avg val is",exp_meanval))
        exp_data <- c(exp_data, exp_meanval)
        subject_frame <- c(subject_frame, ss)
        condition_frame <- c(condition_frame, paste("cond",Cond,sep=""))
    }
}

exp_frame <- data.frame(exp_data,subject_frame,condition_frame)
colnames(exp_frame) <- c("avgexp","subject","condition")
print(exp_frame)
print(summary(aov(avgexp ~ condition + Error(subject/condition), data=exp_frame)))
cond_means <- tapply(exp_frame$avgexp, exp_frame$condition, mean)
print(cond_means)
