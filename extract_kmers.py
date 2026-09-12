import os
import csv
import itertools

# Define k-mer length and generate all 4,096 possible 6-mers
k = 6
bases = ['A', 'C', 'G', 'T']
all_kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]

results = []

print("Scanning proxy files and calculating k-mer frequencies...")

# Scan the current directory for the proxy files you just made
for file in os.listdir('.'):
    if file.endswith('_100kbp_proxy.fna'):
        with open(file, 'r') as f:
            lines = f.readlines()
        
        # Combine the DNA sequence and convert to uppercase
        seq = "".join([line.strip() for line in lines if not line.startswith(">")]).upper()
        
        # Initialize a dictionary to count occurrences
        kmer_counts = {kmer: 0 for kmer in all_kmers}
        total_kmers = len(seq) - k + 1
        
        if total_kmers <= 0:
            continue
            
        # Sliding window to read every 6-mer in the sequence
        for i in range(total_kmers):
            kmer = seq[i:i+k]
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
                
        # Convert raw counts to normalized frequencies
        row = {'filename': file}
        for kmer in all_kmers:
            row[kmer] = kmer_counts[kmer] / total_kmers
            
        results.append(row)

# Save the mathematical signatures to a CSV file
if results:
    with open('genomic_signatures.csv', 'w', newline='') as csvfile:
        fieldnames = ['filename'] + all_kmers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print("Success! Signatures saved to genomic_signatures.csv")
else:
    print("No proxy files found. Make sure they are in the same folder.")

