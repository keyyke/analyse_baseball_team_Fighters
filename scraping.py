from bs4 import BeautifulSoup
import csv
import codecs

codecs.register_error('none', lambda e: ('', e.end))

years = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

for year in years:
    # read local file
    with open('audience_20{}.html'.format(year), 'r', encoding='shift-jis', errors='none') as f:
        res= f.read()

    # initialize beautifulsoup
    bs = BeautifulSoup(res, 'html.parser')

    # set table
    table = bs.find("table", {"class":"tschedule"})
    print('file 20{}'.format(year))
    rows = table.find_all("tr")

    with open('audience_20{}.csv'.format(year), 'w', encoding='shift-jis', errors='none') as f:
        writer = csv.writer(f)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    print('save to file 20{}'.format(year))

print('FINISH!!')