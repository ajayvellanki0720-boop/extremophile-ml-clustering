import pandas as pd
from sklearn.decomposition import PCA

# Load the dataset
df = pd.read_csv('genomic_signatures.csv')
filenames = df['filename']
X = df.drop('filename', axis=1)

# Run the PCA math
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X)

# Find the genome with the highest PC2 value (the vertical axis)
outlier_index = principal_components[:, 1].argmax()
outlier_filename = filenames.iloc[outlier_index]

print(f"FOUND THE OUTLIER: {outlier_filename}")

