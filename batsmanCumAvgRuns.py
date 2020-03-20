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

name="KS Williamson"
team='Sunrisers Hyderabad'
df=yka.getBatsmanDetails(team,name,dir=idir)

yka.batsmanCumulativeAverageRuns(df,name,savePic=True,dir1=odir,picFile="batsmanCumAvgRuns.png")