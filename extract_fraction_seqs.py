#!/usr/bin/env python

'''
@Author This script is developed by Ginsea Chen (ginseachen@hotmail.com) of CATAS
@Descriptions You can use this script to exrtact a small number of sequences from a fasta and then produce a new fasta file
@Infile The file with fasta formati
@Outfile The file with fasta format
@numbers How many sequences you want to exract
'''

import sys
import os, os.path
from Bio import SeqIO

if sys.argv[1] == "-h":
    print "Usage:\n\tpython %s infile outfile numbers"%os.path.basename(__file__)
    sys.exit(0)

out = open(sys.argv[2],"w")
 
y = sys.argv[3]

ids = []
fasta = dict()
for seqs in SeqIO.parse(sys.argv[1],"fasta"):
    ids.append(str(seqs.id))
    fasta[str(seqs.id)] = str(seqs.seq)

for sids in ids[:int(y)]:
    out.write(">%s\n%s\n"%(sids, fasta[sids]))
out.close()
