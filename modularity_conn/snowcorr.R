# get values from swift

library(Rmpi)
library(snow)
library(bct)

nvox <- 34763
cluster = makeMPIcluster(32)

# assumes voxels are 0-ordered
correlateall <- function(vox)
{
ss <- "p4ctd_child01"
cleantshead <- paste("/cnari/child_language/volume.data/CTD_CHILD_YEAR1/",ss,"/common/cleanTScat.",ss,".allwordruns.resamp+orig.HEAD",sep="")
cleantsbrik <- paste("/cnari/child_language/volume.data/CTD_CHILD_YEAR1/",ss,"/common/cleanTScat.",ss,".allwordruns.resamp+orig.BRIK",sep="")
cleantstxt <- paste("/cnari/child_language/volume.data/CTD_CHILD_YEAR1/",ss,"/common/cleanTScat.",ss,".allwordruns.resamp.noijk.txt",sep="")
maskhead <- paste("/cnari/child_language/volume.data/CTD_CHILD_YEAR1/",ss,"/common/auto.mask.di1.alldecon.",ss,".resamp+orig.HEAD",sep="")
maskbrik <- paste("/cnari/child_language/volume.data/CTD_CHILD_YEAR1/",ss,"/common/auto.mask.di1.alldecon.",ss,".resamp+orig.BRIK",sep="")
thresh <- .25

vox_1d = as.matrix(read.table(cleantstxt,nrows=1,skip=vox))
dfile = paste("voxel",vox,"TS.1D", sep="")
bucketfile = paste("corrTask.masked.voxel",vox,ss,sep="")
write(vox_1d,dfile,sep="\n")
afnicmd1 = paste("3dfim+ -input ",cleantsbrik," -mask ",maskbrik," -ideal_file ",dfile," -out Correlation -bucket ",bucketfile,sep="")

print(afnicmd1)
system(afnicmd1)
voxtxt = paste("/cnari/child_language/volume.data/CTD_CHILD_YEAR1/",ss,"/common/Taskoutfiles/corrTask.masked.voxel",vox,".",ss,"noijk.txt",sep="")
afnicmd2 = paste("3dmaskdump -mask ",maskbrik," -noijk corrTask.masked.voxel",vox,ss,"+orig.BRIK > ",voxtxt,sep="")
print(afnicmd2)
system(afnicmd2)
system(paste("rm ",dfile))
system(paste("rm ",bucketfile,"*",sep=""))
}

parallelCorr <- function(numVox)
{
	parSapply(cluster, 0:numVox,correlateall)
}

parallelCorr(nvox-1)
stopCluster(cluster)



