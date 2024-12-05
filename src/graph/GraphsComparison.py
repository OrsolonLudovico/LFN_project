from graph.graph_helpers import format_values
from graph.GraphVisualizer import GraphVisualizer

class GraphsComparison:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2 
        self.graph_visualizer = GraphVisualizer()
    
    """
        Computes degree for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_degree(self):
        computation = 'Degree'
        g_nodes, g_values, rg_values = format_values(self.data1[computation], self.data2[computation])
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.graph_visualizer.histo_graph_vs_rg(data, "Graph Degree", "Random Graph Degree", "Degree")


    # TO DO : IF TAKES TOO LONG USE SAMPLING
    """
        Computes betweeness centrality for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_avg_betweenness(self) :
        computation = 'Betweeness Centrality'
        g_nodes, g_values, rg_values = self.format_values(self.data1[computation], self.data2[computation])
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.graph_visualizer.histo_graph_vs_rg(data, "Graph BC", "Random Graph BC", "Betweeness centrality")

    """
        Computes page rank for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_pagerank(self) : 
        computation = "Pagerank"
        g_nodes, g_values, rg_values = self.format_values(self.data1[computation], self.data2[computation])
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.graph_visualizer.histo_graph_vs_rg(data, "Graph Pagerank", "Random Graph Pagerank", "Pagerank")

    """
        Computes clustering coefficient for each node for random graph and real graph, 
        and plots the differences in a histogram
    """
    def graph_vs_randomg_clustering_coeff(self) : 
        computation = "Clustering Coefficient"
        g_nodes, g_values, rg_values = self.format_values(self.data1[computation], self.data2[computation])
        data = {
            "dataset_1": g_values,
            "dataset_2": rg_values,
            "categories": g_nodes
        }
        self.graph_visualizer.histo_graph_vs_rg(data, "Graph CC", "Random Graph CC", "Clustering Coefficient")
