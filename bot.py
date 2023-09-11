from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

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


@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    await callback.message.edit_text(text='BIG BUTTON 1 was pressed',
                                     reply_markup=callback.message.reply_markup)


@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(text='BIG BUTTON 2 was pressed',
                                     reply_markup=callback.message.reply_markup)


if __name__ == '__main__':
    dp.run_polling(bot)
