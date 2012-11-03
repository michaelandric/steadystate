# running correlation voxel by voxel with afni using R

type file;
type Rscript;

app (file taskout) corr3dfim(Rscript corrR, string subj, file tshead, file tsbrik, file tstxt, file maskhead, file maskbrik, int vox)
{
	RInvoke @corrR subj @tshead @tsbrik @tstxt @maskhead @maskbrik vox;
}

Rscript corrR<single_file_mapper;file="corr.R">;

string ss[] = ["p4ctd_child03"];
int totalvoxels[] = [53127];

foreach subj, index in ss{
	trace(index);
	int nvox = totalvoxels[index];
	trace(nvox);
	int voxels[] = [0:(nvox-1)];
	string fileprefix=@strcat("/cnari/child_language/volume.data/CTD_CHILD_YEAR1/",subj,"/common/");
	foreach vox in voxels{
		file tshead<single_file_mapper;file=@strcat(fileprefix,"cleanTScat.",subj,".allwordruns.resamp+orig.HEAD")>;
		file tsbrik<single_file_mapper;file=@strcat(fileprefix,"cleanTScat.",subj,".allwordruns.resamp+orig.BRIK")>;
		file tstxt<single_file_mapper;file=@strcat(fileprefix,"cleanTScat.",subj,".allwordruns.resamp.noijk.txt")>;
		file maskhead<single_file_mapper;file=@strcat(fileprefix,"auto.mask.di1.alldecon.",subj,".resamp+orig.HEAD")>;
		file maskbrik<single_file_mapper;file=@strcat(fileprefix,"auto.mask.di1.alldecon.",subj,".resamp+orig.BRIK")>;
		file tout<single_file_mapper; file=@strcat(fileprefix,"Taskoutfiles/corrTask.masked.voxel",vox,".",subj,".noijk.txt")>;
		tout = corr3dfim(corrR,subj,tshead,tsbrik,tstxt,maskhead,maskbrik,vox);
		}
}
