import pandas as pd
import os
import yorkpy.analytics as yka
import argparse

parser = argparse.ArgumentParser(description='bowlingWicketKind')
parser.add_argument("idir",help="input directory")
args=parser.parse_args()
idir=args.idir


path=os.path.join(idir,"Chennai Super Kings-allMatchesAllOpposition.csv") 
csk_matches = pd.read_csv(path)

m=yka.teamBatsmenPartnershiAllOppnAllMatches(csk_matches,'Chennai Super Kings',report="summary")
print("Highest partnerships of Chennai Super Kings")
print("\n")
print(m)
