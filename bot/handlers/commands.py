from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode, ShowMode

from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import get_total_score_for_user
from bot.dialogs import ScoreSG, StatsSG

router = Router(name='comands router')


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Hello')


@router.message(Command('score'))
async def score_cmd(
    message: Message,
    dialog_manager: DialogManager
    ):
    await dialog_manager.start(
        state=ScoreSG.fill_score,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.DELETE_AND_SEND
    )


@router.message(Command('stats'))
async def stats_cmd(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=StatsSG.get_stats,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.DELETE_AND_SEND
    )
