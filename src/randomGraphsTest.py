from GraphAnalyser import GraphAnalyser;
from utility_functions import *;
import os

a = GraphAnalyser(filename="TestGraph.txt")
# a.generate_random_graph()
# a.draw_multi_graphs(graphs=[a.randomG, a.G])
# a.graph_vs_randomg_degree()
print(a.friendship_paradox_occurences())
