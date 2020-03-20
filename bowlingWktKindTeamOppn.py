import pandas as pd
import os
import yorkpy.analytics as yka
import argparse
parser = argparse.ArgumentParser(description='bowlingWicketKind')
parser.add_argument("idir",help="input directory")
parser.add_argument("odir",help="output directory")
args=parser.parse_args()
idir=args.idir
odir=args.odir

path=os.path.join(idir,"Chennai Super Kings-Rajasthan Royals-allMatches.csv")
csk_rr_matches = pd.read_csv(path)

yka.teamBowlingWicketKindOppositionAllMatches(csk_rr_matches,'Chennai Super Kings','Rajasthan Royals',plot=True,top=5,wickets=1,savePic=True,dir1=odir,picFile="bowlingWktKindTeamOppn.png")
