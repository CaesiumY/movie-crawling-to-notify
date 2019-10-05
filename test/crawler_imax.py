import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0150&date=20191005'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

imax = soup.select_one('span.imax')

if(imax):
    print('IMAX 이용 가능')
else:
    print('IMAX 이용불가')
