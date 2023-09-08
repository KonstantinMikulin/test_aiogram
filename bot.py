from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import TOKEN

API_TOKEN = TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons: list[KeyboardButton] = [KeyboardButton(text=f'Button {i+1}') for i in range(10)]
kb_builder.add(*buttons)
kb_builder.adjust(2, 1, repeat=True)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Who is worse?',
                         reply_markup=kb_builder.as_markup(resizw_keyboard=True))


if __name__ == '__main__':
    dp.run_polling(bot)
