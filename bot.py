from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ContentType

import config

BOT_TOKEN = config.TOKEN

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello hello')


@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer('I can do some')


@dp.message(F.photo)
async def process_phot(message: Message):
    await message.answer('You send photo')


@dp.message(F.content_type.in_({ContentType.VOICE,
                                ContentType.VIDEO,
                                ContentType.TEXT}))
async def process_vovite(message: Message):
    await message.answer('You send voice or video or text')


async def process_any(message: Message):
    await message.answer('I do not understand')


if __name__ == '__main__':
    dp.run_polling(bot)
