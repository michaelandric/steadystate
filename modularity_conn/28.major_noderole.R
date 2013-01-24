## This is getting the major node role (the majority among participants)
## setting up to do conditions in separate batches. So, this handles only one condition.
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
startvox <- as.numeric(noquote(strsplit(Args," ")[[1]][1]))
endvox <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

setwd(paste(Sys.getenv("state"),"/groupstats/",sep=""))
print(getwd())
roles <- c()

VoxRole <- function(vox)
{
    for (ss in subjects)
    {
        node_role <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",ss,".",Cond,".node_roles_tlrc_dump.txt",sep="")
        roles <- c(roles, scan(node_role,sep=" ",nlines=1,skip=vox)[4])
    }
    ## get the aggregate number occurrences for each role
    agrole = aggregate(roles,list(roles),length)

    ## only want majority - no ties
    if (length(which(agrole$x == max(agrole$x))) > 1)
    {
        role = 0
        numss = 0
    }
    else
    {
        role = agrole[which.max(agrole[,2]),1]
        numss = agrole[which.max(agrole[,2]),2]
    }
    return(c(vox,role,numss))
}


out <- c()
for (vv in c(startvox:endvox))
{
    print(vv)
    out <- c(out,VoxRole(vv))
}

outmat = matrix(out,ncol=3,byrow=T)
outname = paste(startvox,"_Cond",Cond,"major_noderole.txt",sep="")
write.table(outmat,outname,row.names=F,col.names=F,quote=F)
