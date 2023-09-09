from aiogram import Router
from aiogram.types import Message
from rps_game_bot.lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()


@router.message()
async def process_any_message(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
