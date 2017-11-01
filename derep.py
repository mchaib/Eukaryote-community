#################

# This script has been prepared during an internship at the 
# DSMZ institute in Germany, in collaboration with Dr. Sixing Huang
# Its aim is to dereplicate sequences with 100% identities
# To use type
# python derep.py [fasta_containing_dir]

#################


import os, sys, json
from Bio import SeqIO

top_folder = sys.argv[1]
extension = "fasta"

seq_name = {}

for (head, dirs, files) in os.walk(top_folder):
    for file in files:
        if file.endswith(extension):
            current_file_path = os.path.abspath(os.path.dirname(os.path.join(head, file)))
            with_name = current_file_path + "/"+ file
            #print with_name
          
            handle = SeqIO.parse(with_name, "fasta")

            for item in handle:
                if str(item.seq) not in seq_name:
                    seq_name[str(item.seq)] = {}

                #if with_name not in seq_name[str(item.seq)]:
                    #seq_name[str(item.seq)][with_name] = []
                    
                #if item.description not in seq_name[str(item.seq)][with_name]:
                    #seq_name[str(item.seq)][with_name].append(item.description)

                if with_name not in seq_name[str(item.seq)]:
                    seq_name[str(item.seq)][with_name] = set()
            
                seq_name[str(item.seq)][with_name].add(item.description)

index = 0
index_name = {}
temp_fasta_content = ""
for key in seq_name:
    temp_fasta_content += ">seq_" + str(index) + "\n" + key + "\n"
    index_name["seq_" + str(index)] = seq_name[key]
    index += 1

temp_fasta_file_name = os.path.dirname(with_name) + "/temp.fas"
temp_fasta_file = open(temp_fasta_file_name, 'w')
temp_fasta_file.write(temp_fasta_content)
temp_fasta_file.close()

print "FASTA written"

