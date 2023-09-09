from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.methods.delete_message import DeleteMessage
import time

from config import TOKEN

API_TOKEN = TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    msg = await bot.send_sticker(chat_id=message.chat.id,
                                 sticker='CAACAgIAAxkBAAEKQH5k-489IQABlbQqQgTsMWpjmxRyd_kAAi4PAALNvElJfQjcrqE5xpMwBA')
    time.sleep(3)
    await bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)


if __name__ == '__main__':
    dp.run_polling(bot)
