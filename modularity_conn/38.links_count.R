## evalute the percent /number of links that remain in the network after threshold
#subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
#conditions <- seq(4)

setwd(paste(Sys.getenv("state"),"/groupstats",sep=""))
link_count <- read.table("link_count_0.5thresh.txt")
vox_count <- read.table("subject_graymattermask_voxnum.txt")
vox_count2 <- subset(vox_count, vox_count$V1!="BARS")

links_frame <- data.frame(link_count,rep((((vox_count2$V2)^2) / 2),each=4))
colnames(links_frame) <- c("subject", "condition", "links", "possible")
links_frame <- data.frame(links_frame, links_frame$links / links_frame$possible)
colnames(links_frame) <- c("subject", "condition", "links", "possible", "frac_remain")
print(aggregate(links_frame$frac_remain, list(links_frame$condition), mean))
print(aggregate(links_frame$frac_remain, list(links_frame$condition), sd))

