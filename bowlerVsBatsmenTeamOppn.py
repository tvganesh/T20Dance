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

path=os.path.join(idir,"Sunrisers Hyderabad-Kolkata Knight Riders-allMatches.csv")
srh_kkr_matches = pd.read_csv(path)
yka.teamBowlersVsBatsmenOppnAllMatches(srh_kkr_matches,'Sunrisers Hyderabad','Kolkata Knight Riders',plot=True,top=5,runsConceded=10,savePic=True,dir1=odir,picFile="bowlerVsBatsmenTeamOppn.png" )
