import os;
from utility_functions import *
import networkx  as nx
import numpy as np
import math

"""
    Class to load and process graphs
"""
class GraphAnalyser:
    """
        Creates GraphAnalyser object; 
        initializes GraphAnalyser graph G, given the name of the edges file
        attributes: 
            filename (string): the name of the dataset to be read (with extension)
    """
    def __init__(self, filename):
        self.G = self.get_graph_from_file_path(filename)
        #if number of nodes > 50000 sample them
        self.G = self.sample_nodes(self.G)
        self.degree = get_degrees(self.G)
    """
        Returns : 
            full file path of dataset, given a filename
    """
    def get_file_path(self, filename):
        script_dir  = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, "..", "datasets", filename)

    """
        Returns :
            a NetworkX graph, given a filename
    """
    def get_graph_from_file_path(self, filename) : 
        return load_graph(self.get_file_path(filename), progress=True)

    """
        Sets random graph in current class randomG attribute; 
        the random graph is instantiated with the same number of nodes and edges as real graph
    """
    def generate_random_graph(self) : 
        self.randomG = nx.gnm_random_graph(self.G.number_of_nodes(), self.G.number_of_edges())
        self.randomG = self.sampleNodes(self.randomG)

    """
        Draws the histogram of data computed from random graph and real graph to show values compared
        attributes :
            - data['dataset_1'] : data from random graph
            - data['dataset_2'] : data from real graph
            - data['categories'] : nodes in the graph
            - data1Title : title of first dataset
            - data2Title : title of second dataset
            - values_title : title of the y-axis
    """
    def histo_graph_vs_rg(self, data, data1Title, data2Title, values_title):
        bar_width = 0.3
        x = np.arange(len(data["dataset_1"]))
        plt.bar(x - bar_width/2, data["dataset_1"], width=bar_width, label=data1Title, color='blue', alpha=0.7)
        plt.bar(x + bar_width/2, data["dataset_2"], width=bar_width, label=data2Title, color='orange', alpha=0.7)
        plt.xlabel('Nodes')
        plt.ylabel(values_title)
        plt.title(data1Title + " vs " + data2Title)
        plt.xticks(ticks=x, labels=data["categories"])
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    """
        Samples nodes of a graph with a fixed percentage to keep;
        executed only in case of nodes number greater than a specific amount, so as to be able to represent the graph
        attributes: 
            graph (networkx Graph) : graph whose nodes need to be sampled
        returns:
            subgraph of the graph taken as input, with the number of nodes with respect to a fixed percentage
    """
    def sample_nodes(self, graph):
        nodes_number = graph.number_of_nodes()
        print(nodes_number)
        if nodes_number > 500000 : 
            print("Sampling nodes...")
            k = 0.00001
            sampling_percentage = max(100 * math.exp(-k * (nodes_number - 500000)), 10)
            print("Percentage of nodes used: " + str(sampling_percentage))
            num_nodes_to_sample = int(nodes_number * sampling_percentage / 100)
            num_nodes_to_sample = min(num_nodes_to_sample, nodes_number)
            sampled_nodes = np.random.choice(graph.nodes(), size=num_nodes_to_sample, replace=False)
            newG = graph.subgraph(sampled_nodes)
            print("End sampling nodes.")
            return newG
        return graph

    """
        Draws multiple graphs in a single figure, given a list of graphs
        attributes: 
            graphs (list of networkx Graph) : list of graphs to be drawn
    """
    def draw_multi_graphs(self,graphs):
        #find corresponding rows and columns to plot figures
        columns = int(np.ceil(len(graphs) / 4))
        rows = int(np.ceil(len(graphs) / columns))
        fig, axs = plt.subplots(rows, columns)
        axs = axs.flatten()
        # draw graph in its part
        for i, graph in enumerate(graphs):
            print("Drawing graph " + str(i))
            nx.draw(graph, ax=axs[i], with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
            axs[i].set_title(f"Grafo {i+1}")

        # remove empty parts
        for j in range(i + 1, len(axs)):
            axs[j].axis('off')
            
        plt.tight_layout() 
        plt.show()

    """
        Formats data returned from computations in utilites_functions 
        to be used in histograms
    """
    def format_values(self,rg_data, g_data):
        rg_dict = dict(rg_data)
        g_dict  = dict(g_data)
        rg_values = rg_dict.values()
        g_nodes = g_dict.keys()
        g_values = g_dict.values()
        return g_nodes, g_values, rg_values

    """
        Computes degree for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_degree(self) : 
        rg_degree = get_degrees(self.randomG, False)
        g_degree  = get_degrees(self.G, False)
        self.g_degree = g_degree
        self.rg_degree = rg_degree
        g_nodes, g_values, rg_values = self.format_values(rg_degree, g_degree)
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.histo_graph_vs_rg(data, "Graph Degree", "Random Graph Degree", "Degree")


    # TO DO : IF TAKES TO LONG USE SAMPLING
    """
        Computes betweeness centrality for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_avg_betweenness(self) :
        rg_betweeness = get_betweenness(self.randomG, False)
        g_betweeness  = get_betweenness(self.G, False)
        g_nodes, g_values, rg_values = self.format_values(rg_betweeness, g_betweeness)
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.histo_graph_vs_rg(data, "Graph BC", "Random Graph BC", "Betweeness centrality")
    """
        Computes page rank for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_pagerank(self) : 
        rg_pagerank = get_pagerank(self.randomG, False)
        g_pagerank  = get_pagerank(self.G, False)
        g_nodes, g_values, rg_values = self.format_values(rg_pagerank, g_pagerank)
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.histo_graph_vs_rg(data, "Graph Pagerank", "Random Graph Pagerank", "Pagerank")
    """
        Computes clustering coefficient for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_clustering_coeff(self) : 
        rg_cc = get_clustering_coefficient(self.randomG, False)
        g_cc  = get_clustering_coefficient(self.G, False)
        g_nodes, g_values, rg_values = self.format_values(rg_cc, g_cc)
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.histo_graph_vs_rg(data, "Graph CC", "Random Graph CC", "Clustering coefficient")

    """
        Computes the friendship paradox occurrences
        returns: 
            tuple containing the friendship paradox occurences and the total numberof nodes in the graph
    """
    def friendship_paradox_occurences(self):
        avg_neighbor_degree = nx.average_neighbor_degree(self.G)
        friendship_paradox_occ = 0
        for node, node_degree in self.degree:
            if node_degree < avg_neighbor_degree[node]:
                friendship_paradox_occ += 1
        return friendship_paradox_occ, self.G.number_of_nodes()

