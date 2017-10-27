#!/usr/bin/env python3

import sys

from Bio import SeqIO

#command line arguments
kmer_length=int(sys.argv[1])
filename=sys.argv[2]
num_kmers=int(sys.argv[3])

##read in the fastq file filename.fastq from sys

my_kmers={}

for seq_record in SeqIO.parse(filename, "fastq"): #parse file use SeqIO.parse
    record=str(seq_record.seq) #pull out the seq record as a string
    while len(record)>=kmer_length: #while the record is longer than the kmer length
        kmer=record[0:kmer_length] #pull out the kmer
        if kmer in my_kmers: #if the kmer is already in my dictionary, add one to the count
            my_kmers[kmer]+=1
        else: #if the kmer is not in my dictionary, start a new entry equal to 1
            my_kmers[kmer]=1
        record=record[1:] #strip the first base of my record
        
#sort to get top ten

top_ten_kmers=[]

top_kmer_lengths=sorted(my_kmers.values())[::-1][:num_kmers]

for item in top_kmer_lengths:
    for kmer in my_kmers:
        if my_kmers[kmer]==item:
            top_ten_kmers.append(kmer)
        
print(top_ten_kmers, top_kmer_lengths)





