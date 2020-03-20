import yorkpy.analytics as yka
import argparse
parser = argparse.ArgumentParser(description='convert')
parser.add_argument("yamlFile",help="YAML File")
args=parser.parse_args()
yamlFile=args.yamlFile
yka.convertYaml2PandasDataframeT20(yamlFile,"/Users/tvganesh/backup/software/nifi/ipl","/Users/tvganesh/backup/software/nifi/ipldata")
