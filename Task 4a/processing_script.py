import pandas as pd
import json
import sys

inputloc = sys.argv[1]
outputloc = sys.argv[2]
data = pd.read_csv(inputloc)

to_json = data[['Location', 'Name']].copy()

to_json.to_json(outputloc,orient='records')