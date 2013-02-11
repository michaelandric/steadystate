## Analysis to get the power law exponent
library(igraph)
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
Subj <- paste(noquote(strsplit(Args," ")[[1]][1]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Tree <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

spec_func <- function(x)
{
    voxts = ts(as.numeric(x), frequency=2/3)
    spec_out = spectrum(voxts, plot=F)
    return(spec_out$spec[1:15])
}

freq_vals <- spectrum(ts(rnorm(90,1),frequency=2/3), plot=F)$freq

setwd(paste(Sys.getenv("state"),"/",Subj,"/corrTRIM_BLUR/",sep=""))
#print(getwd())
##These 'clean' time series were generated from 4.fcorr.py
myts <- read.table(paste("cleanTS.",Cond,".",Subj,"_graymask_dump",sep=""))
nvox <- dim(myts)[1]

## initiate output frame
output <- c()
mods <- as.matrix(read.table(paste("cleanTS.",Cond,".",Subj,"_graymask_dump.bin.corr.thresh.tree",Tree,".justcomm",sep="")))
mod_list <- unique(mods)

for (i in mod_list)
{
    mod_vox <- which(mods==i)
    spec_power <- rowMeans(apply(myts[mod_vox,], 1, spec_func))
    power_exp <- coef(lm(log(spec_power) ~ log(1/freq_vals[1:15])))[[2]]
    power_exp2 <- coef(lm(log(spec_power[2:15]) ~ log(1/freq_vals[2:15])))[[2]]
    print(power.law.fit(spec_power))
    print(coef(power.law.fit(spec_power))[[1]])
    power_expalpha <- coef(power.law.fit(spec_power))[[1]]
    output <- rbind(output, c(i, round(power_exp,3), round(power_exp2,3), round(power_expalpha,3)))
}

write.table(output, paste("modules.",Cond,".",Subj,"_powerexp",sep=""), row.names=F,col.names=F,quote=F)
