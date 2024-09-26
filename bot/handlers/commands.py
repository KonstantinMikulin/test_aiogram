from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router(name='comands router')


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Hello')
