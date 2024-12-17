import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.stats import spearmanr, kendalltau

def analyze_friendship_paradox_from_csv(file_path):
    # Reading CSV files
    data = pd.read_csv(file_path, index_col=0)
    data.index = data.index.astype(str)  # Normalize the first column to strings
    data.columns = ['degree', 'betweenness centrality', 'pagerank', 'friendship paradox']

    # Converti in numerico
    data = data.apply(pd.to_numeric, errors='coerce')

    print(data)


    # Filtra valori validi
    valid_indices = ~data.isnull().any(axis=1)  # Rimuove righe con NaN
    data = data[valid_indices]

    # Extraction of the main columns
    degrees = data['degree'].values
    betweenness = data['betweenness centrality'].values
    pagerank = data['pagerank'].values
    fship_score = data['friendship paradox'].values

    # Statistical analysis of relationships
    analyze_correlation(degrees, betweenness, pagerank, fship_score)

    # Views
    visualize_data(degrees, betweenness, pagerank, fship_score)

def analyze_correlation(degrees, betweenness, pagerank, fship_score):
    metrics = {
        'Betweenness Centrality': betweenness,
        'PageRank': pagerank, 
    }

    print("\nStatistical analysis of advanced metrics:")
    for metric_name, metric_values in metrics.items():
        # Linear regression
        slope, intercept, r_value, p_value, std_err = linregress(fship_score, metric_values)

        # Spearman correlation
        spearman_corr, spearman_p = spearmanr(fship_score, metric_values)

        # Kendall Tau
        kendall_corr, kendall_p = kendalltau(fship_score, metric_values)

        # Print results
        print(f"\n{metric_name}:")
        print(f"  Linear Regression:")
        print(f"    Slope (pendenza): {slope:.3f}")
        print(f"    Intercept: {intercept:.3f}")
        print(f"    Coefficiente di correlazione (r): {r_value:.3f}")
        print(f"    p-value: {p_value:.3f}")
        print(f"    Standard error: {std_err:.3f}")
        print(f"  Spearman Correlation: {spearman_corr:.3f} (p={spearman_p:.3f})")
        print(f"  Kendall Tau: {kendall_corr:.3f} (p={kendall_p:.3f})")

def visualize_data(degrees, betweenness, pagerank, fship_score):
    plt.figure(figsize=(18, 12))

    # Scatter plot 
    plt.subplot(2, 2, 1)
    plt.scatter(fship_score, betweenness, alpha=0.6, edgecolor='k')
    plt.xlabel('Friendship paradox score')
    plt.ylabel('Betweenness Centrality')
    plt.title('Friendship paradox score vs Betweenness Centrality')

    plt.subplot(2, 2, 2)
    plt.scatter(fship_score, pagerank, alpha=0.6, edgecolor='k')
    plt.xlabel('Friendship paradox score')
    plt.ylabel('PageRank')
    plt.title('Friendship paradox score vs PageRank')

    plt.tight_layout()
    plt.show()

# Example
if __name__ == "__main__":
    # Path CSV file containing data
    file_path = "results/TestGraph_random_graph.csv"  # Sostituisci con il percorso reale del file

    # Analysis of the friendship paradox
    analyze_friendship_paradox_from_csv(file_path)
