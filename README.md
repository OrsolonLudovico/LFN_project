# Learning from networks
## Prerequisites
Python installed
## Installation
1. Clone repository from URL [GITHUB](https://github.com/OrsolonLudovico/LFN_project)
2. pip install networkx
3. pip install tqdm 
4. pip install matplotlib
5. pip install scipy
6. pip install pandas 
7. pip install PyYAML

## Setup
1. Download the dataset files from [DATASET LINK](https://drive.google.com/drive/folders/1d80utx9j2eaPufLXRG9t5D2kpPsV0fLY?usp=drive_link)
2. Put them in the _datasets_ folder with names _youtube.edges_, _linkedin.edges_, _facebook.edges_
The _.edges_ files contain two columns (representing the connected nodes) per row; each column is seperated by a tab space.
The _facebook_ dataset was formed at the beginning by 4 columns per row. After some analysis we realized that the third column was formed 
only by ones, while the fourth column was either a 0 or a very huge integer, which we realized to be a timestamp, maybe an update in the edge. 
Therefore, we processed the data to keep only the edge information by removing the third and fourth columns, and in case of mulitple connection with different "timestamp" column, we took the one which had the "timestamp" column populated 
3. Use the _config.yaml_ file in _config_ folder to configure parameters; the variable parameters are the followings:
    ```yaml
    graph:
        input_file: "facebook"  #graph input file
        extension: "edges"      #extension of the input file

    analysis: 
      #each element is a property to compute, and it is composed by
      #name: string, the title of the property
      #method: string, the function to execute
      #proportion: 0 < proportion < 1 is the percentage of nodes to take into consideration (if too slow computation) 
      #progress: bool, if you want to keep track of computation progresses; sometimes not possible
    - name: "Degree"
      method: "get_degrees"
      proportion: null
      progress: True
    - name: "Betweenness Centrality"
      method: "get_betweenness" 
      proportion: 0.02 
      progress: False
    - name: "Page Rank"
      method: "get_pagerank"
      proportion: null
      progress: True
    - name: "Clustering Coefficient"
      method: "get_clustering_coefficient"
      proportion: 0.2
      progress: True
    ``` 

## Notes
Another experiment that we decided to conduct is the degree of separation.
