from telethon import TelegramClient, events, sync
from telethon.tl.functions.help import GetProxyDataRequest
from telethon.network.connection import ConnectionTcpMTProxyRandomizedIntermediate

import time
import random
import schedule
import datetime

api_id = '848784'
api_hash = '6209aac0cb13a940ef2b2a2d80a83451'
connection = ConnectionTcpMTProxyRandomizedIntermediate
server = 'russia.proxy.digitalresistance.dog'
port = 443
secret = 'd41d8cd98f00b204e9800998ecf8427e'
proxy = (server, port, secret)

# hydrated

def send_all_messages(client, users, messages):
    for user in users:
        client.send_message(user, random.choice(messages))

def self_check(client):
    users = ['me']
    messages = ['check']
    send_all_messages(client, users, messages)

def stay_hydrated(client):
    now = datetime.datetime.now()
    if now.hour >= 9 and now.hour < 24 and now.minute == 30: 
        users = ['kuznetmaria']
        messages = ['Надо выпить водички!!!', 'ВОДЫЫЫЫЫЫЫ МНЕ, ВОДЫЫЫЫЫЫЫ', 'Я бы не отказался выпить воды, ты как?', 'Может немного водички?', 'Открывай бутылочку!', 'В О Д Ы']
        send_all_messages(client, users, messages)

def good_morning(client):
    delay = random.randint(1, 60 * 5)
    users = ['avgaydashenko']
    messages = ['С Добрый утром! Удачного дня (:', ' Доброе утро, хорошего дня!', 'Держи плюс настроение на день!', ']
    time.sleep(delay)
    send_all_messages(client, users, messages)

def good_night(client):
    delay = random.randint(1, 60 * 5)
    users = ['avgaydashenko']
    messages = ['Спокойной ночи :з', 'Сладких снов (:', 'Доброй ночи!', 'Good night!', ' Волшебных слов!']
    time.sleep(delay)
    send_all_messages(client, users, messages)


# with TelegramClient('anon', api_id, api_hash, proxy=proxy, connection=connection) as client:
def main():
    with TelegramClient('anon', api_id, api_hash, proxy=proxy, connection=connection) as client:
        schedule.every(30).seconds.do(self_check, client)
        # schedule.every(2).hours.do(stay_hydrated, client)
        schedule.every().day.at("09:30").do(stay_hydrated, client)
        for hour in range(10, 24):
            schedule.every().day.at("{}:30".format(hour)).do(stay_hydrated, client)
        schedule.every().day.at("08:00").do(good_morning, client)
        schedule.every().day.at("23:30").do(good_night, client)
        while True:
            schedule.run_pending()
            time.sleep(1)
    
if __name__ == "__main__":
    main()