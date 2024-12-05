import networkx as nx
import scipy as sp
import pandas as pd # to use the tables
from tqdm import tqdm
from utility_functions import *
from fileio.file_helpers import get_file_path;

#Creates the file by adding just the row names. The name should cointain .csv
def create_basic_table(G, filename):
    df = pd.DataFrame(index = G.nodes())   #Put the names of the nodes as columns indexes
    save_path = get_file_path(filename, "results")
    df.to_csv(save_path)                    #Save the table in a .csv
    print(filename + " table created")

def add_column(filepath, colname, values):
    #filepath is the path of the file to add the column to
    #colname is the name of teh columns to add
    #values is a vector of tuples with name_of_the_node - value. The names must be the same as the names of the rows

    print("Adding " + colname + " to " + filepath)
    df = pd.read_csv(filepath, index_col=0) #0 means that the first column is the row names
    df.index = df.index.astype(str)
    dict_values = dict(values)                                    #Keep them as strings!!!!!!!!!!!!!!! Very important
    dict_values = {str(k): v for k, v in dict_values.items()}

    missing_keys_n = len(dict_values.keys()) - len(df.index)
    if missing_keys_n != 0:
        print("Missing " + missing_keys_n + " keys error in" + filepath + " exiting: ")
        exit()

    df[colname] = df.index.map(dict_values)
    df.to_csv(filepath)
    print(filepath + " updated")