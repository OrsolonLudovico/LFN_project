import matplotlib.pyplot as plt
import networkx  as nx
from tqdm import tqdm
import numpy as np

class GraphVisualizer:
    def __init__(self):
        pass

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
        Draws the histogram of data computed from random graph and real graph to show values compared. 
        Suggestion: use sampled graph if too big, otherwise won't work
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