import requests
import time
import config

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN: str = config.TOKEN
offset: int = -2
timeout: int = 10
updates: dict


def do_something() -> None:
    print('Was update')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Update`s time to Telegram Bot API: {end_time - start_time}')
