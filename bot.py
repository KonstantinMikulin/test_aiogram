from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, ReplyKeyboardRemove
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

kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Special buttons test',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
