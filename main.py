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
    users = ['kuznetmaria']
    messages = [
        'Надо выпить водички!!!', 
        'ВОДЫЫЫЫЫЫЫ МНЕ, ВОДЫЫЫЫЫЫЫ', 
        'Я бы не отказался выпить воды, ты как?', 
        'Может немного водички?', 
        'Открывай бутылочку!', 
        'В О Д Ы'
    ]
    send_all_messages(client, users, messages)

def motivation(client):
    users = ['Daria_Soboleva']
    messages = [
        'Ты всё сможешь, брат!',
        'Я в тебя по-прежнему верю!',
        'Не сдавайся!',
        'Т Ы М О Л О Д Е Ц !',
        'Занимайся собой!',
        'Не отчаивайся!',
        'Все будет хорошо, я помогу!',
        'Ты умничка!',
        'Ты сильнее обстоятельств!',
        'Будет грустно - пиши, брат!',
    ]
    send_all_messages(client, users, messages)

# with TelegramClient('anon', api_id, api_hash, proxy=proxy, connection=connection) as client:
def main():
    with TelegramClient('anon', api_id, api_hash, proxy=proxy, connection=connection) as client:
        print(datetime.datetime.now())
        schedule.every(1).hours.do(self_check, client)
        # schedule.every(2).hours.do(stay_hydrated, client)
        # time is -3 from moscow

        # change to 30
        schedule.every().day.at("09:30").do(stay_hydrated, client) # 9:30
        schedule.every().day.at("09:30").do(motivation, client) # 9:30
        for hour in range(11, 24, 2):
            schedule.every().day.at("{}:30".format(hour)).do(stay_hydrated, client)
            schedule.every().day.at("{}:30".format(hour)).do(motivation, client)
        while True:
            schedule.run_pending()
            time.sleep(1)
    
if __name__ == "__main__":
    main()