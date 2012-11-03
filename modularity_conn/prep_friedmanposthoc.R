ff <-  read.table("friedman_out.sorted.txt")
length(which(ff[,3] <= .05))
batchsize = 10000
batchstarts <- seq(1,length(which(ff[,3] <= .05)), batchsize)
for (i in 1:(length(batchstarts)-1))
{
    print(batchstarts[i])
    group <- which(ff[,3] <= .05)[batchstarts[i]:(batchstarts[i]+batchsize-1)]
    write.table(group,paste("group",i,".txt",sep=""),row.names=F,col.names=F,quote=F)
}

lastgroup <- which(ff[,3] <= .05)[batchstarts[length(batchstarts)]:length(which(ff[,3] <= .05))]
write.table(lastgroup,paste("group",length(batchstarts),".txt",sep=""),row.names=F,col.names=F)
