import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.exceptions import TelegramBadRequest

import config

BOT_TOKEN = config.TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def process_any_message(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))

    await message.answer(text=message.video.file_id)


if __name__ == '__main__':
    dp.run_polling(bot)
