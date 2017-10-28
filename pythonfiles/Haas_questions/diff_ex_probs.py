#!/usr/bin/env python3

def meet_my_threshold(FDR, logFC, anyfile):
    num_DE_transcipts=0
    for line in anyfile:
        line_list=line.split('/t')
        my_logFC=line_list[1]
        my_FDR=line_list[4]
        if my_logFC>=logFC and my_FDR>=FDR:
            num_DE_transcripts+=1
    return(num_DE_transcripts)



DE_file=open('ph8_vs_std.edgeR.DE_results.txt', 'r')

FDR_range = [0.05, 0.001, 1e-5, 1e-10, 0]
logFC_range = [1, 2, 3, 4, 5]

unique_transcripts={}

for line in DE_file:
    line_list=line.split('\t')
    expression=line_list[1]
    gene=line_list[0]
    print("I'm a line! My favorite transcript is {} and it is expressed this much: {}".format(gene, expression))

test_test=meet_my_threshold(0.05,1,DE_file)

print(test_test)
DE_file.close()
