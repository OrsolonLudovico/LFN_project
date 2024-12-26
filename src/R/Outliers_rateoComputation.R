#name <- "../results/youtube.csv" 
name <- "../../results/random/TestGraph_random_graph.csv"
df <- read.csv(name)

vector <- df[["Friendship.paradox"]]
num_greater_than_1 <- sum(vector > 1)
#print(paste("Num > 1 ", num_greater_than_1))
num_total_elements <- length(vector)
#print(paste("total ",num_total_elements))
ratio <- num_greater_than_1 / num_total_elements
print(paste("Rateo of ", name, " ",  ratio))