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


path=os.path.join(idir,"Chennai Super Kings-allMatchesAllOpposition.csv")
csk_matches = pd.read_csv(path)
team1='Chennai Super Kings'

yka.plotWinLossByTeamAllOpposition(csk_matches,team1,plot="detailed",savePic=True,dir1=odir,picFile="winsLossTeamsAllOpposition.png")
