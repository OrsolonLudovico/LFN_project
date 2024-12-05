import networkx  as nx
from graph.graph_helpers import sample_nodes

class RandomGraph:
    """
        Creates RandomGraph object; 
        initializes random graph G with the same number of nodes and edges as real graph, based on read graph G
        attributes: 
            filename (string): the name of the dataset to be read (with extension)
    """
    def __init__(self, loaded_graph, sampled = False):
        self.G = nx.gnm_random_graph(loaded_graph.number_of_nodes(), loaded_graph.number_of_edges())
        if sampled ==  True:
            self.G = sample_nodes(self.G)

        