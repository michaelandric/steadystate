## this is simple code for getting quick filter passes of the communities.
## originally seelcts only those greater than 100 voxels
Args <- Sys.getenv("R_ARGS")
ss <- noquote(strsplit(Args," ")[[1]][1])
nVoxArg <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
treeNum <- as.numeric(noquote(strsplit(Args," ")[[1]][4]))

#setwd(paste(Sys.getenv("state"),"/",ss,"/connectivity/",sep=""))
setwd(paste(Sys.getenv("state"),"/",ss,"/corrORIG_versionTRIM/",sep=""))
print(getwd())
tree = read.table(paste(ss,".",Cond,".comm.tree",treeNum,"_filt.txt",sep=""))
filt.tree = tree
print(summary(filt.tree))
junk = c(as.matrix(read.table(paste("junk_comms_Cond",Cond,".txt",sep=""))))
filt.tree[which(filt.tree[,1] %in% junk),1]=0
print(summary(filt.tree))
print(length(filt.tree[,1]))
write.table(filt.tree[,1],paste(ss,".",Cond,".comm.tree",treeNum,"_filt2.txt",sep=""),row.names=F,col.names=F,quote=F)
#write.table(filt.tree[,1],paste(ss,".",Cond,".comm.tree",treeNum,"_filt3.txt",sep=""),row.names=F,col.names=F,quote=F)
