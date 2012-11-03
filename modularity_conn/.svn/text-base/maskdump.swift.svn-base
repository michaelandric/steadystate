## for doing 3dmaskdump
type file{}
type AFNI_obj{
    file HEAD;
    file BRIK;
}

app (file outfile) Maskdump (file pyscript, AFNI_obj mask, AFNI_obj input, string outname, string relativeloc){
    shell "python" @pyscript "--ijk" "no" "--automask" @mask "--inputfile" @input "--outputname" @strcat(relativeloc,outname);
}

file pyscript<single_file_mapper; file="maskdump.py">;
#string subjects[] = ["hel12","hel13","hel14","hel15","hel16","hel17","hel18"];
string subjects[] = ["hel19"];

foreach ss in subjects{
    string relativeloc = @strcat("gpfs/pads/projects/normal_language/HEL/",ss,"/connectivity/");
    string loc = @strcat("/",relativeloc);
    AFNI_obj mask<simple_mapper; location = loc, prefix=@strcat("automask_d2_",ss,"+orig.")>;
    AFNI_obj input<simple_mapper; location=loc, prefix=@strcat("cleanTScat_",ss,".allruns+orig.")>;
    ##OUTPUT
    string outname = @strcat("cleanTScat_",ss,".allruns.noijk.txt");
    file outfile<single_file_mapper; file=@strcat(loc,outname)>;
    outfile = Maskdump(pyscript, mask, input, outname, relativeloc);
}