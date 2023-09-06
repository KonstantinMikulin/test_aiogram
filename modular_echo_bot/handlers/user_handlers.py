from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
