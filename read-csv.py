import pandas as pd
from collections import defaultdict
import csv

# df = pd.read_csv('./output_file.csv')
# column = df['COURSE No.']

columns = defaultdict(list) # each value in each column is appended to a list

with open('output_file.csv') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
	for (i,v) in enumerate(row):
	    columns[i].append(v)

# print(columns[3])
