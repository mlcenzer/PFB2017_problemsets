#!/usr/bin/env python3

import sys

filename=sys.argv[1]

#generate a program that reads in a file name from the command line and generates a table containing the number of reads mapped to each gene.
sam_file=open(filename, 'r')

read_numbers={}


for line in sam_file:
    line_list=line.split('\t')
    gene_name=line_list[2].split('^')[0]
    if gene_name in read_numbers:
        read_numbers[gene_name]+=1
    else:
        read_numbers[gene_name]=1

#for gene in read_numbers:
#    print(gene, '\t', read_numbers[gene])


reads_sorted=sorted(read_numbers, key=lambda x:read_numbers[x], reverse=True)


for gene in reads_sorted:
    print(gene, '\t', read_numbers[gene])


print(sum(read_numbers.values())) #compare this to wc -l filename in command line

sam_file.close()
