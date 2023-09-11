from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexion.lexicon import LEXICON, BUTTONS
from keyboards.keyboards import create_inline_kb

import config

API_TOKEN = config.TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    keyboard = create_inline_kb(2, 'but_1', 'but_2', 'but_3')
    await message.answer(text='Это инлайн-клавиатура, сформированная функцией '
                              '<code>create_inline_kb</code>',
                         reply_markup=keyboard,
                         parse_mode='HTML')


if __name__ == '__main__':
    dp.run_polling(bot)
