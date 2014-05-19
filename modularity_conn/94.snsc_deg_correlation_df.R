## Determine whether SNSC correlates with Degrees

## !!!!! This was built as a take on 92.snsc_deg_correlation.R
## Uses an effective degrees of freedom that accounts for spatial noise in the time series data
## see stuff on RESELS (Worsley's RFT is a point of departue)
## effectively lowering resoultion from single voxel to appropriate up-samples


v = 4 * 4 * 4.8   # this is the voxel size in mm
RESEL <- function(v, N, FWHMvec) 
    N / (prod(c(apply(read.table(paste(FWHMvec)), 2, mean))) / v)   # http://blogs.warwick.ac.uk/nichols/entry/fwhm_resel_details/

corT <- function(r, effectiveN) 
    r / (sqrt((1-r**2)/(effectiveN-2)))   # effective N is the adjusted N after FWHM estimate for effective resolution

subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")

r_estimates1 <- c()
r_estimates3 <- c()
effective_N1 <- c()
effective_N3 <- c()
for (ss in subjects)
{
    d1 <- as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/links_files5p/",ss,".1.5p_linksthresh_proportion.degrees_gray", sep = "")))   # these are the degrees
    d3 <- as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/links_files5p/",ss,".3.5p_linksthresh_proportion.degrees_gray", sep = "")))   # these are the degrees
    snsc_with_filtvals <- as.matrix(read.table(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/modularity5p/set_consistency2/preserved_",ss,"_median5p_20vxFltr.txt", sep = "")))
    #print(c(ss, length(which(snsc_with_filtvals == 777)), round(length(which(snsc_with_filtvals == 777))/length(snsc_with_filtvals),3)))
    snsc <- snsc_with_filtvals
    snsc[which(snsc_with_filtvals == 777)] = NA

    r_estimates1 <- c(r_estimates1, cor.test(snsc, d1, use = "complete.obs")$estimate[[1]])
    r_estimates3 <- c(r_estimates3, cor.test(snsc, d3, use = "complete.obs")$estimate[[1]])

    effective_N1 <- c(effective_N1, RESEL(v, length(d1), paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/",ss,".Cond1_fwhm_estimates", sep = "")))   # determine RESEL 
    effective_N3 <- c(effective_N3, RESEL(v, length(d1), paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/",ss,".Cond3_fwhm_estimates", sep = "")))   # determine RESEL 
}

print(r_estimates1)
print(summary(r_estimates1))
print(r_estimates3)
print(summary(r_estimates3))

print(corT(r_estimates1, effective_N1))
print(summary(corT(r_estimates1, effective_N1)))
print(t.test(corT(r_estimates1, effective_N1)))

print(corT(r_estimates3, effective_N3))
print(summary(corT(r_estimates3, effective_N3)))
print(t.test(corT(r_estimates3, effective_N3)))

