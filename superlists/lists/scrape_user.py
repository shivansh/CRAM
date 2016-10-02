from bs4 import BeautifulSoup
import csv
import pandas as pd
from collections import defaultdict
import os

import urllib.request

def scrape(roll):
    url = "http://172.26.142.68/dccourse/studdc.php?roll_no=" + str(roll)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response.read(), "lxml")

    table = soup.find('table')

    rows = []

    for row in table.find_all('tr'):
        rows.append([val.text.encode('utf8') for val in row.find_all('td', limit=4)])

    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(row for row in rows if row)

    columns = defaultdict(list) # each value in each column is appended to a list

    with open('output.csv') as f:
        reader = csv.reader(f)
        # reader.next()
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v[3:len(v)-2])

    # Output file is no longer required
    os.remove('output.csv')

    return columns[2]

