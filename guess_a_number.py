from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import random

import config

BOT_TOKEN = config.TOKEN

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS: int = 5

# dict for user`s data
user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0}


# func for getting random number
def get_random_number() -> int:
    return random.randint(1, 100)


# handler for "/start" command
@dp.message(Command(commands=['start']))
async def cmd_start(message: Message):
    await message.answer('Привет!\nДавайте сыграем в игру "Угадай число!"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду "/help"')


# handler for "/help" command
@dp.message(Command(commands=['help']))
async def cmd_stat(message: Message):
    await message.answer(f'Правила игры:\n\n Я загадываю число от 1 до  100,'
                         f'а вам нужно его угадать\nУ вас {ATTEMPTS}'
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/start - посмотреть статистику\n\nДавай сыграем?')


# handler for "/stat" command
@dp.message(Command(commands=['stat']))
async def cmd_stat(message: Message):
    await message.answer(f'Всего сыграно: {user["total_games"]}\n'
                         f'Игр выиграно: {user["wins"]}')


# handler for "/cancel" command
@dp.message(Command(commands=['cancel']))
async def cmd_cancel(message: Message):
    if user["in_game"]:
        user["in_game"] = False
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите нам об этом')
    else:
        await message.answer('А мы и не играем :)')


# handler for processing game start
@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра', 'играть',
                                'хочу играть']))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
        await message.answer('Ок!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
    else:
        await message.answer('Пока мы играем в игру, я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /start')


# handler for processing negative answer
@dp.message(F.text.lower().in_['нет', 'не', 'не хочу', 'не буду'])
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer('Жаль. Если захотите поиграть, напишите')
    else:
        await message.answer('Мы же сейчас играем. Присылайте числа от 1 до 100')


# handler for processing updates with numbers 1 to 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answers(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
            await message.answer('Ура! Вы угадали число! Сыграем еще?')
        elif int(message.text) > user['secret_number']:
            user['attempts'] -= 1
            await message.answer('Мое число меньше')
        elif int(message.text) < user['secret_number']:
            await message.answer('Мое число больше')

        if user['attempts'] == 0:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(f'''К сожалению у вас больше не осталось 
                                    попыток. Вы проиграли. Мой число было
                                    {user['secret_number']}
                                    Давайте сыграем еще?''')
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')



