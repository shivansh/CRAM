from bs4 import BeautifulSoup
import urllib2
import csv

for roll in range(11001, 11800):
    url = "http://172.26.142.68/dccourse/studdc.php?roll_no=" + str(roll)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    # soup = BeautifulSoup(open('test.html'))

    table = soup.find('table')
    # headers = [header.text for header in table.find_all('th')]

    rows = []

    for row in table.find_all('tr'):
        rows.append([val.text.encode('utf8') for val in row.find_all('td')])
        # print '\n'.join(row.stripped_strings)

    for nrow in rows:
        nrow.append(str(roll))

    with open('output_file.csv', 'a') as f:
        writer = csv.writer(f)
        # writer.writerow(headers)
        writer.writerows(row for row in rows if row)
