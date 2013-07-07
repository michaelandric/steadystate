# Density plot of each condition. 
# THIS IS JUST PROOF OF CONCEPT; shows these distances distribute pretty much the same in each condition
# Each condition traces on top of the other in the plot because they're essentially the same
# uses the average gamma and rate parameters from distributions that include all distances ("*distance_noavgs"). 
library(MASS)
library(RColorBrewer)
subjects <- c("ANGO","CLFR","MYTP","TRCO","PIGL","SNNW","LDMW","FLTM","EEPA","DNLN","CRFO","ANMS","MRZM","MRVV","MRMK","MRMC","MRAG","MNGO","LRVN")
conditions <- seq(4)
condition_names = c("Highly ordered", "Some order", "Random", "Almost Random")

thepal = colorRampPalette(brewer.pal(9,"Set2"))(9)
thepalOrder = thepal[c(1,2,4,3)]

shapes <- c()
rates <- c()

for (ss in subjects)
{
    setwd(paste("/mnt/tier2/urihas/Andric/steadystate/",ss,"/corrTRIM_BLUR/", sep=""))
    dd <- read.table(paste("distance_gammafits_",ss,".txt", sep=""), header=T)
    shapes <- c(shapes, dd$shape)
    rates <- c(rates, dd$rate)
}

shapes_mat <- matrix(shapes, nrow = length(subjects), byrow = TRUE)
rates_mat <- matrix(rates, nrow = length(subjects), byrow = TRUE)

b1 <- rgamma(15000000, shape = mean(shapes_mat[,1]), rate = mean(rates_mat[,1]))
b2 <- rgamma(15000000, shape = mean(shapes_mat[,2]), rate = mean(rates_mat[,2]))
b3 <- rgamma(15000000, shape = mean(shapes_mat[,3]), rate = mean(rates_mat[,3]))
b4 <- rgamma(15000000, shape = mean(shapes_mat[,4]), rate = mean(rates_mat[,4]))

xmaxmin <- c()
ymaxmin <- c()
for (i in seq(4))
{
    xmaxmin <- c(xmaxmin, c(range(density(get(paste("b",i,sep="")))$x)))
    ymaxmin <- c(ymaxmin, c(range(density(get(paste("b",i,sep="")))$y)))
}
    
pdf(paste("/mnt/tier2/urihas/Andric/steadystate/groupstats/Distance_density_avg_fit.pdf",sep=""), paper="a4r", width=10.5)
plot(density(b1), xlim = c(range(xmaxmin)), ylim = c(range(ymaxmin)), lwd = 2, col = thepalOrder[1], xlab = "Distance", main = "Distance densities")
lines(density(b2), lwd = 2, col = thepalOrder[2])
lines(density(b3), lwd = 2, col = thepalOrder[3])
lines(density(b4), lwd = 2, col = thepalOrder[4])
dev.off()