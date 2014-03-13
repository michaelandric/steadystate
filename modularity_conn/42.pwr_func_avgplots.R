##generate histograms for each person in each condition.
##average histograms across conditions
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
#subjects <- c("ANGO")
conditions <- seq(4)

library(RColorBrewer)
thepal = colorRampPalette(brewer.pal(9,"Set2"))(9)

#library(brainwaver)
cutoff = 1

fitting <- function (degree.dist, nmax) 
{
    n.regions <- length(degree.dist)
    tmp <- hist(degree.dist, breaks = c(0:nmax),plot=F)
    cum.dist <- 1 - cumsum(tmp$counts)/n.regions
    mu <- 1/(sum(degree.dist)/n.regions)
    nb <- length(degree.dist[degree.dist > 0])
    gamma <- 1 + nb/(sum(log(degree.dist[degree.dist > 0])))
    x <- degree.dist
    x <- x[x > 0]
    n <- length(x)
    fn <- function(p) -(-n * p * log(sum(x)/(n * p)) - n * log(gamma(p)) + 
        (p - 1) * sum(log(x)) - n * p)
    out <- nlm(fn, p = 1, hessian = TRUE)
    alpha <- out$estimate
    beta <- sum(degree.dist)/(n.regions * alpha)
    AIC.exp <- -2 * (n.regions * log(mu) - mu * sum(degree.dist)) + 2
    AIC.pow <- -2 * (n.regions * log(gamma - 1) - gamma * sum(log(x))) + 2
    AIC.trunc <- -2 * (-out$minimum) + 2
    fitting <- "mu ="
    fitting <- paste(fitting, mu, sep = " ")
    fitting <- paste(fitting, "gamma = ", sep = "\n")
    fitting <- paste(fitting, gamma, sep = " ")
    fitting <- paste(fitting, "alpha = ", sep = "\n")
    fitting <- paste(fitting, alpha, sep = " ")
    fitting <- paste(fitting, "beta = ", sep = "\n")
    fitting <- paste(fitting, beta, sep = " ")
    fitting <- paste(fitting, "AIC exp = ", sep = "\n")
    fitting <- paste(fitting, AIC.exp, sep = " ")
    fitting <- paste(fitting, "AIC pow = ", sep = "\n")
    fitting <- paste(fitting, AIC.pow, sep = " ")
    fitting <- paste(fitting, "AIC trunc = ", sep = "\n")
    fitting <- paste(fitting, AIC.trunc, sep = " ")
    write.table(fitting, "fitting.txt", row.names = FALSE, col.names = FALSE, 
        quote = FALSE)
    list(mu = mu, gamma = gamma, alpha = alpha, beta = beta)
}


condition_names = c("Highly ordered", "Some order", "Random", "Almost Random")
thepalOrder = thepal[c(1,2,4,3)] 
pdf(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/Vers2deg_distribution_plotsCONDAVGS",cutoff,".pdf",sep=""), paper="a4r", width=10.5)

for (i in conditions)
{
    indiv_counts <-c()
    dat <- c()

    for (ss in subjects)
    {
        setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR",sep=""))
        indiv_counts <- c(indiv_counts, length(as.matrix(read.table(paste(ss,".",i,".degrees_gray",sep="")))))
        dat <- c(dat, as.matrix(read.table(paste(ss,".",i,".degrees_gray",sep=""))))
    }

    deg_max <- max(dat)
    deg_mat <- matrix(nrow=length(subjects),ncol=deg_max-1)
    n = 1

    for (ss in 1:length(subjects))
    {
        current_ss <- dat[n:sum(indiv_counts[1:ss])] 
        current_ss_filtered <- current_ss[which(current_ss > cutoff)] 
        n = n + indiv_counts[ss]
        deg_mat[ss,] <- hist(current_ss_filtered, breaks=c(cutoff:deg_max), plot=F)$counts
    }

    degree.dist = colMeans(deg_mat) ## take the average at each bin
    tmp = hist(degree.dist, breaks=c(cutoff:deg_max),plot=F)
    cum.dist = 1-cumsum(tmp$counts)/length(degree.dist)
    d = fitting(x, deg_max)
    gamma.trace<-1-pgamma((0:nmax),shape=d$alpha,scale=d$beta)
    #Rsq = round((cor(log10(cum.dist)[1:(nmax-1)], log10(gamma.trace)[1:(nmax-1)]))^2, 4)
    plot(log10(cutoff:(deg_max-1)),log10(cum.dist),pch=3,xlab="log(k)",ylab="log(cumulative distribution)", main=paste(condition_names[i]))
    lines(log10(cutoff:(deg_max-1)),log10(gamma.trace)[1:(deg_max-1)], lwd=2, col=thepalOrder[i])
}   

dev.off()

