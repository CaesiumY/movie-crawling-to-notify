# 영화 예매 알리미 봇
파이썬 크롤링으로 텔레그램 영화 예매 오픈 알리미 만들기!

## 사용하기

1. 깃 저장소를 클론.
2. `token.json` 파일을 생성하고 예시처럼 작성.
>예시 
```json
{
    "token": "텔레그램 봇 토큰",
    "user_id": "자신의 유저 아이디"
}
```

3. `D_DAY, MOVIE, TIME, url` 변수를 자신의 입맛대로 바꾼다.
4. 자신의 가상환경을 만들고, `pip install -r requirements.txt` 입력.
5. `python crawler.py` 로 실행.


## 텔레그램 봇 스크린샷

![telegram](https://raw.githubusercontent.com/CaesiumY/movie-crawling-to-notify/master/images/telegram_test.png)

### 기타
- 아마존 EC2에 올리는 건 생각만 해볼 예정... 프리티어가 끝나서...