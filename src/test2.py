import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm

def draw_graph_with_progress(G):
    # Imposta la dimensione della figura per il grafico
    plt.figure(figsize=(10, 10))

    # Ottieni la lista di nodi e archi
    nodes = list(G.nodes())
    edges = list(G.edges())

    # Disegna i nodi e gli archi separatamente per avere un controllo sul progresso
    for i, (node1, node2) in tqdm(enumerate(edges), total=len(edges), desc="Disegnando archi", unit="arco"):
        # Puoi decidere di disegnare l'arco dopo ogni passo (o in batch se è un grafo molto grande)
        nx.draw_networkx_edges(G, pos=nx.spring_layout(G), edgelist=[(node1, node2)], width=1.0, alpha=0.5)

    # Ora disegna i nodi, per farlo separatamente e aggiornare il progresso
    for i, node in tqdm(enumerate(nodes), total=len(nodes), desc="Disegnando nodi", unit="nodo"):
        nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=[node], node_size=100, node_color="blue", alpha=0.7)

    # Aggiungi etichette (se necessario)
    nx.draw_networkx_labels(G, pos=nx.spring_layout(G), font_size=10, font_color="black")

    # Visualizza il grafo
    plt.show()

# Esegui il disegno del grafo con la barra di avanzamento
G = nx.erdos_renyi_graph(100, 0.1)  # Esempio di grafo casuale
draw_graph_with_progress(G)