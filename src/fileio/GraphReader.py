import networkx as nx
from fileio.file_helpers import get_file_path
from tqdm import tqdm

class GraphReader :
    def __init__(self, filename):
        self.filename = filename

    # Loads the data
    def load_graph(self, progress = False):
        data_path = get_file_path(self.filename, 'datasets')
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