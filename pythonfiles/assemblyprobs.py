#!/usr/bin/env python3

##Goals: determine # of contigs in file
##find the shortest contig
##find the longest contig
##find the L50 value

from Bio import SeqIO

lengths={}
lengths_list=[]
longest=''
shortest=''

for seq_record in SeqIO.parse('./canu/ecoli-manual/ecoli_6X.fasta', 'fasta'):
    lengths[seq_record.id]=len(str(seq_record.seq))
    lengths_list.append(len(str(seq_record.seq)))
    if longest is '':
        longest=seq_record.id
    if shortest is '':
        shortest=seq_record.id
    if lengths[seq_record.id]>lengths[longest]:
        longest=seq_record.id
    if lengths[seq_record.id]<lengths[shortest]:
        shortest=seq_record.id

print("There are", len(lengths), "contigs in this file. The shortest contig is", shortest, "and it has length", lengths[shortest], ". The longest contig is", longest, "and it has length", lengths[longest], ".")

#Locate the L50.
sorted_lengths=sorted(lengths_list)
#print(sorted_lengths)

running_total=0

goal=sum(sorted_lengths)*0.5

position=0

while running_total < goal:
    running_total+=sorted_lengths[-position]
    position+=1

print(running_total, position, goal)



