import matplotlib.pyplot as plt
import networkx as nx
from tqdm import tqdm

#Draws the graph 
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

#Loads the data
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

#Returns a vector of tuples with name of the node - degree
def get_degrees(G, progress = False):
    if progress == True:
        print("\nComputing degrees")
        degrees = []
        for node in tqdm(G.nodes(), desc="Calculating degrees", unit="node"):
            degrees.append((node,G.degree(node)))
    else:
        degrees = [(node, G.degree(node)) for node in G.nodes()]
    return degrees

#Add functions here