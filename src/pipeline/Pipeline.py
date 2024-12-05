from graph.GraphAnalyzer import GraphAnalyzer
from graph.RandomGraph import RandomGraph

class Pipeline:
    def __init__(self, graph_file_reader, filewriter, config):
        self.reader = graph_file_reader
        self.writer = filewriter
        self.config = config

    def analyze_graph(self, analyzer):
        results = {}
        for analysis in self.config["analysis"]:
            func = analysis["method"]
            if hasattr(analyzer, func):
                results[analysis["name"]] = getattr(analyzer, func)(progress=analysis["progress"], proportion=analysis["proportion"])
        return results
    
    def run(self):
        """
            GRAPH TO LOAD
        """
        # read graph
        graph = self.reader.load_graph(progress=True)
        # initialize GraphAnalyzer
        print("Analyzing graph loaded...\n*********************")
        analyzer = GraphAnalyzer(graph)
        # call all analysis functions defined in config
        results = self.analyze_graph(analyzer)
        print("End analyzing graph loaded...\n*********************")
        # write results
        print("Writing graph loaded results...\n*********************")
        self.writer.write_file(graph, results)
        print("End writing graph loaded results...\n*********************")

        """
            RANDOM GRAPH
        """
        #create random graph
        print("Analyzing random graph...\n*********************")
        random_graph = RandomGraph(graph)
        #initialize GraphAnalyzer for RandomGraph
        rg_analyzer = GraphAnalyzer(random_graph.G)
        # call all analysis functions defined in config for random graph
        rg_results = self.analyze_graph(rg_analyzer)
        print("End analyzing random graph...\n*********************")
        # write results
        print("Writing random graph results...\n*********************")
        self.writer.write_file(random_graph.G, rg_results, "_random_graph.csv")
        print("End writing random graph results...\n*********************")


    