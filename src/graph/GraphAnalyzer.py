from utility_functions import *
import networkx as nx 

"""
    Class to process graphs
"""
class GraphAnalyzer:
    """
        Creates GraphAnalyser object; 
        attributes: 
            G (Graph): the graph loaded through FileReader
            sampled  : if the graph needs to be sampled
    """
    def __init__(self, G, sampled = False):
        self.G = G
        if sampled == True:
            self.G = self.sample_nodes(self.G)
   
    # Returns a vector of tuples with name of the node - degree
    def get_degrees(self, proportion = None, progress = False):
        if progress == True:
            print("\nComputing degrees")
            degrees = []
            for node in tqdm(self.G.nodes(), desc="Calculating degrees", unit="node"):
                degrees.append((node, self.G.degree(node)))
        else:
            degrees = [(node, self.G.degree(node)) for node in self.G.nodes()]
        return degrees

    # Returns a vector of tuples with name of the node - betweenness centrality (normalized) and the poportion used, it considers the number of source nodes to be |V| * proportion
    #Using progress bar for this absolutely kills performances!
    def get_betweenness(self, proportion = None, progress = False):
        if proportion is not None:
            if not (0 < proportion <= 1):
                raise ValueError("The proportion must be '0 < proportion <= 1' or None")
            k = max(1, int(proportion * self.G.number_of_nodes()))  #You shold always take at least one node
        else:
            k = None
        if progress:
            print("\nComputing betweenness centrality")
            betweenness = {}
            for node in tqdm(self.G.nodes(), desc="Calculating betweenness", unit="node"):
                betweenness[node] = nx.betweenness_centrality(self.G, k=k, normalized=True)[node]
        else:
            print("\nComputing betweenness centrality")
            betweenness = nx.betweenness_centrality(self.G, k=k , normalized=True)

        return list(betweenness.items())

    # Returns a vector of tuples with name of the node - PageRank
    #The progress bar for this is unfeasable without redoing the entire nx.pagerank function
    def get_pagerank(self, proportion = None, progress = False):
        if progress:
            print("\nComputing PageRank... progress bar not available")
            pagerank = nx.pagerank(self.G)
        else:
            pagerank = nx.pagerank(self.G)
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
    def get_clustering_coefficient(self, proportion = None, progress = False):
        if progress == True:
            print("\nComputing clustering cefficients")
            clustering_coefficients = {}
            for node in tqdm(self.G.nodes(), desc="Calculating Clustering Coefficient", unit="node"):
                clustering_coefficients[node] = nx.clustering(self.G, node)
        else:
            clustering_coefficients = nx.clustering(self.G)

        return [(node, coefficent) for node, coefficent in clustering_coefficients.items()]

    """
        Computes the friendship paradox occurrences percentage
        returns: 
            the ration between the degree of the node and the average neighbor degree
    """
    def get_friendship_paradox(self, proportion = None, progress=False):
        #get average neighbor degree (for each node)
        avg_neighbor_degree = nx.average_neighbor_degree(self.G)
        friendship_paradox = {}
        print("\nComputing friendship paradox")
        for node, node_degree in tqdm(self.G.degree, desc="Checking for friendship paradox", unit="node"):
            if avg_neighbor_degree[node] == 0:
                friendship_paradox[node] = "undefined"
            else:
                friendship_paradox[node] = node_degree/avg_neighbor_degree[node]
        return friendship_paradox
        
