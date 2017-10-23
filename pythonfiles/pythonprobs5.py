#!/usr/bin/env python3


##Q5: generating gene lists

#alpaca_all_file=open("alpaca_all_genes.tsv", 'r')
#alpaca_stem_file=open("alpaca_stemcellproliferation_genes.tsv", 'r')
#alpaca_pig_file=open("alpaca_pigmentation_genes.tsv", 'r')
#alpaca_trans_file=open("alpaca_transcriptionFactors.tsv",'r')
#
#alpaca_all=set(alpaca_all_file.read().rstrip().split('\n')[1:])
#alpaca_stem=set(alpaca_stem_file.read().rstrip().split('\n')[1:])
#alpaca_pig=set(alpaca_pig_file.read().rstrip().split('\n')[1:])
#alpaca_trans=set(alpaca_trans_file.read().rstrip().split('\n')[1:])
#
#alpaca_stem_trans=alpaca_stem & alpaca_trans
#
#print(alpaca_stem_trans)

#A: Find all the genes that are not cell proliferation genes

#non_prolif_genes=(alpaca_all|alpaca_pig)-alpaca_stem
#
#testset1={'charming', 'splendid', 'fabulous'}
#testset2={'alarming', 'charming', 'disarming'}
#testset3={'fabulous', 'shut up', 'you don\'t say'}
#
#non_prolif_genes=(testset1|testset2)-testset3
#
#print(non_prolif_genes)

#B Find all the genes that are both stem cell proliferation genes and pigment genes

#stem_and_pig=alpaca_stem & alpaca_pig
#
#print(stem_and_pig)
#
#alpaca_all_file.close()
#alpaca_stem_file.close()
#alpaca_pig_file.close()
#alpaca_trans_file.close()

##Q4: working with fastq data

#fastq_file=open("Python_05.fastq",'r')
#
#lines=0
#chars=0
#
#for line in fastq_file:
#	lines+=1	
#	chars+=len(line)
#
#avg_length=chars/lines
#
#print("There are {} lines, with a total of {} characters, in this file. The average line is {} characters long.".format(lines,chars,avg_length))


##Q3: reverse complement fasta data

#file_seq=open("Python_05.fasta", 'r')
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
#seq_list=sequence.split()
#
#rev_sequence=''
#
#for pos in seq_list:
#	if pos[0]=='>':
#       	rev_sequence+='\n'+pos + '|this sequence has been complemented and reversed'
#	else:
#		comp_pos=pos.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
#		rev_sequence+='\n'+comp_pos[::-1].upper()
#
#print(rev_sequence)
#file_seq.close()


##Q1-2: working with a song text file

#song=open("Python_05.txt", "r")
#cap_song=open("Python_05_uc.txt", 'w')
#
#for lyric in song:
#	lyric=lyric.upper()
#	cap_song.write(lyric + '\n')
#	print(lyric)
#
#song.close()
#cap_song.close()


