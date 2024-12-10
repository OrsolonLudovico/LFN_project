from graph.GraphAnalyzer import GraphAnalyzer
from graph.RandomGraph import RandomGraph

class Pipeline:
    def __init__(self, graph_file_reader, filewriter, config):
        self.reader = graph_file_reader
        self.writer = filewriter
        self.config = config

    def write_graph_result(self, result, analysis, extra_title):
        # write results
        print("*************************\nWriting {:s} result...\n*************************" . format(analysis["name"]))
        self.writer.add_column(analysis["name"], result, extra_title)
        print("*************************\nEnd writing {:s} result...\n*************************" . format(analysis["name"]))

    def analyze_graph(self, analyzer, extra_title = ""):
        results = {}
        for analysis in self.config["analysis"]:
            func = analysis["method"]
            if hasattr(analyzer, func):
                # analysis of function specified
                result = getattr(analyzer, func)(progress=analysis["progress"], proportion=analysis["proportion"])
                if result != None : 
                    self.write_graph_result(result, analysis, extra_title)
        return results
    
    # def analyze_graph(self, args):
    #     analysis, analyzer = args
    #     func = analysis["method"]
    #     if hasattr(analyzer, func):
    #         result = getattr(analyzer, func)(progress=analysis["progress"], proportion=analysis["proportion"])
    #         if result is not None:
    #             self.write_graph_result(result, analysis)
    
    # def parallelize_processes(self, analyzer):
    #     #define the tasks for computations to be done (all the functions to compute)
    #     computations = [(analysis, analyzer) for analysis in self.config["analysis"]]
    #     #define the number of parallel processes to run: take the minimum between the number of cores and the number of functions called
    #     #in this way if enough cores, each function is called separately
    #     num_computations = len(computations)
    #     num_processes = 1#min(num_computations, os.cpu_count())
    #     with Pool(processes=num_processes) as pool:
    #         pool.map(self.analyze_graph, computations)
    
    def run(self):
        """
            GRAPH TO LOAD
        """
        # read graph
        graph = self.reader.load_graph(progress=True)
        if(self.config["only_random_graph"] == False):
            # initialize GraphAnalyzer
            print("*********************\nAnalyzing graph loaded...\n*************************")
            analyzer = GraphAnalyzer(graph)
            if(self.config["create_new_file"] == True):
                self.writer.create_basic_table(graph)
            # call all analysis functions defined in config
            self.analyze_graph(analyzer)

        """
            RANDOM GRAPH
        """
        #create random graph
        if(self.config["random_graph"] == True):
            print("*********************\nAnalyzing random graph...\n*********************")
            random_graph = RandomGraph(graph)
            #initialize GraphAnalyzer for RandomGraph
            rg_analyzer = GraphAnalyzer(random_graph.G)
            if(self.config["create_new_file_random_graph"] == True):
                self.writer.create_basic_table(random_graph.G, "_random_graph")
            # call all analysis functions defined in config for random graph
            self.analyze_graph(rg_analyzer, "_random_graph")

    