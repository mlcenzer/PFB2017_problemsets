#!/usr/bin/env python3

import sys
import pronto

go_file_name='go.owl.1'

Dros_file=open(sys.argv[1],'r')

ont = pronto.Ontology(go_file_name)

#term_id='GO:0040011'# term name for 'locomotion'; this is formatted 'REF:ACCESSION'

#ok, locomotion is a great song but kind of a long list.

term_id=sys.argv[2]

term_obj=ont[term_id] 

term_name=term_obj.name

all_children={}

for child in term_obj.rchildren():
    all_children[child.id]=child.name
    all_children[term_id]=term_name

for line in Dros_file:
    line=line.rstrip()
    line_list=line.split('\t')
    for object in line_list: #go through each term in the line
        if object.startswith('GO:'): #hit the accession number
            if object in all_children.keys(): #if the accession number is a key in my children dictionary
                print(line_list) #print it


Dros_file.close()#make sure to close your file!







