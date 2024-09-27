from random import randint

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import add_score

router = Router(name='comands router')


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Hello')


@router.message(Command('score'))
async def score_cmd(message: Message, session: AsyncSession):
    score = randint(1, 100)
    
    await add_score(
        session=session,
        telegram_id=message.from_user.id, #type:ignore
        score=score
    )
    await message.answer(f"You got {score}")
