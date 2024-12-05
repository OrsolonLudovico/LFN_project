import math
import numpy as np

"""
    Formats data returned from computations  
    to be used in histograms
"""
def format_values(self, rg_data, g_data):
    rg_dict = dict(rg_data)
    g_dict  = dict(g_data)
    rg_values = rg_dict.values()
    g_nodes = g_dict.keys()
    g_values = g_dict.values()
    return g_nodes, g_values, rg_values

 
"""
    Samples nodes of a graph with a fixed percentage to keep;
    executed only in case of nodes number greater than a specific amount, so as to be able to represent the graph
    attributes: 
        graph (networkx Graph) : graph whose nodes need to be sampled
    returns:
        subgraph of the graph taken as input, with the number of nodes with respect to a fixed percentage
"""
def sample_nodes(graph):
    nodes_number = graph.number_of_nodes()
    if nodes_number > 50000 : 
        print("Sampling nodes...")
        k = 0.00001
        sampling_percentage = max(100 * math.exp(-k * (nodes_number)), 10)
        print("Percentage of nodes used: " + str(sampling_percentage))
        num_nodes_to_sample = int(nodes_number * sampling_percentage / 100)
        num_nodes_to_sample = min(num_nodes_to_sample, nodes_number)
        sampled_nodes = np.random.choice(graph.nodes(), size=num_nodes_to_sample, replace=False)
        newG = graph.subgraph(sampled_nodes)
        print("End sampling nodes.")
        return newG
    return graph