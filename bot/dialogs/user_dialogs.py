from aiogram.types import Message

from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput

from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.requests import add_score
from .states import ScoreSG


def validate_score(text: str) -> str | None:
    score = int(text)
    if 1 <= score <= 100:
        return text
    
    raise ValueError


async def score_fill_correct(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
    # session: AsyncSession
):
    score = int(text)
    
    session = dialog_manager.middleware_data.get("session")
    
    await add_score(
        session=session, #type:ignore
        telegram_id=message.from_user.id, #type:ignore
        score=score
    )
    await message.answer(f"Your score: {score} was added to database")
    await dialog_manager.reset_stack()


async def score_fill_error(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
):
    await message.answer('Score must be integer')

 
score_dialog = Dialog(
    Window(
        Const("Enter you score, please"),
        TextInput(
            id="fill_score",
            type_factory=validate_score,
            on_success=score_fill_correct, # type:ignore
            on_error=score_fill_error # type:ignore
        ),
        state=ScoreSG.fill_score,
    )
)
