#We have to find a way to translate the graphs into rapresentations with networkx
from utility_functions import *
from networkx import *
import os

script_dir  = os.path.dirname(os.path.abspath(__file__))
data_path   = os.path.join(script_dir, "../datasets/TestGraph.txt")
#data_path   = os.path.join(script_dir, "../datasets/linkedin.edges")
#data_path   = os.path.join(script_dir, "../datasets/facebook.edges")
#data_path   = os.path.join(script_dir, "../datasets/youtube.edges")


#This will put the graph from the path
G = load_graph(data_path, progress= True)

#Draw the graph (not feasable with large graphs)
#draw_graph(G, progress= True)

#Get tuples with node name - degree
degrees = get_degrees(G, progress= True)
print(degrees)

#Some ideas:
#Some centrality measures (betweenness, PageRank, closeness ...)
#Graphlets
#Random Graphs

#Add everything togheder in a .csv file