from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import config

API_TOKEN: str = config.TOKEN

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# handler for command /start
@dp.message(Command(commands=['start']))
async def cmd_start(message: Message):
    await message.answer('Hello! Im the Bot!')


# handler for command /help
@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer('Send me some and I will echo')


# handler for any messages
@dp.message()
async def send_echo(message: Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
