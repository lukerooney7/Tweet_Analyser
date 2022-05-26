import csv
from typing import Counter
import pandas as pd
import json
import re
import datetime
import sys
from pathlib import Path

def format_date(cell):
    values = re.split('/| |:', cell)
    if (len(values) != 5):
        return "invalid input"
    return datetime.datetime(int(values[2]), int(values[1]), int(values[0]), int(values[3]), int(values[4]))

path = Path(__file__).parent.joinpath(Path("CometLanding.csv"))
df = pd.read_csv(path)
df.drop_duplicates(inplace=True) # Remove duplicate entries in the dataset
df = df[df['source'].isna() != True] # Checks for empty rows in the dataset and removes them

# Changes the times column to be in the datetime format
times = df['time']
formatted_times = []
for i in times:
    formatted_times.append(format_date(i))
df['time'] = formatted_times

# Changes the entities column so that the hashtags can be analysed more easily
entities = df['entities_str']
i=0
hashtags = [None] * df.shape[0]
for x in entities:
    if(isinstance(x, float)):
        continue
    res = json.loads(x)
    hashtags[i] = set(map(lambda x: x['text'], res['hashtags']))
    i += 1

df['hashtags'] = hashtags
