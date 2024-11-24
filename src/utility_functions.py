import matplotlib.pyplot as plt
import networkx as nx
from tqdm import tqdm
import scipy as sp

# Draws the graph 
def draw_graph(G, progress = False):
    #show the progress bar if progress = true

    if progress == True:
        print("\nDrawing graph")
        plt.figure(figsize=(8, 8))
        pos = nx.spring_layout(G, seed = 123)       #set seed for consistency
        nodes = list(G.nodes())
        edges = list(G.edges())

        # Draw the edges
        for i, (node1, node2) in tqdm(enumerate(edges), total=len(edges), desc="Drawing edges", unit="edge"):
            nx.draw_networkx_edges(G, pos, edgelist=[(node1, node2)])
        # Draw the nodes
        for i, node in tqdm(enumerate(nodes), total=len(nodes), desc="Drawing nodes", unit="node"):
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=500, node_color="lightblue")
        # Add labels
        nx.draw_networkx_labels(G, pos, font_size= 10, font_color="black")
        plt.show()
    else:
        plt.figure(figsize=(8, 8))
        pos = nx.spring_layout(G, seed=123)         #set seed for consistency
        nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_color="black")
        plt.show()

# Loads the data
def load_graph(data_path, progress = False):

    #Monitor the process, if progress = true shows the progress bar

    if progress == True:
        print("\nReading graph at " + data_path)
        def file_generator_with_progress(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                total_lines = sum(1 for line in f)
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in tqdm(f, total=total_lines, desc="Loading graph"):
                    yield line
        #Generate the graph
        G = nx.read_edgelist(file_generator_with_progress(data_path), comments='#', encoding='utf-8')
    else:
        G = nx.read_edgelist(data_path, comments='#', encoding='utf-8')

    return G

# Returns a vector of tuples with name of the node - degree
def get_degrees(G, progress = False):
    if progress == True:
        print("\nComputing degrees")
        degrees = []
        for node in tqdm(G.nodes(), desc="Calculating degrees", unit="node"):
            degrees.append((node,G.degree(node)))
    else:
        degrees = [(node, G.degree(node)) for node in G.nodes()]
    return degrees

# Returns a vector of tuples with name of the node - betweenness centrality (normalized) and the poportion used, it considers the number of source nodes to be |V| * proportion
#Using progress bar for this absolutely kills performances!
def get_betweenness(G, proportion = None, progress = False):

    if proportion is not None:
        if not (0 < proportion <= 1):
            raise ValueError("The proportion must be '0 < proportion <= 1' or None")
        k = max(1, int(proportion * G.number_of_nodes()))  #You shold always take at least one node
    else:
        k = None


    if progress:
        print("\nComputing betweenness centrality")
        betweenness = {}
        for node in tqdm(G.nodes(), desc="Calculating betweenness", unit="node"):
            betweenness[node] = nx.betweenness_centrality(G, k=k, normalized=True)[node]
    else:
        betweenness = nx.betweenness_centrality(G, k=k , normalized=True)

    return list(betweenness.items()) , k

# Returns a vector of tuples with name of the node - PageRank
#The progress bar for this is unfeasable without redoing the entire nx.pagerank function
def get_pagerank(G, progress = False):
    if progress:
        print("\nComputing PageRank... progress bar not aviable")
        pagerank = nx.pagerank(G)
    else:
        pagerank = nx.pagerank(G)
    return list(pagerank.items())

# Returns a vector of tuples with name of the node - closeness centrality

########I can't figue out how to approximate this
'''
def get_closeness(G, progress=False):
    if progress:
        print("\nComputing closeness centrality")
        closeness = {}
        for node in tqdm(G.nodes(), desc="Calculating closeness", unit="node"):
            closeness[node] = nx.closeness_centrality(G)[node]
    else:
        closeness = nx.closeness_centrality(G)
    return list(closeness.items())
'''

#Returns a vector of touples name of the node - clustering coefficient
#Using the progress bar doesn't impact performances too much, doesn't need to be approximated, calculates the coefficient for any graph
def get_clustering_coefficient(G, progress = False):

    if progress == True:
        print("\nComputing clustering cefficients")
        clustering_coefficients = {}
        for node in tqdm(G.nodes(), desc="Calculating Clustering Coefficient", unit="node"):
            clustering_coefficients[node] = nx.clustering(G, node)
    else:
        clustering_coefficients = nx.clustering(G)

    return [(node, coefficent) for node, coefficent in clustering_coefficients.items()]