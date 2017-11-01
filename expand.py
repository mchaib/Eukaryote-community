#################

# This script has been prepared during an internship at the 
# DSMZ institute in Germany, in collaboration with Dr. Sixing Huang
# Its aim is to expand dereplicated sequences with 100% identities

# This scripts takes three mandatory arguments: a complete (not dereplicated fasta),
# the dereplicated fasta file and the result from searching a database using USEARCH 
# To run, type: 
# python expand.py [complete_fasta] [dereplicated_fasta] [usearch_output]

#################


import sys
from Bio import SeqIO

complete_fasta = sys.argv[1]
derep_fasta = sys.argv[2]
usearch_result = sys.argv[3]


handle = SeqIO.parse(derep_fasta, "fasta")

name_seq = {}
for item in handle:
	name_seq[item.description] = str(item.seq)

seq_classification = {}

for line in open(usearch_result, 'r'):
	fields = line.strip().split("\t")

	if fields[0] in name_seq:
		seq_classification[name_seq[fields[0]]] = [fields[1], fields[2]]


handle = SeqIO.parse(complete_fasta, "fasta")

for item in handle:
	if str(item.seq) in seq_classification:
		print (str(item.description) + "\t" + "\t".join([str(x) for x in seq_classification[str(item.seq)]]))