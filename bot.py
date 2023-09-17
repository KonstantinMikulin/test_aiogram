from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import config

BOT_TOKEN = config.TOKEN

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(
        text='Привет!\n\nЯ бот, демонстрирующий '
             'как работает HTML-разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/bold - жирный текст\n'
             '/italic - наклонный текст\n'
             '/underline - подчеркнутый текст\n'
             '/spoiler - спойлер'
    )


@dp.message(Command(commands=['help']))
async def process_help_cmd(message: Message):
    await message.answer(
        text='Я бот, демонстрирующий '
             'как работает HTML-разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/bold - жирный текст\n'
             '/italic - наклонный текст\n'
             '/underline - подчеркнутый текст\n'
             '/spoiler - спойлер'
    )


@dp.message(Command(commands=['bold']))
async def process_bold_cmd(message: Message):
    await message.answer(
        text='<b>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'делающая текст жирным.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</b>'
    )


@dp.message(Command(commands=['italic']))
async def process_italic_cmd(message: Message):
    await message.answer(
        text='<i>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'делающая текст наклонным.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</i>'
    )


@dp.message(Command(commands=['underline']))
async def process_underline_cmd(message: Message):
    await message.answer(
        text='<u>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'делающая текст подчеркнутым.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</u>'
    )


@dp.message(Command(commands=['spoiler']))
async def process_spoiler_cmd(message: Message):
    await message.answer(
        text='<tg-spoiler>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'убирающая текст под спойлер.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</tg-spoiler>'
    )


@dp.message()
async def process_any_cmd(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду\n\n'
             'Чтобы посмотреть список доступных команд - '
             'отправь команду /help'
    )


if __name__ == '__main__':
    dp.run_polling(bot)
