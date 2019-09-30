import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0150&date=20191005'
html = requests.get(url)
print(html.text)