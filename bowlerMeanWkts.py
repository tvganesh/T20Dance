import pandas as pd
import os
import yorkpy.analytics as yka

import argparse
parser = argparse.ArgumentParser(description='saveMatches2Teams')
parser.add_argument("idir",help="input directory")
parser.add_argument("odir",help="output directory")
args=parser.parse_args()
idir=args.idir
odir=args.odir

name="B Kumar"
team='Sunrisers Hyderabad'
df=yka.getBowlerWicketDetails(team,name,dir=idir)

yka.bowlerWicketsAgainstOpposition(df,name,savePic=True,dir1=odir,picFile="bowlerMeanWkts.png")
