## Analysis to get the power law exponent
Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
print(length(noquote(strsplit(Args," ")[[1]])))
Subj <- paste(noquote(strsplit(Args," ")[[1]][1]))
Cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
Tree <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))

linear_predictor <- seq(14)
spec_func_linear_filt <- function(x)
{
    voxts = ts(as.numeric(x), frequency=2/3)
    spec_out = spectrum(voxts, plot=F)
    usable_spec = spec_out$spec[2:15]
    #linear_test_F = summary(lm(usable_spec ~ linear_predictor))$fstatistic[[1]]  ##Unused here. Left in code for use another time.
    #linear_pval = summary(lm(usable_spec ~ linear_predictor))$coefficients[8]
    linear_pred = summary(lm(usable_spec ~ linear_predictor))$coefficients[[2]]
    out <- c(usable_spec, round(linear_pred,4))
    return(out)
}


freq_vals <- spectrum(ts(rnorm(90,1),frequency=2/3), plot=F)$freq

setwd(paste(Sys.getenv("state"),"/",Subj,"/corrTRIM_BLUR/",sep=""))
##These 'clean' time series were generated from 4.fcorr.py
myts <- read.table(paste("cleanTS.",Cond,".",Subj,"_graymask_dump",sep=""))
nvox <- dim(myts)[1]

## initiate output frame
output <- c()
mods <- as.matrix(read.table(paste("cleanTS.",Cond,".",Subj,"_graymask_dump.bin.corr.thresh.tree",Tree,".justcomm",sep="")))
mod_list <- unique(mods)

for (i in mod_list)
{
    mod_vox <- which(mods==i) ## use only voxels belonging to the module
    spec_apply <- apply(myts[mod_vox,], 1, spec_func_linear_filt) ## use the function on the module's voxels
    if (length(as.matrix(which(spec_apply[15,] < 0))) == 0) ## check to see if some voxels show linear trend
    {
        spec_pval_filt = NA
        num_survive_voxels = 0
        proportion_survive_voxels = 0
        power_exp = NA
    }else
    {
        spec_pval_filt <- as.matrix(which(spec_apply[15,] >= 0)) ## now filtering by those that don't show negative linear trend
        num_survive_voxels <- length(mod_vox) - length(spec_pval_filt) ## find number of voxels that pass the filter
        if (num_survive_voxels==1)
        {
            spec_power <- spec_apply[1:14,]
        }else
        {
            if (num_survive_voxels==length(mod_vox)) ## in case where all pass filter
            {
                spec_power <- rowMeans(spec_apply[1:14,]) ## determine spectrum power 
            }else
            {
                spec_power <- rowMeans(spec_apply[1:14,-spec_pval_filt]) ## determine the spectrum power only using unfilterd
            }
        }
        proportion_survive_voxels <- num_survive_voxels / length(mod_vox) ## find the proportion voxels that pass the filter
        power_exp <- coef(lm(log(spec_power) ~ log(1/freq_vals[2:15])))[[2]] ## determine power exponent
    }
    output <- rbind(output, c(i, round(power_exp,3), length(spec_pval_filt), num_survive_voxels, round(proportion_survive_voxels,3))) 
}

write.table(output, paste("modules.",Cond,".",Subj,"_powerexp_filteredneg",sep=""), row.names=F,col.names=F,quote=F)
