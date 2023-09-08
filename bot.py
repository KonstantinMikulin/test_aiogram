from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import TOKEN

API_TOKEN = TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

contact_btn: KeyboardButton = KeyboardButton(text='Send phone number',
                                             request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(text='Send location',
                                         request_location=True)
poll_btn: KeyboardButton = KeyboardButton(text='Make poll',
                                          request_poll=KeyboardButtonPollType())
web_app_btn: KeyboardButton = KeyboardButton(text='Start web app',
                                             web_app=WebAppInfo(url="https://stepik.org/"))
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[web_app_btn]],
                                                            resize_keyboard=True)

kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)

btn_1: KeyboardButton = KeyboardButton(text='Button 1')
btn_2: KeyboardButton = KeyboardButton(text='Button 2')

placeholder_example_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[btn_1, btn_2]],
                                                                  resize_keyboard=True,
                                                                  input_field_placeholder='Press button 1')


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Special buttons test',
                         reply_markup=keyboard)


@dp.message(Command(commands=['web_app']))
async def cmd_web_app(message: Message):
    await message.answer(text='Web app test',
                         reply_markup=web_app_keyboard)


@dp.message(Command(commands=['placeholder']))
async def cmd_placeholder(message: Message):
    await message.answer(text='Placeholder test',
                         reply_markup=placeholder_example_kb)


if __name__ == '__main__':
    dp.run_polling(bot)
