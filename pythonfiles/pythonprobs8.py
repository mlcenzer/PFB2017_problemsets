#!/usr/bin/env python3

import sys

import re


#import file from user input
fasta_file_name=sys.argv[1]

fasta_file=open(fasta_file_name)

fasta=fasta_file.read()

#clean your data and make it a pretty dictionary of lists
fasta_dict={}

for (id, description, seq) in re.findall(r"(>\S+)[ \t]?(.*?)\n([ATGC\n]+)", fasta):
        fasta_dict[id]={'Description': description, 'sequence': seq.replace('\n','')}

#print(fasta_dict)

#have some play data for testing
play_fasta={'geneA':{'Description': 'desc', 'sequence':'AAAGGC'}, 'geneB':{'Description':'desc','sequence':'AATGGGCC'}}

fasta_dict=play_fasta

##Q5
#Reverse complement and break it up into codons in all six frames; see also Q1-2,4 notes.

#add the reverse complement to the value list in your dictionary.

fasta_dict_rev=fasta_dict

for gene in fasta_dict_rev:
	seq=fasta_dict_rev[gene]['sequence']
	seq=seq.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
	seq=seq[::-1].upper()
	fasta_dict_rev[gene]["revseq"]=seq

print(fasta_dict_rev)

codons_dict={}

for gene in fasta_dict_rev:
	sequence=fasta_dict_rev[gene]['sequence'] #position of sequence in the list value of gene
	rev_sequence=fasta_dict_rev[gene]['revseq']
	codons_dict[gene]={'Description':fasta_dict_rev[gene]['Description']} #keep the description, initiate dictionary
	for frame in range(3):  #loop over frame positions
		codons=re.findall(r"[ATGC]{3}",sequence[frame:]) #Break it up in sets of three codons
		codons_dict[gene]['codons']=codons
		codons_rev=re.findall(r"[ATGC]{3}",rev_sequence[frame:]) #Break it up in sets of three codons
		codons_dict[gene]['rev_codons']=codons_rev 

print(codons_dict)

#take this dictionary and write it line by line to a file named "Python_08.codons-frame-1.nt"

#new_file=open("Python_08.codons-6frames.nt",'w')


####This doesn't work yet.
#for gene in codons_dict:
#	for frame in range(3):
#		new_file.write(gene.strip('>')+'-frame-'+str(frame+1)+'-codons\n')
#		sequence=codons_dict[gene]['codons'][frame+1]
#		for codon in sequence:
#			new_file.write(codon+' ')
#		new_file.write('\n')
#		rev_sequence=codons_dict[gene]['rev_codons'][frame+1]
#		for codon in rev_sequence:
#			new_file.write(codon+' ')
#		new_file.write('\n')
#new_file.close()



##Q4

#clean your data and make it a pretty dictionary of lists
fasta_dict={}

for (id, description, seq) in re.findall(r"(>\S+)[ \t]?(.*?)\n([ATGC\n]+)", fasta):
        fasta_dict[id]=['Description:'+ description, seq.replace('\n','')]


#have some play data for testing
play_fasta={'geneA':['desc','AAAGGC'], 'geneB':['desc','AATGGGCC']}

fasta_dict=play_fasta

#Break it up into codons in all three frames; see also Q1-2 notes.

codons_dict={}

for gene in fasta_dict:
	sequence=fasta_dict[gene][1] #position of sequence in the list value of gene
	codons_dict[gene]=[fasta_dict[gene][0]] #keep the description, initiate list
	for frame in range(3):	#loop over frame positions
		codons=re.findall(r"[ATGC]{3}",sequence[frame:]) #Break it up in sets of three codons
		codons_dict[gene].append(codons)

#print(codons_dict)

#take this dictionary and write it line by line to a file named "Python_08.codons-frame-1.nt"

new_file=open("Python_08.codons-3frames.nt",'w')

for gene in codons_dict:
	for frame in range(3):
		new_file.write(gene.strip('>')+'-frame-'+str(frame+1)+'-codons\n')
		sequence=codons_dict[gene][frame+1]
		for codon in sequence:
			new_file.write(codon+' ')
		new_file.write('\n')

new_file.close()

##Q1-2: Take a multi-FASTA file from user input and calculate the nucleotide composition for each sequence.
## Use a datastructure to keep count. Print out each sequence name and its composition in this format:
## seqName\tA_count\tT_count\tG_count\C_count
##Then, write a script that takes that file and breaks each sequence into codons in just the first frame.
#Break it up into codons in the first frame; Note: relies on above sequence, these Qs are not independent.

codons_dict={}

for gene in fasta_dict:
	sequence=fasta_dict[gene][1] #position of sequence in the list value of gene
	codons=re.findall(r"[ATGC]{3}",sequence) #Break it up in sets of three codons
	codons_dict[gene]=[fasta_dict[gene][0],codons] #put in new dictionary, retaining description and adding an element to the list that is codons in the first frame.
#print(codons_dict)

#take this dictionary and write it line by line to a file named "Python_08.codons-frame-1.nt"

new_file=open("Python_08.codons-frame-1.nt",'w')

for gene in codons_dict:
	new_file.write(gene.strip('>') + '-frame-1-codons\n')
	sequence=codons_dict[gene][1]
	for codon in sequence:
		new_file.write(codon+' ')
	new_file.write('\n')

new_file.close()

#count all the nucleotides of each type within each gene.
fasta_counts={}

for gene in fasta_dict:
	sequence=fasta_dict[gene][1]
	fasta_counts[gene]={'A':sequence.count('A'),'T':sequence.count('T'),'G':sequence.count('G'),'C':sequence.count('C')}	
#print(fasta_counts)

