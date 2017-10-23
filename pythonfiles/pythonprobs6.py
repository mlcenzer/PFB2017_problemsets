#!/usr/bin/env python3

import re

##Q6-7: enzymes with regular expressions
##Check enzyme ambiguity codes at http://www.chick.manchester.ac.uk/SiteSeer/IUPAC_codes.html
##R is A or G
##Y is C or T
##restriction site is R^AATTY

#locate and print where all the RAATTY sites happen in this file.
file_apoI=open("Python_06_ApoI.fasta")
apoI_read=file_apoI.read()

apoI={}

for (id, description, seq) in re.findall(r"(>\S+)[ \t]?(.*?)\n([ATGC\n]+)", apoI_read):
	apoI[id]=['Description:'+description, seq.replace('\n','')]

test_apoI='GAATTCAAAAAAGGTTAAATTTGC'

rest_sites={}
for gene in apoI:
	rest_sites[gene]=re.findall(r"[AG]AATT[CT]",apoI[gene][1])

#Now determine the sites of the physical cuts and print out the sequence with ^ at the cut sites

cut_sites={}

for gene in apoI:
	cut_sites[gene]=re.sub(r"([AG])(AATT[CT])", r"\1^\2",apoI[gene][1])

print(cut_sites)

apoi_frags=[]

for gene in cut_sites:
	apoI_frags=cut_sites[gene].split('^')

print(apoI_frags)

file_apoI.close

##Q5 Modifying my fasta parser from pythonprobs5.py to use regular expressions.

#file_seq=open("Python_06.fasta")
#
#sequence=file_seq.read()
#
#seq_string=''
#	
#for (id, description, seq) in re.findall(r"(>\S+)\s(.+)\n([ATGC\n]+)", sequence):
#	seq_string+=id+'\t'+description+'\n'
# 	seq=seq.replace('\n','')
#	seq=seq.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
#	seq_string+=seq[::-1].upper()+'\n'
#	print(seq_string)
#

##The following code effectively complements and reverses this code. It does not include regular expressions-it is the code from pythonprobs5.py plus a '\n' in the split.

#file_seq=open("Python_06.fasta")
#
#sequence=''
#
#for line in file_seq:
#	if line[0]=='>':
#		sequence+='\n'+line
#	else:
#		sequence+=line.rstrip()
#
#sequence=sequence.lstrip()
#
#seq_list=sequence.split('\n')
#
#rev_sequence=''
#       
#for pos in seq_list:
#	if pos[0]=='>':
#		rev_sequence+='\n'+pos + '|this sequence has been complemented and reversed'
#	else:
#		comp_pos=pos.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
#		rev_sequence+='\n'+comp_pos[::-1].upper()
#
#print(rev_sequence)
#file_seq.close()


##Q3-4 finding headers in a fasta file, extracting sequence names and descriptions

#fasta_file=open("Python_06.fasta")
#
#fasta=fasta_file.read()

#for IDs in re.finditer(r"(>\S+)\s(.+)\n",fasta):
#	print("ID:", IDs.group(1))
#	print("description:", IDs.group(2))




#Q1-2 reading in Shel Silverstein's Nobody, finding occurances of nobody and replacing with my favorite name.

#shel_file=open("Python_06_nobody.txt",'r')
#
#shel=shel_file.read()
#
#for nobody in re.finditer(r"Nobody", shel):
#	start_n=nobody.start()+1 #locations of nobody
#	line_n=shel[:start_n].count('\n')+1
#	print(start_n,line_n)
#
#bennie=re.sub(r"Nobody", r"Benedict Cumberbatch", shel)
#
#print(bennie)
#shel_file.close()
