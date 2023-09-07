from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import TOKEN

API_TOKEN = TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

button_1: KeyboardButton = KeyboardButton(text='Dogs 🦮')
button_2: KeyboardButton = KeyboardButton(text='Pickles 🥒')

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Who is worse?',
                         reply_markup=keyboard)


@dp.message(F.text == 'Dogs 🦮')
async def process_dogs_answer(message: Message):
    await message.answer('Yes! dogs are worst!',
                         reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == 'Pickles 🥒')
async def process_pickles_answer(message: Message):
    await message.answer('Exactly! Pickles are worst!',
                         reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    dp.run_polling(bot)
