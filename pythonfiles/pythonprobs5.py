#!/usr/bin/env python3

##Q3: reverse complement fasta data

file_seq=open("Python_05.fasta", 'r')

sequence=''

for line in file_seq:
	if line[0]=='>':
		sequence+='\n'+line
	else:
		sequence+=line.rstrip()

sequence=sequence.lstrip()

seq_list=sequence.split()

rev_sequence=''

for pos in seq_list:
        if pos[0]=='>':
               rev_sequence+='\n'+pos + '|this sequence has been reversed'
        else:
               rev_sequence+='\n'+pos[::-1]

print(rev_sequence)
file_seq.close()


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


