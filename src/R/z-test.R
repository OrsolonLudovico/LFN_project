#This script performs the z-test on two files on the "Frienship paradox column"
name1 <- "../../results/facebook.csv"
df1 <- read.csv(name1)
name2 <- "../../results/youtube.csv"
df2 <- read.csv(name2)

v1 <- df1[["Friendship.paradox"]]
v2 <- df2[["Friendship.paradox"]]

#number of values greater than 1
k1 <- sum(v1 > 1)
k2 <- sum(v2 > 1)

#number of values
n1 <- length(v1)
n2 <- length(v2)

#proportions
p1 <- k1 / n1
p2 <- k2 / n2

#combinated proportion
p_comb <- (k1 + k2) / (n1 + n2)

#z-test statistic
z <- (p1 - p2) / sqrt(p_comb * (1 - p_comb) * (1/n1 + 1/n2))

#p-value (two tail)
p_value <- 2 * (1 - pnorm(abs(z)))

# Visualizza i risultati
cat("z statistic:", z, "\n")
cat("p-value:", p_value, "\n")

# Confronto con il livello di significatività alpha (ad esempio, 0.05)
alpha <- 0.01
if (p_value < alpha) {
  cat("Reject HO, proportions are different.\n")
} else {
  cat("Can't reject H0, proportions are too similar.\n")
}

#Verify histograms to asses p-value validity

#hist(v1, main = "Distribuzione Friendship.paradox (Dataset 1)", 
#     xlab = "Friendship.paradox", col = "skyblue", border = "black", 
#     breaks = 30, xlim = range(c(v1, v2)))

#hist(v2, main = "Distribuzione Friendship.paradox (Dataset 2)", 
#     xlab = "Friendship.paradox", col = "lightgreen", border = "black", 
#     breaks = 30, xlim = range(c(v1, v2)))
