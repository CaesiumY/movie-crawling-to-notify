import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0150&date=20191005'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
list = soup.select('div.info-movie')

for i in list:
    print(i.select_one('a > strong').text.strip())