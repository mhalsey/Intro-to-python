#!/usr/bin/env python3

import os
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--BEDFILE", required=True, help="Path to file in .bed format")
ap.add_argument("-f","--FAMILY", required=True, help="TE subfamily to be retained. Surround with quotes")
ap.add_argument("-s", "--GENOMESIZE", required=True, help="Size of genome of interest")
ap.add_argument("-t", "--TAXON", required=True, help="Taxon under study")
args=vars(ap.parse_args() )

cols=["Scaffold", "Start", "Stop", "Element","Score", "Strand", "Class", "Family", "Divergence"]

file = pd.read_csv(args["BEDFILE"], sep="\t", names=cols)

print(file.head() )

classes = file.Class.unique()

print(classes)

is_SINE = file['Family']==args["FAMILY"]
SINE = file[is_SINE]

#SINE = file[file.Family == args["FAMILY"]
#Something is hanging up here.

SINE = SINE.drop(["Strand", "Score"], axis=1)

SINE["Length"]=(SINE["Stop"] - SINE["Start"])
SINE["Proportion"]=SINE["Length"]/args["GENOMESIZE"]

SINE.to_csv(args["TAXON"])
#only prints out headers. 

print("Done!")
