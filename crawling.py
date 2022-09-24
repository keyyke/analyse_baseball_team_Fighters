import requests
import time
import codecs

codecs.register_error('none', lambda e: ('', e.end))

years = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

#set user agent
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"

# Obtain the number of audiences at games hosted by Fighters from 2009 to 2019
for year in years:
    url_audience =  'https://baseball-freak.com/audience/{}/fighters.html'.format(year)
    response = requests.get(url_audience, headers={"User-Agent": user_agent})
    response.encoding = response.apparent_encoding
    response_html = response.text
    with open('audience_20{}.html'.format(year), 'w', encoding='shift-jis', errors='none') as f:
        f.write(response_html)
    print('save to file 20{}'.format(year))
    time.sleep(1)

print('FINISH!!')