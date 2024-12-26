import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import linregress, spearmanr, pearsonr

def analyze_friendship_paradox_from_csv(file_path):
    # Reading CSV files
    data = pd.read_csv(file_path, index_col=0)
    data.index = data.index.astype(str)  # Normalize the first column to strings
    data.columns = ['degree', 'betweenness centrality', 'pagerank', 'friendship paradox', 'clustering coefficient']

    # Convert to numeric
    data = data.apply(pd.to_numeric, errors='coerce')

    # Missing data management
    data.dropna(inplace=True)

    # Filter valid values
    #valid_indices = ~data.isnull().any(axis=1)  # Rimuove righe con NaN
    #data = data[valid_indices]

    # Standarditazion (optional)
    #data = (data - data.mean()) / data.std()

    # Extraction of the main columns
    degrees = data['degree'].values
    betweenness = data['betweenness centrality'].values
    pagerank = data['pagerank'].values
    fship_score = data['friendship paradox'].values
    clustering = data['clustering coefficient'].values

    # Statistical analysis of relationships
    analyze_correlation(degrees, betweenness, pagerank, fship_score, clustering)

    # Views
    visualize_data(degrees, betweenness, pagerank, fship_score, clustering)

def analyze_correlation(degrees, betweenness, pagerank, fship_score, clustering):
    metrics = {
        'Degrees' : degrees,
        'page rank' : pagerank,
        'clustering' : clustering
    }

    print("\nStatistical analysis of advanced metrics:")
    for metric_name, metric_values in metrics.items():
        # Linear regression
        slope, intercept, r_value, p_value, std_err = linregress(fship_score, metric_values)

        # Spearman correlation
        spearman_corr, spearman_p = spearmanr(fship_score, metric_values)

        # Kendall Tau
        pearson_corr, pearson_p = pearsonr(fship_score, metric_values)

        # Print results
        print(f"\n{metric_name}:")
        print(f"  Linear Regression:")
        print(f"    Slope (pendenza): {slope:.3f}")
        print(f"    Intercept: {intercept:.3f}")
        print(f"    Coefficiente di correlazione (r): {r_value:.3f}")
        print(f"    p-value: {p_value:.2e}")
        print(f"    Standard error: {std_err:.3f}")
        print(f"  Pearson Correlation: {pearson_corr:.3f} (p={pearson_p:.10e})")
        print(f"  Spearman Correlation: {spearman_corr:.3f} (p={spearman_p:.10e})")

def visualize_data(degrees, betweenness, pagerank, fship_score, clustering):
    plt.figure(figsize=(18, 12))

    # Scatter plot 
    plt.subplot(2, 2, 1)
    plt.scatter(fship_score, degrees, alpha=0.6, edgecolor='k')
    plt.xlabel('Friendship paradox score')
    #plt.xscale('log')
    #plt.yscale('log')
    plt.ylabel('Degree')
    plt.title('Friendship paradox score vs Degree')

    plt.subplot(2, 2, 2)
    plt.scatter(fship_score, pagerank, alpha=0.6, edgecolor='k')
    plt.xlabel('Friendship paradox score')
    #plt.xscale('log')
    #plt.yscale('log')
    plt.ylabel('PageRank')
    plt.title('Friendship paradox score vs PageRank')

    plt.subplot(2, 2, 3)
    plt.scatter(fship_score, clustering, alpha=0.6, edgecolor='k')
    plt.xlabel('Friendship paradox score')
    #plt.xscale('log')
    #plt.yscale('log')
    plt.ylabel('Clustering coefficient')
    plt.title('Friendship paradox score vs Clustering Coefficient')

    #plt.subplot(2, 2, 4)
    #plt.scatter(fship_score, betweenness, alpha=0.6, edgecolor='k')
    #plt.xlabel('Friendship paradox score')
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.ylabel('Betweenness')
    #plt.title('Friendship paradox score vs Betweenness')

    plt.tight_layout()
    plt.show()

# Example
if __name__ == "__main__":
    # Path CSV file containing data
    #file_path = "results/TestGraph.csv"
    file_path = "datasets/facebook.csv"  

    # Analysis of the friendship paradox
    analyze_friendship_paradox_from_csv(file_path)
