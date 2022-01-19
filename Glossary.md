# Glossary and quick reference

## Command-line utilities used in class/labs

### `bash`

-  GNU Bourne-Again SHell

### `cat`

- concatenate files and print on the standard output

### `chmod`

- change file mode bits (i.e. the permissions for whether users can read, write and execute)

### `cut`

- remove sections from each line of files


### `echo`

-  display a line of text (i.e. send that line of text to STDOUT)

### `grep` and `egrep`

- print lines matching a pattern

### `gzip`, `gunzip` and `gzcat`

- compression/decompression tool using Lempel-Ziv coding (LZ77)
- `gzip` for compressing, and the other two are for decompressing. 
- `zcat` decompresses to STDOUT and is simply an alias for `gunzip -c` 

### `head`

- output the first part of files

### `ls`

- list directory contents

### `man`

-  an interface to the on-line reference manuals (or "man pages")

### `paste`

- Write lines consisting of the sequentially corresponding lines from each FILE, separated by TABs, to standard output.  With no FILE, or when FILE is -, read standard input.


### `tail`

- output the last part of files

### `perl`

- The Perl 5 language interpreter

### `samtools`

- Utilities for the Sequence Alignment/Map (SAM) format

### `seqtk`

- Tools for processing sequences in the FASTA or FASTQ format

### `sort`

- sort lines of text files using one or more column
- can perform numeric or alphabetic/alphanumeric sort

### `less`

- Less  is a program similar to more, but which allows backward movement in the file as well as forward movement.  Also, less does not have to read the entire input file before starting, so with large input files it starts up faster than text editors like vi.

### `wc`

- word, line, character, and byte count

### `which`

- locate a program file in the user's path

## Commonly used symbols and their various applications

### newline `\n`

- A highly important whitespace character that splits a line of text to the next line

### tab `\t`

- A highly important whitespace character that is commonly used as a delimiter between columns (e.g. in a tsv or tab-separated values file)

### dollar sign `$`

- Goes before a bash variable when retrieving (but not when setting) its value
- Acts as a pattern anchor on the right-hand side when used in the context of a regular expression

### exclamation mark `!` 

- In many programming languages this reverses the logic of an operation 
  - e.g. `!=` means *not equal to*
  - Shortcut for checking if an operation or function call returns FALSE, negating it (`! some_operation`) will cause it to evaluate to TRUE 
  
### hash symbol `#` 

- A common way to embed lines of text in code that is ignored by the compiler (i.e. create a comment)
- Used at the start of scripts in combination with `!` to create the *shebang* line `#!`
- Also used for making hashtags although that's not relevant for this course

### asterisk `*`

- In bash this is used for globbing
- Indicates multiplication operation in most programming languages

### tilde `~`

- Found to the left of the 1 on most keyboards
- Used in unix-like systems as a shortcut to your home directory 
- Used as an operator for regular expressions in some languages (i.e. `~=` sorta equal to)

### hypen or minus sign `-`

- Used as a minus sign
- Various uses in different contexts in bash
 - Convention to use this before named arguments e.g. `program -i input_file`
 - Can be used to tell a command-line program to read from STDIN instead of an input file e.g. `some_other_program | program -i`
 
### vertical bar or pipe `|`

- used in unix-like systems to flow data between multiple processes
- Two vertical bars together almost always means logical OR `||`
- In R a single `|` can mean OR in many contexts

### ampersand `&`

- Adding this to the end of a command in bash sends the process to the background and frees your terminal to allow more commands to be run
- Two ampersands together mean logical AND `&&`

### forward slash `/`  

- The *normal* function of the `?` key on your keyboard
- used a LOT in unix-like operating systems to separate directory levels.
- On its own it has a special meaning as the "root" directory of a filesystem 
- *not to be confused with backslash*

### backslash `\` 

- above the return/enter key on most keyboards
- used in windows to separate directory levels
- acts as a special *escape* character in various programming languages as a way to hide special symbols from being interpreted by the compiler

## Week 1

### annotation

Genomic annotation refers to the process of identifying functional elements in a genome. Annotations are also what we call any set of coordinate-based information that result from this process, in other words, the locations of functional elements and their relationships to other annotations. Examples: gene, a gene's exons, an exon's splice sites, a gene's transcripts, repetitive elements.

### BED

A commonly used tab-separated format for storing and manipulating genomic annotations. [See also.](https://genome.ucsc.edu/FAQ/FAQformat.html)

### bit

The minimal unit of binary data representation/storage. Can exist in two states (on or off, i.e. 0 or 1).

### byte

A set of eight bits. A minimum amount of information needed to store an ASCII character in a plain text file. 

### character

A data type in some programming languages used to store a single character (printable or whitespace). Examples: `a`, `?`, `\n` (newline).

### FASTA

A simple plain-text format for storing one or more DNA, RNA or protein sequence records. 

### Globbing

A convenience feature used by bash to restrict files to all those matching more generic patterns specified by the glob. The general use is to us `*` to represent a component of the filename that matches the files the user wants to specify. [See also](https://mywiki.wooledge.org/glob)

### Pipe

A stream of data from one program to another. In bash, a pipe of standard output (STDOUT) is achieved by separating commands with the bar `|` symbol. 

### string

A common data type used in virtually all programming languages. Used for values that are made up of ordered sequences of characters. A string can contain any sequence of characters, printable or whitespace. Examples: `AAAAA`, `hello world`, `GATTACA`.

## Week 2

### alias

- A user-settable shorthand way to run a command in bash. Often used to run a command that reqires complex set of parameters 
- These are set using the built-in alias command, usually in the `.bashrc` or `.bash_profile` file: `alias alias_name="command_to_run"`

### argument

- A value (e.g. string, integer) given to a program at runtime. Typically these will specify the input for the program or the path to an input file along with specifying options or settings for the program.


