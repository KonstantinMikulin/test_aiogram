from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import TOKEN

API_TOKEN = TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)],
    [KeyboardButton(text=str(i)) for i in range(7, 9)]]

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Special buttons test',
                         reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
