## This is to analyze time series frequency power
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
Subj <- paste(noquote(strsplit(Args," ")[[1]][1]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))

setwd(paste(Sys.getenv("state"),"/",Subj,"/corrTRIM_BLUR/",sep=""))
#print(getwd())
##These 'clean' time series were generated from 4.fcorr.py
myts <- read.table(paste("cleanTS.",Cond,".",Subj,"_graymask_dump",sep=""))
nvox <- dim(myts)[1]

## initiate output frame
output <- c()

for (vox in 1:nvox)
{
    #print(vox)
    voxts <- ts(as.numeric(myts[vox,]), frequency=2/3)
    current.spectrum <- spectrum(voxts, spans=c(2,2), plot=F)
    ##find the max power and which freq it belongs
    max_power <- max(current.spectrum$spec)
    freq_max_power <- current.spectrum$freq[which.max(current.spectrum$spec)]
    ##to what extent is the frequency an outlier relative to power in other freqs
    max_power_scaled <- scale(current.spectrum$spec)[which.max(current.spectrum$spec)]
    output <- rbind(output, c(round(max_power,4), round(freq_max_power,4), round(max_power_scaled,4)))
}

write.table(output, paste("cleanTS.",Cond,".",Subj,"_graymask_dump_freqpower",sep=""), row.names=F,col.names=F,quote=F)
