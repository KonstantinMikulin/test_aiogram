from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config

API_TOKEN: str = config.TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='YouTube',
    url='https://www.youtube.com/')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Stepik.org',
    url='https://stepik.org/learn')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2]])


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(text='These are inline buttons',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
