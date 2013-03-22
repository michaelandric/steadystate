## Group analysis for the power law exponent across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
exp_data <- c()
surviving_voxel_prop <- c()
subject_frame <- c()
condition_frame <- c()

module_voxelnum_limit = 37

for (ss in subjects)
{
    setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
    print(getwd())
    for (Cond in conditions)
    {
        mods_filename <- list.files(pattern=paste("cleanTS.",Cond,".*.justcomm",sep=""))
        mods <- as.matrix(read.table(mods_filename))
        exps <- read.table(paste("modules.",Cond,".",ss,"_powerexp_filteredneg",sep=""))
        contributing_mods <- exps[,1][which(exps[,4] > module_voxelnum_limit)]
        #contributing_mods <- aggregate(mods, list(mods), length)[which(aggregate(mods,list(mods), length)[,2] > module_voxelnum_limit),1]
        exp_meanval <- mean(subset(exps, exps[,1]%in%contributing_mods)[,2],na.rm=T)
        vox_prop <- mean(subset(exps, exps[,1]%in%contributing_mods)[,5],na.rm=T)
        print(paste(ss,"condition",Cond,"exp avg val is",exp_meanval))
        exp_data <- c(exp_data, exp_meanval)
        surviving_voxel_prop <- c(surviving_voxel_prop, vox_prop)
        subject_frame <- c(subject_frame, ss)
        condition_frame <- c(condition_frame, paste("cond",Cond,sep=""))
    }
}

exp_frame <- data.frame(exp_data,surviving_voxel_prop,subject_frame,condition_frame)
colnames(exp_frame) <- c("avgexp","voxelproportion","subject","condition")
print(exp_frame)
print(summary(aov(avgexp ~ condition + Error(subject/condition), data=exp_frame)))
cond_means <- tapply(exp_frame$avgexp, exp_frame$condition, mean)
print(tapply(exp_frame$voxelproportion, exp_frame$condition, mean))
print(cond_means)
