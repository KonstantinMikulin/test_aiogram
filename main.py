import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '5751024125:AAFHkyBrgab3LVI_OpmmpHoyhw-ts2Dqlo4'
TEXT = 'Hello hello'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt = ', counter)

    update = requests.get(f'{API_URL}{BOT_TOKEN}/getupdates?offset={offset+1}').json()

    if update['result']:
        for result in update['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1
