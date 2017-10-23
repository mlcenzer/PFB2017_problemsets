#!/usr/bin/env python3

# this script is totally awesome

#functions for mean and standard deviation because Lukas and Jessen are unintentionally hazing me

def mean(anylist):
    list_sum=0
    for n in anylist:
        list_sum+=n
    list_mean=list_sum/len(anylist)
    return list_mean

def stddev(anylist, anylist_mean):
    square_sum=0
    for n in anylist:
        square_sum+=(n-anylist_mean)**2
    stddev=(square_sum/(len(anylist)-1))**(1/2)
    return(stddev)

##Q3: Write a script to parse a GFF3 file

gff_file=open("cab_sav_contig.gff",'r')

#print average gene length

#gene_lengths=[]
exon_lengths=[]

for line in gff_file:
    if line.startswith('#'):
        None
    else:
        line_list=line.split('\t')
        if line_list[2]=='exon':
            start=line_list[3]
            end=line_list[4]
            length=int(end)-int(start)
            exon_lengths.append(length)

#gene_length_mean=mean(gene_lengths)
exon_length_mean=mean(exon_lengths)

print(exon_lengths)
print(exon_length_mean)


gff_file.close() #don't forget to close your file!

# #Read in fastq file
# fastq_file=open("pfb.fastq","r")

# ##Q2: Trim each sequence in a fastq file starting from the first base in each sequence lower than Q=20 to the end of the sequence.
# ##Unfortunately this is not going to be fast. I need to eat.

# current_line=0
# prev_bases=''

# fastq_out=open("fastq_output.fastq", "w")

# for line in fastq_file:
#     current_line+=1 #start at 1, moves down line by line
#     if current_line%4==1: #references an identifier
#         fastq_out.write(line)
#     elif current_line%4==2: #references sequence
#         prev_bases=line #grab the previous sequence
#     elif current_line%4==0: #references quality string
#         qual_str='' #make an empty string where I will write characters that pass the quality test
#         char_counter=0
#         for char in line: #Go through all characters in quality string
#             print(line[char_counter], char, (ord(char)-33))
#             if (ord(char)-33)>=20: #if the quality at that char is <= 20(-33 to get w/in 1-char ascii range) & we have not skipped any positions
#                 qual_str+=char #cat quality scores to qual_str
#                 char_counter+=1
#             else:
#                 break
#         cut_sequence=prev_bases[0:char_counter] #cut it
#         fastq_out.write(cut_sequence+'\n'+ '+\n' +qual_str + '\n') #write in order sequence, + line, quality string

# fastq_out.close() #don't forget to close the file you're writing!

##Q1
# length_file=0
# length_list=[]
# qual_list=[]

# #make a list of sequences in length_list. Also make a list of lists of quality characters.
# #Note in the final nested for loop, that 1) dividing two integars returns a float; 2) quality scores are always on lines that are exactly divisible by 4.

# for line in fastq_file:
#     length_file+=1 #start at 1, moves down line by line
#     if length_file%4==2: #references sequences
#         length_list.append(len(line)) #add sequence length to length_list
#     elif length_file%4==0: #references quality string
#         qual_list.append([]) #add a new list for a new gene
#         for char in line: #Go through all characters in quality string
#             qual_list[int((length_file/4)-1)].append(ord(char)) #append quality scores to gene list
            

# length_mean=mean(length_list)
# length_std=stddev(length_list, length_mean)
# #print(qual_list)
# qual_means=[]

# for gene in qual_list:
#     qual_means.append(mean(gene))

# qual_mean=mean(qual_means)

#print(qual_list)
#print(qual_means, qual_mean)

#print(length_mean, length_std)

#don't forget to close it!
#fastq_file.close()
