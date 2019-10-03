import requests
import telegram
import json
from bs4 import BeautifulSoup

with open('token.json') as f:
    token_json = json.loads(f.read())

bot = telegram.Bot(token=token_json["token"])
D_DAY = "03"
MOVIE = "조커"

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0150&date=201910' + D_DAY
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

day = soup.select_one('li.on > div > a > strong').text.strip()
titleMovie = []
title = soup.select('div.info-movie > a > strong')
for i in title:
    titleMovie.append(i.text.strip())

if(MOVIE in titleMovie and day == D_DAY):
    messageSuccess = D_DAY + "일 " + MOVIE + "의 예매가 열렸습니다."
    bot.sendMessage(chat_id=token_json["user_id"], text=messageSuccess)
else:
    messageFailure = D_DAY + "일 " + MOVIE + "의 예매가 열리지 않았습니다."
    bot.sendMessage(chat_id=token_json["user_id"], text=messageFailure)
