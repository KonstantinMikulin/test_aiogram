from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import random

import config

BOT_TOKEN: str = config.TOKEN

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS: int = 5

users: dict = {}


# func for getting random number
def get_random(x: int, y: int) -> int:
    return random.randint(x, y)


# handler for processing command "/start"
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду "/help"')

    # if users` ID not in db
    if message.from_user.id not in users:
        users[message.from_user.id]: dict = {'in_game': False,
                                             'secret_number': None,
                                             'attempts': None,
                                             'total_games': 0,
                                             'wins': 0}


# handler for processing command "/help"
@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам  нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавайте сыграем?')


# handler for processing command "/stat"
@dp.message(Command(commands=['stat']))
async def cmd_stat(message: Message):
    await message.answer(f'Всего игр сыграно: '
                         f'{users[message.from_user.id]["total_games"]}\n'
                         f'Игр выиграно: '
                         f'{users[message.from_user.id]["wins"]}')


# handler for command "/cancel"
@dp.message(Command(commands=['cancel']))
async def cmd_cancel(message: Message):
    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
    else:
        await message.answer('А мы и так не играем. '
                             'Может, сыграем разок?')


# handler for positive for game
@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра',
                                'играть', 'хочу играть']))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random(1, 100)
        users[message.from_user.id]['attempts'] = ATTEMPTS
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100 '
                             'попробуй угадать!')
    else:
        await message.answer('Пока мы играем в игру, я могу '
                             'реагировать только на числа от 1 до 100'
                             'и команды /cancel и /stat')


# handler for negative game
@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами уже играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


# handler for processing numbers from user
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_number_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
            await message.answer('Ура! Вы угадали число!\n\n'
                                 'Сыграем еще?')
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('Мое число меньше')
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('Мое число больше')

        if users[message.from_user.id]['attempts'] == 0:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :)\n\nМой число '
                                 f'было {users[message.from_user.id]["secret_number"]}'
                                 f'\n\nДавайте сыграем еще раз?')
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


# handler for processing any other messages
@dp.message()
async def process_any_messages(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('Мы же с вами играем.'
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')


if __name__ == '__main__':
    dp.run_polling(bot)
