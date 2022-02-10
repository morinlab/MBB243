#!/usr/bin/env python
from mbb_functions import parse_fasta
from mbb_functions import count_nucleotides

# A basic demo FASTA parser using functions stored in a separate file
# Run this from the base directory of the repository
# ./scripts/fasta_parse.py

fasta_file = "data/some_human_genes.fa"
fasta_file="data/human_genes_chr7/ENST00000631335.fa"
#get a dictionary of sequences, keyed by Ensembl transcript ID
sequences = parse_fasta(fasta_file)

for trans_id, trans_seq in sequences.items():
  #count ALL nucleotides in the sequence
  nuc_count = count_nucleotides(trans_seq,"total")
  print(trans_id,nuc_count["total"])
  #count individual nucleotides in the sequence
  nuc_count = count_nucleotides(trans_seq,"nucleotide")
  print(trans_id,nuc_count)
