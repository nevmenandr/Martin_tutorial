cities <- read.csv("/home/boris/Work/Martin_tutorial/code/word2vec/table_dist.csv")
cityDist <- as.matrix(cities[,2:11], ncol = 10);
rownames(cityDist) <- cities[,1];
plot(cityDist, pch = "")
text(cityDist, rownames(cityDist))

png(file="/home/boris/Work/Martin_tutorial/code/word2vec/geo_vec.png", width=800 , height=800)
plot(cityDist, pch = "")
text(cityDist, rownames(cityDist))
dev.off()