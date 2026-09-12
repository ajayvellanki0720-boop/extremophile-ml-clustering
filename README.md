# Polyextremophile Genomic Signatures
Objective: To computationally map the hidden environmental signatures of microbes surviving multiple extreme stresses using unsupervised machine learning.

Methodology:
Curated whole-genome datasets using the NCBI Datasets CLI.
Extracted 100kbp continuous genome proxies using Python.
Calculated 6-mer frequency vectors (4,096 dimensions) to establish mathematical genomic signatures.
Reduced dimensionality via PCA and clustered organisms using K-Means.
Results:
The K-Means algorithm successfully and blindly segregated polyextremophiles (Sulfolobus), single-stress extremophiles (Thermus), and mesophiles (Bacillus) into distinct mathematical clusters, proving that extreme environmental pressures leave a computationally detectable footprint on DNA.
