pov <- c('DAVOS', 'REEK', 'VICTARION', 'SANSA', 'BRIENNE', 'MELISANDRE', 'EDDARD', 'TYRION', 'SAMWELL', 'CERSEI', 'ALAYNE', 'JAIME', 'CATELYN', 'DAENERYS', 'THEON', 'ARYA', 'BRAN', 'JON')
col <- c(517, 83, 42, 477, 284, 78, 239, 1200, 380, 386, 76, 534, 483, 1242, 198, 655, 609, 1318)
cp <- array(col, dimnames=list(pov))
plot(cp, type="h", xaxt="n")
axis(1, at=seq(1:18), labels=pov)

png(file="/home/boris/Work/Martin_tutorial/code/colors/plot_all_POV.png", width=1550 , height=500)
plot(md, type="h", xaxt="n")
axis(1, at=seq(1:18), labels=pov)
dev.off()

pov1 <- c("Davos", "Reek", "Victarion", "Sansa", "Brienne", "Melisandre", "Eddard", "Tyrion", "Samwell", "Cersei", "Alayne", "Jaime", "Catelyn", "Daenerys", "Theon", "Arya", "Bran", "Jon")
col1 <- c(0.0165170441839, 0.0101059296238, 0.0216383307573, 0.0108569477637, 0.0114474585836, 0.0270083102493, 0.0088172360363, 0.0107664839355, 0.013764624914, 0.0108907259543, 0.00881670533643, 0.0126396515811, 0.00995650471027, 0.0146327670303, 0.0106583409593, 0.0115795986918, 0.0136749449859, 0.0124022546132)
cp1 <- array(col1, dimnames=list(pov1))
plot(cp1, type="h", xaxt="n")
axis(1, at=seq(1:18), labels=pov1)

png(file="/home/boris/Work/Martin_tutorial/code/colors/plot_rel_POV.png", width=1550 , height=500)
plot(cp1, type="h", xaxt="n")
axis(1, at=seq(1:18), labels=pov1)
dev.off()

# variety

povvar <- c("Davos", "Reek", "Victarion", "Sansa", "Brienne", "Melisandre", "Eddard", "Tyrion", "Samwell", "Cersei", "Alayne", "Jaime", "Catelyn", "Daenerys", "Theon", "Arya", "Bran", "Jon")
colvar <- c(25, 10, 9, 27, 18, 11, 20, 30, 17, 21, 13, 26, 22, 36, 14, 19, 18, 27)
cp2 <- array(colvar, dimnames=list(povvar))
plot(cp2, type="h", xaxt="n")
axis(1, at=seq(1:18), labels=povvar)

png(file="/home/boris/Work/Martin_tutorial/code/colors/plot_var_POV.png", width=1550 , height=500)
plot(cp2, type="h", xaxt="n")
axis(1, at=seq(1:18), labels=povvar)
dev.off()

# Tyrion color variation

tyr <- c(3, 7, 6, 6, 9, 2, 8, 13, 6, 9, 6, 10, 9, 8, 8, 7, 4, 10, 8, 5, 6, 10, 9, 11, 8, 11, 12, 3, 16, 13, 7, 6, 18, 13, 8, 14, 10, 11, 13, 14, 12, 11, 11, 6)

mt <- mean(tyr)
mt
mdt <- median(tyr)
mdt

mdt_p <- c(9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)

# tyr[29]
# Буря мечей, Тирион 5
# В Тирион 4 -- последняя встреча с Шаей перед женитьбой на Сансе
# В Тирион 5 -- приезд Оберина в Королевскую Гавань

plot(tyr, type='b')
lines(mdt_p, type='l', col='blue')


png(file="/home/boris/Work/Martin_tutorial/code/colors/plot_var_Tyrion.png", width=1550 , height=500)
plot(tyr, type='b')
lines(mdt_p, type='l', col='blue')
dev.off()