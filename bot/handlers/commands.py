from random import randint

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode, ShowMode

from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import add_score, get_total_score_for_user
from bot.dialogs import ScoreSG

router = Router(name='comands router')


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Hello')


@router.message(Command('score'))
async def score_cmd(
    message: Message,
    # session: AsyncSession,
    dialog_manager: DialogManager
    ):
    await dialog_manager.start(
        state=ScoreSG.fill_score,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.DELETE_AND_SEND
    )
    
    # score = randint(1, 100)
    
    # await add_score(
    #     session=session,
    #     telegram_id=message.from_user.id, #type:ignore
    #     score=score
    # )
    # await message.answer(f"You got {score}")


@router.message(Command('stats'))
async def stats_cmd(message: Message, session: AsyncSession):
    total_score: int = await get_total_score_for_user(
        session=session,
        telegram_id=message.from_user.id #type:ignore
    )
    
    await message.answer(f"Your total score is {total_score}")
