import os
import random

# This is the default folder structure created by the NCBI datasets tool
data_dir = "ncbi_dataset/data"

# Walk through all subdirectories to locate the genome FASTA files
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith(".fna"):
            filepath = os.path.join(root, file)
            
            # Read the FASTA file
            with open(filepath, 'r') as f:
                lines = f.readlines()
            
            # Strip out the '>' header lines and combine all DNA letters into one long string
            sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
            
            # Define our 100kbp proxy length
            slice_length = 100000
            
            # If the genome is long enough, grab a random 100kbp slice
            if len(sequence) > slice_length:
                start_idx = random.randint(0, len(sequence) - slice_length)
                proxy_seq = sequence[start_idx : start_idx + slice_length]
                
                # Save the new lightweight proxy sequence to your current folder
                output_name = file.replace(".fna", "_100kbp_proxy.fna")
                with open(output_name, 'w') as out_f:
                    out_f.write(f">{file}_proxy\n")
                    out_f.write(proxy_seq)
                    print(f"Successfully created proxy: {output_name}")
            else:
                print(f"Skipping {file} - sequence is shorter than 100kbp.")

