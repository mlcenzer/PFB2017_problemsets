#!/usr/bin/env python3

##Q1: ssearch values

import sys

import os

directory=sys.argv[1]

field_names=['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits']

for filename in os.listdir(directory):
     ssearch_file=open(filename, 'r')
#clean it up
     for line in ssearch_file:
         if not line.startswith('#'):
             clean_line=line.rstrip()
             new_ssearch=dict(zip(field_names,clean_line.split('\t')))
             results_dict[sys.argv[n+1]]=new_ssearch
# #            print(new_ssearch)
#             break



#open all the files

# num_files=int((len(sys.argv)-1)/2)




# results_dict={}

# for n in range(1,num_files*2, 2):

# print(results_dict)
# ssearch_file.close()
# new_ssearch_file.close()









