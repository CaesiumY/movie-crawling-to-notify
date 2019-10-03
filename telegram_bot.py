import telegram
import json

with open('token.json') as f:
    token_json = json.loads(f.read())

print(token_json["user_id"])

bot = telegram.Bot(token=token_json["token"])

for i in bot.getUpdates():
    print(i.message)

bot.sendMessage(chat_id=token_json["user_id"], text="테스트 메세지")
