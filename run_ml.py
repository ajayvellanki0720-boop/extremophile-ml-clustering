import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

print("Loading genomic signatures...")
df = pd.read_csv('genomic_signatures.csv')
filenames = df['filename']
X = df.drop('filename', axis=1)

print("Calculating statistical validity (Silhouette Score & Elbow Method)...")
inertia = []
silhouette_scores = []
K_range = range(2, 10)

# Test every cluster size from 2 to 9
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, labels))

# 1. Plot the Statistical Proof
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Elbow (Inertia) on the left axis
ax1.plot(K_range, inertia, 'bo-')
ax1.set_xlabel('Number of Clusters (k)')
ax1.set_ylabel('Inertia (Elbow Method)', color='b')

# Plot Silhouette Score on the right axis
ax2 = ax1.twinx()
ax2.plot(K_range, silhouette_scores, 'ro-')
ax2.set_ylabel('Silhouette Score', color='r')

plt.title('Determining Optimal k: Elbow Method & Silhouette Score')
plt.savefig('cluster_stats.png')
print("Saved statistical metrics to cluster_stats.png")

# 2. Run the Final PCA Plot with the optimal k (we will use 3 based on our biology)
print("Running final K-Means and PCA...")
optimal_k = 3
final_kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = final_kmeans.fit_predict(X)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(X)

plot_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
plot_df['Cluster'] = clusters
plot_df['Genome'] = filenames

plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', palette='viridis', data=plot_df, s=100)
plt.title(f'Genomic Signatures of Extremophiles (k={optimal_k})')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.savefig('cluster_plot.png')
print("Saved cluster plot to cluster_plot.png")

