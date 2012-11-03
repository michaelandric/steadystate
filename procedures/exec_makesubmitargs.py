#!/usr/bin/python

## Here's how you use this on the command line:
## python exec_makesubmitargs.py >> submit.try
## where 'submit.try' is the condor_submit file that you're adding arguments to

import commands
import makesubmitargs

#subjects = ["ANGO"]
#subjects = ["MYTP","TRCO","CLFR","PIGL","SNNW"]
#subjects = ["LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS"]
#subjects = ["MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"]
#subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN"] #CLFR & ANGO not in here
subjects = ["MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EZCR","EEPA","DNLN","CRFO","ANMS","BARS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN","CLFR"] # ANGO not in here
conditions = range(1,5)
## this is the dictionary that maps nvox to subject
dictionary = {'EZCR': '31902', 'FLTM': '32555', 'MRZM': '23081', 'MRMC': '29045', 'ANMS': '25009', 'MRAG': '26830', 'ANGO': '22170', 'PIGL': '26253', 'CLFR': '24883', 'CRFO': '28632', 'EEPA': '30432', 'TRCO': '28705', 'MRMK': '26331', 'SNNW': '27839', 'BARS': '28340', 'LDMW': '27133', 'LRVN': '26562', 'MRVV': '24476', 'DNLN': '25884', 'MYTP': '26202', 'MNGO': '28266'}
## this dictionary gives the highest level (at .5 corr threshold)
#dictionary2 = {'MYTP':(4,3,3,3), 'TRCO':(4,4,4,3), 'CLFR':(4,3,4,3), 'PIGL':(4,4,4,4), 'SNNW':(3,4,3,3)}
dictionary2 = {"LDMW":(,) ,"FLTM":() ,"EZCR":() ,"EEPA":() ,"DNLN":() ,"CRFO":() ,"ANMS":() ,"BARS":()}
hemispheres = ["lh","rh"]



mm = makesubmitargs.makeargs
mm.ijkTALAIRACHcoordsargs("TTavg152T1","automask_d1")

#for ss in subjects:
    #print commands.getoutput("python makesubmitargs.py --subject "+ss) ## for dir maker
    #mm.ijkcoordsargs(ss,"/mnt/tier2/urihas/Andric/steadystate/","automask_d3")
    #print commands.getoutput("python makesubmitargs.py --subject "+ss+" --arg1 /mnt/tier2/urihas/Andric/steadystate/ --arg2 automask_d3") ## for submit.10.getijk
    #mm.autotlrcargs(ss)
    #for cc in conditions:
        #for i in range(dictionary2[ss][cc-1]+1): 
        #print commands.getoutput("python makesubmitargs.py --subject "+ss+" --arg1 "+`cc`) ## this was for submit.splice
        #mm.maskdumpargs(ss,cc)
        #print commands.getoutput("python makesubmitargs.py --subject "+ss+" --arg1 /mnt/tier2/urihas/Andric/steadystate/ --arg2 automask_d3 --arg3 "+`cc`) ## for submit.3.maskdump
        #print commands.getoutput("python makesubmitargs.py --subject "+ss+" --arg1 "+dictionary[ss]+" --arg2 "+`cc`)  ## this is for submit.4.corr
        #mm.threshargs(ss,cc) ## for submit.6.threshold
        #mm.convertargs(ss,cc) ## for submit.7.blondel_convert
        #mm.blondelargs(ss,cc) ## for submit.8.blondel
        #print commands.getoutput("python makesubmitargs.py --subject "+ss+" --arg1 "+`cc`)  ## for submit.6.threshold, submit.7.blondel_convert, submit.8.blondel, submit.9.hierarchy
            #print commands.getoutput("python makesubmitargs.py --subject "+ss+" --arg1 /mnt/tier2/urihas/Andric/steadystate/ --arg2 "+`cc`+" --arg3 "+`i`) ## for submit.11.undump
        #mm.undumpargs(ss,ss+"."+`cc`+".degrees",ss+"."+`cc`+".degrees.ijkSHORT")
        #mm.filter(ss,cc,dictionary2[ss][cc-1]) ## for submit.13.filter
        #mm.undump14(ss,cc,dictionary2[ss][cc-1],1)
        #mm.degree(ss,dictionary[ss],cc)
        #for h in hemispheres:
        #    mm.vol2surfargs(ss, "s"+ss+"_"+h+"_mesh140"+ss+"_"+h+".spec", "s"+ss+"_"+h+"_mesh140"+h+".smoothwm.asc", "s"+ss+"_"+h+"_mesh140"+h+".pial.asc", "max_abs", ss+"."+`cc`+".degrees.ijk+orig.", ss+"."+`cc`+".degrees_"+h+"_max_abs.1D")

