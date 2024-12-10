from fileio.GraphReader import GraphReader 
from fileio.FileWriter import FileWriter
from pipeline.Pipeline import Pipeline
from fileio.file_helpers import read_config_file

if __name__ == "__main__":
    #read configuration
    config = read_config_file()

    file_name = config['graph']['input_file']
    input_file = file_name + "." + config['graph']['extension']

    #create graph reader and writer objects
    reader = GraphReader(filename=input_file)
    writer = FileWriter(file_name)

    #start processing pipeline
    pipeline = Pipeline(reader, writer, config)
    pipeline.run()