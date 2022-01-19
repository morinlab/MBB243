#!/usr/bin/env python3
import sys #import the library we need for parsing command-line arguments

num_args = str(len(sys.argv))

print('This many arguments were provided: ' + num_args)
print('And they were::' + str(sys.argv))

