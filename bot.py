from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config

API_TOKEN: str = config.TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

group_name = 'aiogram_stepik_course'
url_btn_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Группа "Телеграм-боты на AIOgram"',
    url=f"tg://resolve?domain={group_name}")

user_id = 828900493
url_btn_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Автор курса на Степике по телеграм-ботам',
    url=f'tg://user?id={user_id}')

channel_name = 'toBeAnMLspecialist'
url_btn_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Канал "Стать специалистом по машинному обучению"',
    url=f'https://t.me/{channel_name}')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_btn_1],
                     [url_btn_2],
                     [url_btn_3]])


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(text='These are inline buttons',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
