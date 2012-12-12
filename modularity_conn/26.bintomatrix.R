## This is code to turn a *.bin file created with fcorr (via the "bct" package) and make a text file matrix
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
ss <- noquote(strsplit(Args," ")[[1]][1])
nVoxArg <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
print(c(ss,nVoxArg,Cond))


bintomatrix <- function(infile,outmat,nrows,ncols)
{
    for (r in 0:nrows)
    {
        tsvals = NULL
        for(c in 0:ncols)
        {
            tsval = readBin(infile, numeric(), size=4)
            tsvals = c(tsvals,tsval)
        }
        write(tsvals,outmat,ncolumns=ncols,append=TRUE,sep=" ")
        write("\n",outmat, append=TRUE)
    }
}            

#readBin(corrmat,numeric(),n=(10094^2),size=4)
setwd(paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/",sep=""))
corrmat <- paste("cleanTS.",Cond,".",ss,"_graymask_dump.bin.corr",sep="")
outname <- paste("Cond",Cond,".",ss,".matrix.corr.txt",sep="")
bintomatrix(corrmat,outname,nVoxArg,nVoxArg)

