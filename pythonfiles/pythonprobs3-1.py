#!/usr/bin/env python3

import sys

import random

#loops and things

#while loop

#count=int(sys.argv[1])

#while count<=100:
#	print(count)
#	count+=1

fact=1
count=1

while count<=1000:
	fact*=count
	count+=1
print(fact)


#numbers=[1,2,3] #test numbers

#numbers=[101,2,15,22,95,33,2,27,72,15,52]

#print(numbers)

#numbers_shrunk=numbers.remove(2)

#print(numbers, numbers_shrunk)


#for loops

#play_seq=list('AAATTTGGCCTTAA')


#for pos in play_seq:
#	pos1=random.randrange(0,len(play_seq)-1)
#	pos2=random.randrange(0,len(play_seq)-1)
#	nt1=play_seq[pos1]
#	nt2=play_seq[pos2]
#	play_seq[pos1]=nt1.lower()
#	play_seq[pos2]=nt2.lower()	
#	#print(play_seq,pos1,pos2)

#print(''.join(play_seq).upper())



#data_list=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#seqs_and_lengths=[(data_list.index(seq)+1,seq,len(seq)) for seq in data_list]

#for pos in range(len(seqs_and_lengths)):
#	print("{}\t{}\t{}\n".format(seqs_and_lengths[pos][0], seqs_and_lengths[pos][1], seqs_and_lengths[pos][2]))

#for seq in data_list:
#	print(len(seq),'\t', seq, '\n')


#for n in range(int(sys.argv[1]), int(sys.argv[2])+1):
#	if n%2:
#		print(n)



#for num in numbers:
#	if num%2==0:
#		print(num)

#numbers.sort()

#print(numbers)

#add evens and odds using loops

evens=[]
odds=[]
#for num in numbers:
#	print(num)
#	if num%2==0:
#		evens.append(num)
#	if num%2!=0:
#		odds.append(num)
#print("The sum of even numbers is", sum(evens),"and the sum of odd numbers is",sum(odds))


