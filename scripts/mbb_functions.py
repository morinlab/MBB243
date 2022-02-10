# A module containing custom functions for MBB demos

# Function for parsing a FASTA file into a dictionary using part of the header as the key
def parse_fasta(fasta_file):
  fasta_file_handle = open(fasta_file,"r")
  fasta_dict = {}
  sequence = ""
  for text_line in fasta_file_handle:
    text_line = text_line.rstrip("\n") 
    if text_line.startswith(">"):
      if sequence: 
        fasta_dict[id] = sequence
        sequence = ""
      text_line = text_line.lstrip(">")
      header_info = text_line
      header_vals = header_info.split("|")
      id = header_vals[2]
    else:
      sequence += text_line
  fasta_dict[id] = sequence
  return(fasta_dict)

# Function for counting the characters in a sequence (or any other string, actually)
# This function can return either a dictionary containing the total number of nucleotides under the key "total"
# or a dictionary with counts of each nucleotide with a key for each nucleotide
def count_nucleotides(sequence,count_type="nucleotide"):
  nucl_dict = {}
  bases = list(sequence) # converts string to array
  for base in bases: # loop over all characters
    if base in nucl_dict.keys():
      nucl_dict[base] += 1  # more observations of the base
    else:
      nucl_dict[base] = 1 # first observation of the base
  if count_type == "nucleotide":
    return(nucl_dict) # return the dictionary of counts
  elif count_type == "total":
    total_count = 0
    for key in nucl_dict.keys():
      total_count += nucl_dict[key]
    return({"total":total_count})
  else:
    print("You haven't specified an allowable option for count_type")
