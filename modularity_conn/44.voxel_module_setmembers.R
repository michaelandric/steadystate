## characterize voxels by their module membership between Highly ordered and Random conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
cutoff = 100

average_counts <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR",sep=""))
    dat1 <- as.matrix(read.table(list.files(pattern=paste("cleanTS.1.*.justcomm",sep="")))) 
    dat1 <- cbind(c(1:length(dat1)), dat1)
    dat3 <- as.matrix(read.table(list.files(pattern=paste("cleanTS.3.*.justcomm",sep=""))))
    dat3 <- cbind(c(1:length(dat3)), dat3)
    ordered_agframe1 = aggregate(dat1[,2], list(dat1[,2]), length)[order(-aggregate(dat1[,2], list(dat1[,2]), length)$x),]
    ordered_agframe3 = aggregate(dat3[,2], list(dat3[,2]), length)[order(-aggregate(dat3[,2], list(dat3[,2]), length)$x),]

## Does disorder partition modules that exist in "Highly ordered" (pruning)
## Or do voxels form new setsi, i.e., which voxels connect is different (re-organization)
## see if in Random condition voxels in a set are also in a set in Highly Ordered 

    for (i in unique(dat1[,2]))
    {
        which(dat1[,1]set1 %in% dat3[,1]set1)


set1 = subset(dat1, dat1[,2]==ordered_agframe1$Group.1[1])[,1]
set2 = subset(dat1, dat1[,2]==ordered_agframe1$Group.1[2])[,1]
set1_3 = subset(dat3, dat3[,2]==ordered_agframe3$Group.1[1])[,1]

subset(dat1, dat1[,2]==unique(dat1[,2])[1])[,1]
ordered_agframe = aggregate(dat1[,2], list(dat1[,2]), length)[order(-aggregate(dat1[,2], list(dat1[,2]), length)$x),]
length(intersect(set1,set1_3))


