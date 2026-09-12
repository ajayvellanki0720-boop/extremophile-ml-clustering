import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading genomic signatures...")
# Load the dataset
df = pd.read_csv('genomic_signatures.csv')

# Separate the filenames from the numerical k-mer data
filenames = df['filename']
X = df.drop('filename', axis=1)

print("Running K-Means Clustering and PCA...")
# Group the data into 3 mathematical clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X)

# Reduce the 4,096 dimensions down to 2 dimensions for plotting
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X)

# Create a new dataframe for visualization
plot_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
plot_df['Cluster'] = clusters
plot_df['Genome'] = filenames

# Plot the results
plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', palette='viridis', data=plot_df, s=100)
plt.title('Genomic Signatures of Extremophiles (PCA)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

# Save the plot as an image file
plt.savefig('cluster_plot.png')
print("Success! Open 'cluster_plot.png' to view your results.")
# Export the final cluster assignments to a new CSV
output_df = plot_df[['Genome', 'Cluster']]
output_df.to_csv('cluster_results.csv', index=False)
print("Saved cluster assignments to cluster_results.csv")

