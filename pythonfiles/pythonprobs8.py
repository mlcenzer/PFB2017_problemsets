#!/usr/bin/env python3

import sys

import re

##Q1: Take a multi-FASTA file from user input and calculate the nucleotide composition for each sequence.
## Use a datastructure to keep count. Print out each sequence name and its composition in this format:
## seqName\tA_count\tT_count\tG_count\C_count


#import file from user input
fasta_file_name=sys.argv[1]

fasta_file=open(fasta_file_name)

fasta=fasta_file.read()

#clean your data and make it a pretty dictionary of lists
fasta_dict={}

for (id, description, seq) in re.findall(r"(>\S+)[ \t]?(.*?)\n([ATGC\n]+)", fasta):
        fasta_dict[id]=['Description:'+description, seq.replace('\n','')]

#count all the nucleotides of each type within each gene.

play_fasta={'geneA':['desc','AAAGGC'], 'geneB':['desc','AATGGGCC']}

fasta_counts={}

for gene in fasta_dict:
	sequence=fasta_dict[gene][1]
	fasta_counts[gene]={'A':sequence.count('A'),'T':sequence.count('T'),'G':sequence.count('G'),'C':sequence.count('C')}	
print(fasta_counts)

print(play_fasta)
