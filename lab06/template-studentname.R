#!/usr/bin/env Rscript

# Template for creating the final script for your lab
# The code provided should not be deleted
# Some of these lines should be changed as specified

student_name = "Ryan" #set this to your name
student_aa = "M" #replace this value with the amino acid you were assigned

example_df = read.csv("example.tsv",sep="\t",row.names=1)

# Put your custom code here


num_aa = 0 # this should eventually be the count for the total number of times your assigned amino acid appeared in all proteins
transcript = "ENST0123" #this variable can be deleted or repurposed to suit your needs

# leave this code the end of the script and modify for your needs, if necessary

print(paste0("My name is ",
            student_name,
            " and I was assigned ",
            student_aa,
            ". This amino acid was seen a total of ",
            num_aa,
            " times, and is the most common in ",
            transcript))