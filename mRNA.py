#!/usr/bin/env python3

import random
import string

#My random.choices still does not work. So I looked into a work around

def mRNA(seqLength=1000):
    """Generate a random string of fixed length """
    bases = 'AUGC'
    return ''.join(random.choice(bases) for i in range(seqLength))
#What I think it is doing is choosing 1000 elements from bases and joining them to the sequence.

sequence = mRNA()
#Getting our string ready for action.

start_codon = sequence.count('AUG')

print("This is how many genes we have=", start_codon) 
#Counts then notifies user how many genes we have.

renz = sequence.split('AUG')
#Splits on 'AUG'
#The only problem I see here is that it uses AUG as a delimiter and is thus removed in later steps.
#I suppose I could just add 3 to the count down below...

#print(renz)
#Commented out checkpoint

genes = [s for s in renz if len(s) > 50]
#If a chunk is greater than 50 base pairs, add to list.

print("Genes over 50 base pairs", genes)
#Checkpoint
num_genes = len(genes)
print("We now have this many genes=", num_genes)

for element in genes:
	print((len(element)) )
#As a loop, determines length of each gene. 

print("And again as a list comprehension")
hardy = [len(element) for element in genes]

print(hardy)
#Same as above, but as list comprehension
