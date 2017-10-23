#!/usr/bin/env python3

from Bio import SeqIO

import re

##Q3: Make a new fasta file of all the sequences containing the species "Salmonella paratyphi B"
##Call the file s_paratyphi.prot.fa



for seq_record in SeqIO.parse("short_uniprot_sprot.fasta", "fasta"):
    


##Q1-2

# IDs=[]
# seqs=[]
# descs=[]

# #Note: uniprot_sprot.fasta contains 555k records. short_uniprot_sprot.fasta contains the first 2.

# #go through every line of your fasta file and pull out IDs, sequences, and descriptions. 
# for seq_record in SeqIO.parse("uniprot_sprot.fasta", "fasta"):
#     IDs.append(seq_record.id)
#     seqs.append(seq_record.seq)
#     descs.append(seq_record.description)

# #Go through the descriptions and pull out the organism names. Then check how many records there are for each "species".

# org_records={}

# for record in descs:
#     genus_sp=re.search(r"OS=([A-Z][a-z]+) ([a-z]+) +?", record) #using search because there should only be one per line; being specific here, won't work for improperly formatted genus/species names
#     if genus_sp:
#         organism=genus_sp.group(1)+' ' + genus_sp.group(2) #cat just genus group and species group
#         if organism in org_records: #trying to call org_records[organism] if that key does not exist returns an error, NOT None
#             org_records[organism]+=1 #If it exists, add 1 to it
#         elif organism not in org_records:
#             org_records[organism]=1 #if it doesn't exist yet, add 1 to it
        

# print(org_records)



