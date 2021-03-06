## this is simple code for getting quick filter passes of the communities.
## originally seelcts only those greater than 100 voxels
Args <- Sys.getenv("R_ARGS")
ss <- noquote(strsplit(Args," ")[[1]][1])
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
treeNum <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

#setwd(paste(Sys.getenv("state"),"/",ss,"/corrORIG_versionTRIM/",sep=""))
setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
print(getwd())
#tree = read.table(paste(ss,".",Cond,".corrmatrix.bin.thresh.tree",treeNum,sep=""))
tree = as.matrix(read.table(paste("cleanTS.Cond",Cond,".",ss,".noijk_dump.bin.corr.thresh.tree",treeNum,".justcomm",sep="")))
ag.tree = aggregate(tree,list(tree),length)
ag.tree[which(ag.tree[,2] > 100),]
ag.tree.top = ag.tree[which(ag.tree[,2] > 100),]
filt.tree = tree
filt.tree[which(!filt.tree %in% ag.tree.top[,1])]=0
print(summary(filt.tree))
print(length(filt.tree))
write.table(filt.tree,paste(ss,".",Cond,".comm.tree",treeNum,"_filt.txt",sep=""),row.names=F,col.names=F,quote=F)
