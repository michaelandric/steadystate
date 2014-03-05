## This now includes 'thresh' variable 

## I NEVER ACTUALLY USED THIS SCRIPT.
## SEE 70.community_iterations.py INSTEAD

library(bct)

Args <- Sys.getenv("R_ARGS")
print(noquote(strsplit(Args," ")[[1]]))
subj <- noquote(strsplit(Args," ")[[1]][1])
cond <- as.numeric(noquote(strsplit(Args," ")[[1]][2]))
StartIter <- as.numeric(noquote(strsplit(Args," ")[[1]][3]))
EndIter <- as.numeric(noquote(strsplit(Args," ")[[1]][4]))

threshes <- c(15, 12, 8, 5)

for (linksthresh in threshes)
{
    for (iter in StartIter:EndIter)
    {
        srcdir <- paste(Sys.getenv("state"),"/links_files",linksthresh,"/", sep = "")
        ss_moddir <- paste(Sys.getenv("state"),"/",subj,"/modularity",linksthresh,"/", sep = "")

        srcdst <- paste(srcdir,subj,".",cond,".",linksthresh,"_r0.5_linksthresh_proportion.out.srcdst", sep = "") 
        tree <- paste(ss_moddir,iter,".",subj,".",cond,".",linksthresh,"_r0.5_linksthresh_proportion.out.tree", sep = "")
        modularity_score = blondel_community(srcdst, tree)
        print(modularity_score)

        modout <- paste(ss_moddir,iter,".",subj,".",cond,".",linksthresh,"_r0.5_linksthresh_proportion.mod_score", sep = "")
        write.table(modularity_score, modout, row.names = F, col.names = F, quote = F) 
    }
}

