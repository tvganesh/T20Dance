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

path=os.path.join(idir,"Rajasthan Royals-Royal Challengers Bangalore-allMatches.csv")
rr_rcb_matches = pd.read_csv(path)

yka.teamBatsmenVsBowlersOppnAllMatches(rr_rcb_matches,'Rajasthan Royals',"Royal Challengers Bangalore",plot=True,top=3,runsScored=20,savePic=True,dir1=odir,picFile="runsScoredTeamOppn.png")
