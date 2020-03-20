import yorkpy.analytics as yka
import pandas as pd

import yorkpy.analytics as yka
import argparse
parser = argparse.ArgumentParser(description='MatchWorm')
parser.add_argument("odir",help="output directory")
args=parser.parse_args()
odir=args.odir

gl_mi=pd.read_csv("/Users/tvganesh/backup/software/nifi/ipldata/Gujarat Lions-Mumbai Indians-2017-04-29.csv")
yka.matchWormChart(gl_mi,"Mumbai Indians","Gujarat Lions",plot=True,savePic=True, dir1=odir,picFile="matchWorm.png")