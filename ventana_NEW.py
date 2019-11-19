#!/usr/bin/env python3

"""I attempted this assignment last year. 
Hopefully, this is an improvement. 
I've added argparse, so that, in itself, is an improvement... 
"""

import os
import Bio
from Bio import SeqIO
from Bio import SeqUtils
from Bio.SeqUtils import GC
import matplotlib
matplotlib.use('Agg')
#Enables some backend sorcery.
#That is allows me to view the plot after it's created
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--FILE"), required=True, help="Name of input file in current directory")
#ap.add_argument("-l", "--LENGTH", required=True, type=int, help="Length of input sequence")
ap.add_argument("-c","--CHUNK", required=True, type=int, help="Smaller subset of sequence")
args=vars(ap.parse_args() )

for record in SeqIO.parse(args["FILE"], "fasta"):
	genome.append(record)
print("Genome locked")
print(len(genome) )
#Imports genome and tells us how big it is

scaffolds = [] 
for record in genome:
	if len(record.seq) > 100:
		scaffolds.append(record.seq)

#Finds scaffolds of suitable size 
print("Found %i scaffolds of suitable size" % len(scaffolds))
#I mean, look how fancy I was!
print("Scaffolds of suitable size loaded")

#Defines our sliding window iterator, called the VENTANA
def ventana (input,size): 

#Proceed with sliding ventana
	open_window = []
	for i in range(0,size):
		open_window.append(input[i:])
		yield input[i:i+size]

ventana(scaffolds, args["CHUNK"])
print ("Initializing the ventana")

#To be honest, I am still unsure how functions "save" its work

def GCC(list):
#Calculates GC content for each window
	GCCounter = []
	for sequence in list:
		GC(sequence)
		GCCounter.append(sequence)
	return GCCounter

GCC(open_window)
print("Calculating GC content")

#Ideally, plots each window's GC content
plot = ' '.join(str(a) for a in GCCounter)
print("Plotting...")
fig = plt.hist(plot, density=True)
plt.ylabel('GC Content')
num_bins = len(scaffolds)
plt.savefig('ventana.pdf')

print("Done!")