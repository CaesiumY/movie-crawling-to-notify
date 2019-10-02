import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0150&date=20191012'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

D_DAY = "12"
day = soup.select_one('li.on > div > a > strong').text.strip()

titleMovie = []
title = soup.select('div.info-movie > a > strong')
for i in title:
    titleMovie.append(i.text.strip())

if("조커" in titleMovie and day == D_DAY):
    print(D_DAY + "일 조커의 예매가 열렸습니다.")
else:
    print(D_DAY + "일 조커의 예매가 열리지 않았습니다.")
