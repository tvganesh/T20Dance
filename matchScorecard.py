import pandas as pd
import yorkpy.analytics as yka

import yorkpy.analytics as yka
import argparse
parser = argparse.ArgumentParser(description='MatchWorm')
parser.add_argument("odir",help="output directory")
args=parser.parse_args()
odir=args.odir

csk_kxip=pd.read_csv("/Users/tvganesh/backup/software/nifi/ipldata/Chennai Super Kings-Kings XI Punjab-2014-05-30.csv")
scorecard,extras=yka.teamBattingScorecardMatch(csk_kxip,"Chennai Super Kings")
print("Batting scorecard of Chennai Super Kings - vs Kings X1 Punjab on 30 May 2014")
print("\n")
print(scorecard)
