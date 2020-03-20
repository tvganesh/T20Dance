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


path=os.path.join(idir,"Delhi Daredevils-allMatchesAllOpposition.csv")
dd_matches = pd.read_csv(path)

yka.teamBatsmenPartnershipAllOppnAllMatchesChart(dd_matches,'Delhi Daredevils', plot=True, top=4, partnershipRuns=100,savePic=True,dir1=odir,picFile="partnershipTeamAllOppn.png")
