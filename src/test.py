#We have to find a way to translate the graphs into rapresentations with networkx
from utility_functions import *
from networkx import *
from data_manager import *
from graph.GraphAnalyzer import GraphAnalyser;
from fileio.file_helpers import get_file_path;
import os

if __name__ == "__main__":

    script_dir  = os.path.dirname(os.path.abspath(__file__))
    #data_path   = os.path.join(script_dir, "../datasets/TestGraph.txt")
    data_path   = os.path.join(script_dir, "../datasets/linkedin.edges")
    #data_path   = os.path.join(script_dir, "../datasets/facebook.edges")
    #data_path   = os.path.join(script_dir, "../datasets/youtube.edges")


    #This will put the graph from the path
    G = load_graph(data_path, progress=True)

    #Draw the graph (not feasable with large graphs)
    #draw_graph(G, progress= True)

    #Get tuples with node name - degree
    #degrees = get_degrees(G, progress= True)
    #print(degrees)

    # Betweenness (unfeasable with lage graphs exactly)   #2 min with 0.005 #35 min with 0.005
    #betweenness, k = get_betweenness(G, proportion = 0.005)
    #print(betweenness)
    

    # PageRank
    #page_rank = get_pagerank(G, True)
    #print(page_rank)
    # Closeness Centrality (unfeasable with large graphs, need to figure out how to approximate)
    #closeness = get_closeness(G, True)
    #print(closeness)

    #clustering_coef = get_clustering_coefficient(G, progress=True)
    #print(cls_coef)


##WARNING change G to the graph you want before testing
#TEST
    #create_basic_table(G, "TestGraph.csv")
    #add_column("../results/TestGraph.csv","degree",get_degrees(G, progress=True))
#FACEBOOK
    #create_basic_table(G, "facebook.csv")
    #print(len(G.nodes()))
    #add_column("../results/facebook.csv","degree",get_degrees(G, progress=True))
#YOUTUBE
    #create_basic_table(G, "Youtube.csv")
    #add_column("../results/Youtube.csv","degree",get_degrees(G, progress=True))
#LINKEDIN
    create_basic_table(G, "Linkedin.csv")
    add_column("../results/Linkedin.csv","degree",get_degrees(G , progress=True))