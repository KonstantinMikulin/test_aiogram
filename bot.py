from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import TOKEN

API_TOKEN = TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

button_1: KeyboardButton = KeyboardButton(text='Dogs 🦮')
button_2: KeyboardButton = KeyboardButton(text='Pickles 🥒')
button_3: KeyboardButton = KeyboardButton(text='Ducks?')
button_4: KeyboardButton = KeyboardButton(text='Cats?')

keyboard_1: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2], [button_3, button_4]],
                                                      resize_keyboard=True,
                                                      one_time_keyboard=True)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Who is worse?',
                         reply_markup=keyboard_1)


@dp.message(F.text == 'Dogs 🦮')
async def process_dogs_answer(message: Message):
    await message.answer('Yes! dogs are worst!')


@dp.message(F.text == 'Pickles 🥒')
async def process_pickles_answer(message: Message):
    await message.answer('Exactly! Pickles are worst!')


@dp.message(F.text == 'Ducks?')
async def process_pickles_answer(message: Message):
    await message.answer('Ducks???')


@dp.message(F.text == 'Cats?')
async def process_pickles_answer(message: Message):
    await message.answer('Cats???')

if __name__ == '__main__':
    dp.run_polling(bot)
