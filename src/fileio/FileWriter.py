import networkx as nx
import scipy as sp
import pandas as pd # to use the tables
from tqdm import tqdm
from utility_functions import *
from fileio.file_helpers import get_file_path;
import os

class FileWriter :
    def __init__(self, filename):
        self.filename = filename
        pass

    #Creates the file by adding just the row names. The name should cointain .csv
    def create_basic_table(self, G, extra_title=""):
        self.file_path = get_file_path(self.filename + extra_title + ".csv", "results")
        df = pd.DataFrame(index = G.nodes())   #Put the names of the nodes as columns indexes
        df.to_csv(self.file_path)                   #Save the table in a .csv
        print(self.filename + " table created")

    def add_column(self, colname, values, extra_title):
        #filepath is the path of the file to add the column to
        #colname is the name of teh columns to add
        #values is a vector of tuples with name_of_the_node - value. The names must be the same as the names of the rows
        self.file_path = get_file_path(self.filename + extra_title + ".csv", "results")
        print("Adding " + colname + " to " + self.file_path)
        
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} not found, creating a new file...")
            df = pd.DataFrame(index=[str(k) for k, v in values])  # Use nodes as index
            df.to_csv(self.file_path)

        df = pd.read_csv(self.file_path, index_col=0) #0 means that the first column is the row names
        df.index = df.index.astype(str)
        dict_values = dict(values)                                    #Keep them as strings!!!!!!!!!!!!!!! Very important
        dict_values = {str(k): v for k, v in dict_values.items()}

        missing_keys_n = len(dict_values.keys()) - len(df.index)
        if missing_keys_n != 0:
            print(f"Missing {missing_keys_n} keys error in {self.file_path}, exiting.")
            exit()

        df[colname] = df.index.map(dict_values)
        df.to_csv(self.file_path)
        print(self.file_path + " updated")