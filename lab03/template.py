#!/usr/bin/env python
import Bio
print("Delete this line!")

# IMPORTANT: replace the line of code below with the one you changed in your tutorial
# that sets the global variable to store your name

student_name = "Student"
file_base_path = "/local-scratch/course_files/MBB243/human_genes_chr7/"

#keep this code intact!
def get_filename(student_name):
  fh = open("student_files.txt","r")
  for line in fh.readlines():
    line = line.rstrip()
    (name,fasta) = line.split("\t")
    if name == student_name:
      return(file_base_path + fasta)

#this provides each student with their own sequence to work with.   
my_fasta_path = get_filename(student_name)
print("USING: ",my_fasta_path)

# add your new code below this comment
# your script should output the %GC of your sequence to the terminal. 
# You can modify the existing code below once you have the code that calculates
# %GC for you

#add your new code above this comment and modify the lines below as necessary
pc_gc = 0.0

print("My name is",student_name,"and my sequence was",pc_gc,"% GC",sep=" ")
