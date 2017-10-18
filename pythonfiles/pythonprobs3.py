#!/usr/bin/env python3

#general list things

list = ['a', 'bb', 'ccc']
list_copy = list

list = ['a', 'bb', 'ccc']
list_copy = list.copy()



#sequence things
seq='AAATTGAATTCTGGC' #made up sequence for testing

#seq='GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

#locates position of EcoR1
EcoR1='GAATTC'

EcoR1_site1=seq.find(EcoR1)

#print(EcoR1_site1)

restriction_starts=[0,EcoR1_site1+1]

restriction_ends=[EcoR1_site1,len(seq)-1]

frag_1_limits=[seq[restriction_starts[0]],seq[restriction_ends[0]]]

frag_2_limits=[seq[restriction_starts[1]],seq[restriction_ends[1]]]

frag_1=seq[restriction_starts[0]:restriction_ends[0]+1]

frag_2=seq[restriction_starts[1]:restriction_ends[1]+1]


#print("Fragment\tPosition\tLength\n{}\t{}\t{}\n{}\t{}\t{}".format(frag_1[0:50],[restriction_starts[0],restriction_ends[0]],len(frag_1),frag_2[0:50],[restriction_starts[1],restriction_ends[1]],len(frag_2)))

frag_list=sorted([frag_1,frag_2]) #sort by default

frag_list.sort(key=len) #sort by length

print(frag_list)











#AT and GC content
seq_length=len(seq)

A_count=seq.count('A') #number of As in seq

T_count=seq.count('T') #numbe of Ts in seq

AT_content=(A_count+T_count)/seq_length

print("AT content is", AT_content)

G_count=seq.count('G')

C_count=seq.count('C')

GC_content=(G_count+C_count)/seq_length

print("GC content is", GC_content)

print(AT_content+GC_content)


#build complementary strand
#To avoid replacing Gs with Cs and then replacing those Cs with Gs, I put in a place holder for Gs first, then replace Cs, then replace my placeholders.
comp_seq_X=seq.replace('G','X').replace('C','G').replace('X','C')

comp_seq=comp_seq_X.replace('A','Y').replace('T','A').replace('Y','T')

#build reverse complement
#notation is seq[start:end:dir steplength]; here this is blank, blank, negative (for reverse), one (for single character steps)
rev_seq=seq[::-1] 

print("Original Sequence\t5'{}\t3'\nComplement\t\t5'{}\t3'\nReverse Complement\t3'{}\t5'\n".format(seq[0:25], comp_seq[0:25], rev_seq[0:25]))


