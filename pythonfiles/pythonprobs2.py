#!/usr/bin/env python3

seq="GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"

atg_test='ATG' in seq

print(atg_test)

print('TTT' in seq)

codon=['AAAA', 'TTTT', 'GGGG']

if codon[0] in seq:
	print(codon[0], "is in sequence data")
elif codon[1] in seq:
	print(codon[1], "is in sequence data, and", codon[0], "is not")
elif codon[2] in seq:
	print(codon[2], "is in sequence data, and neither", codon[0], "nor", codon[1], "is.")
else:
	print(codon[0], ",", codon[1], ", and", codon[2], "are not in this sequence.")

