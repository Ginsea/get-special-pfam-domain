#!/usr/bin/env python
#-*- cdoing: utf-8 -*-

'''
@Author This script was developed by Ginsea Chen (ginseachen@hotmail.com) in CATAS
@Description Script can be used to extract some seqs which contained one or more
domains in a fasta file based on pfam results
@Pfamfile The output file of pfamscan.pl
@outfile Fasta file contained special domains
@fastafile Oringinal fasta file which used as infile of pfamscan.pl
@pfamdomains a list of one or more domains which you need to extract
'''


import sys
from Bio import SeqIO
import os,os.path

if sys.argv[1] == "-h":
    print "Usage:\n\tpython %s pfamfile outfile fastafile pfamdomains"%os.path.basename(__file__)
    sys.exit(0)

out = open(sys.argv[2],"w")

fasta = dict()
for seqs in SeqIO.parse(sys.argv[3],"fasta"):
    fasta[str(seqs.id)] = str(seqs.seq)

out1 = open("pfamout","w")
for lines in open(sys.argv[1],"r"):
    if lines[0] != "#":
        out1.write("%s\n"%lines)
out1.close()

pfam = dict()
for lines in open("pfamout","r"):
    cols = lines.strip().split()
    if len(cols) != 0:
        try:
            pfam[cols[0]].append(cols[5])
        except KeyError:
            pfam[cols[0]] = [cols[5]]

target = []
for ids in sys.argv[4:]:
    target.append(ids)

for query in pfam:
    if pfam[query] == target:
        out.write(">%s\n%s\n"%(query,fasta[query]))
out.close()
os.system("rm pfamout")
