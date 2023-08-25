from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import config

API_TOKEN: str = config.TOKEN

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def cmd_start(message: Message):
    await message.answer('Hello! Im the Bot!')


@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.an
