#!/usr/bin/env python3

import os
import pandas as pd
import argparse
import Bio 
import SeqUtils from Bio

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--LENGTH", required=True, type=integer, help="Length of input sequence")
ap.add_argument("-c","--CHUNK", required=True, type=integer, help="Smaller subset of sequence")
args=vars(ap.parse_args() )

def GC_chunk(size, step):
    	"""
	In theory, will create a sequence, chunk it, then calculate GC content for each chunk
	In practice...
    	"""
	bases = 'ATGC'
    seq = ''.join(random.choice(bases) for i in range(args["LENGTH"])
	return seq

    gc = []
    #Initializes list
	
    seq = seq_rec.seq
    print SeqUtils.GC(seq)
	#Converts to sequence record to be read by SeqUtils
    
    for i in xrange(0, len(seq), step):
        s = seq[i:i+step].upper()
        a = s.count('A')
        c = s.count('C')
        g = s.count('G')
        t = s.count('T')
        if a+c+g+t > 0:
            gc.append((g+c)/float(a+c+g+t))
        else:
            gc.append(0.0)
	"""
	For every step, here 1000/100, count number of nucleotides, then divide GC content by all nucleotides
	"""
    return gc
GC_chunk(args["LENGTH"], ["CHUNK"])
