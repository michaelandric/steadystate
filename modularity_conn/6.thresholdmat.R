library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))


thresh_func <- function(i,ss)
{
    library(bct)
    corrmat <- paste(Sys.getenv("state"),"/",ss,"/corrTRIM_BLUR/cleanTS.Cond",i,".",subj,".noijk_dump.bin.corr",sep="")
    fthreshold_absolute(corrmat,.5,1)
}


thresh_func(cond,subj)
