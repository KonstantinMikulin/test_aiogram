from pprint import pprint

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

import config

API_TOKEN = config.TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher()

big_button_1 = InlineKeyboardButton(text='BIG BUTTON 1',
                                    callback_data='big_button_1_pressed')
big_button_2 = InlineKeyboardButton(text='BIG BUTTON 2',
                                    callback_data='big_button_2_pressed')

keyboard = InlineKeyboardMarkup(inline_keyboard=[[big_button_1],
                                                 [big_button_2]])


@dp.message(CommandStart)
async def process_start_cmd(message: Message):
    await message.answer(text='Press any inline button',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
