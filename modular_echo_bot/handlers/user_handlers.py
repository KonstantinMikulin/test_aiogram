from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from ..lexicon.lexicon import LEXICON_RU


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
