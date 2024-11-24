# Learning from networks
## Prerequisites
Python installed
## Installation
1. Clone repository from URL [text](https://github.com/OrsolonLudovico/LFN_project)
2. pip install networkx
3. pip install tqdm 
4. pip install 

## Setup
1. Download the dataset files from [text](https://drive.google.com/drive/folders/1d80utx9j2eaPufLXRG9t5D2kpPsV0fLY?usp=drive_link)
2. Put them in the _datasets_ folder with names _youtube.edges_, _linkedin.edges_, _facebook.edges_
The _.edges_ files contain two columns (representing the connected nodes) per row; each column is seperated by a tab space.
The _facebook_ dataset was formed at the beginning by 4 columns per row. After some analysis we realized that the third column was formed 
only by ones, while the fourth column was either a 0 or a very huge integer, which we realized to be a timestamp, maybe an update in the edge. 
Therefore, we processed the data to keep only the edge information by removing the third and fourth columns, and in case of mulitple connection with different "timestamp" column, we took the one which had the "timestamp" column populated 


// TO ADD  add degree of seperation
