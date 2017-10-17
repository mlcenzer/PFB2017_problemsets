#!/usr/bin/env python3

import sys

seq="GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"

codon=[sys.argv[1], sys.argv[2], sys.argv[3]]

if codon[0] in seq:
        print(codon[0], "is in sequence data")
elif codon[1] in seq:
        print(codon[1], "is in sequence data, and", codon[0], "is not")
elif codon[2] in seq:
        print(codon[2], "is in sequence data, and neither", codon[0], "nor", codon[1], "is.")
else:
        print(codon[0], ",", codon[1], ", and", codon[2], "are not in this sequence.")
