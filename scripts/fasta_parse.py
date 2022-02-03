#!/usr/bin/env python

# A basic demo FASTA parser
# Run this from the base directory of the repository
# ./scripts/fasta_parse.py

# Function for counting the characters in a sequence (or any other string, actually)
def count_nucleotides(seq):
  nucl_dict = {}
  bases = list(seq) # converts string to array
  for base in bases: # loop over all characters
    if base in nucl_dict.keys():
      nucl_dict[base] += 1  # more observations of the base
    else:
      nucl_dict[base] = 1 # first observation of the base
  return(nucl_dict) # return the dictionary of counts


fasta_file_handle = open("data/some_human_genes.fa","r")

sequence = "" # for storing the "current" sequence as we collect it from multiple lines
# NOTE: why make an empty variable here?
for text_line in fasta_file_handle:
  text_line = text_line.rstrip("\n") 
  if text_line.startswith(">"):
    if sequence: 
# This is only false at the first header and the rest of the time it's our cue that we have a full sequence
      nuc_count = count_nucleotides(sequence)
      print(id,sequence[0:10],nuc_count)
      sequence = ""
    text_line = text_line.lstrip(">")
    header_info = text_line
    header_vals = header_info.split("|")
    id = header_vals[2]
  else:
    sequence += text_line
nuc_count = count_nucleotides(sequence)
print(id,sequence[0:10],nuc_count)
# These last two lines ensure the final sequence is also processed with our function
