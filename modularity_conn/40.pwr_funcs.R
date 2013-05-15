##generate histograms for each person in each condition.
##average histograms across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
#subjects <- c("CLFR")
conditions <- seq(4)

library(RColorBrewer)
thepal = colorRampPalette(brewer.pal(9,"Set2"))(9)

library(brainwaver)

deg_func <- function(x)
{
    degree.dist = x[which(x > 1)]
    nmax = max(degree.dist)
    tmp = hist(degree.dist, breaks=c(0:nmax))
    Fn = ecdf(tmp$counts)
    d = fitting(x, nmax)
    ptshape = d$alpha + d$gamma
    gamma.trace <- log10(1-pgamma((0:(nmax-1)),shape=ptshape,scale=d$beta))
    v1 = log10(Fn(tmp$counts))
    Rsq = round((cor(v1,gamma.trace))^2, 4)

    #return(list(gamma.trace, v1, Rsq))
    return(list("gamma.trace"=gamma.trace, "log10cnts"=v1, "Rsq"=Rsq, "nmax"=nmax, "shape"=ptshape))
}

condition_names = c("Highly ordered", "Some order", "Random", "Almost Random")
thepalOrder = thepal[c(1,2,4,3)] 

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR",sep=""))
    dat <- c()
    for (i in conditions)
    {
        dat <- c(dat, as.matrix(read.table(paste(ss,".",i,".degrees_gray",sep=""))))
    }
    dat_matrix <- matrix(dat, ncol=4)
    pdf("deg_distribution_plots.pdf")
    rsquares <- c()
    for (i in conditions)
    {
        out = deg_func(dat_matrix[,i])
        rsquares = c(rsquares, out$Rsq)
        plot(log10(0:(out$nmax-1)), out$log10cnts, main=condition_names[i])
        lines(log10(0:(out$nmax-1)), out$gamma.trace, col=thepalOrder[i],lwd=2)
    }
    dev.off()
    rsquared_mat = matrix(rsquares, nrow=1, byrow=T)
    write.table(rsquared_mat, paste("Rsq_vals",ss,".txt",sep=""), row.names=F,col.names=F,quote=F)
}

