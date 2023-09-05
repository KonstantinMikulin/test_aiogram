from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config_data.config import load_config

config = load_config('C:\\Users\\user\\PycharmProjects\\test_aiogram\\test_bot_aiogram\\config_data\\.env')

API_TOKEN: str = config.tg_bot.token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# handler for command /start
@dp.message(Command(commands=['start']))
async def cmd_start(message: Message):
    await message.answer('Hello! Im the Bot!')


# handler for command /help
@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer('Send me some and I will echo')


# handler for voice message
@dp.message()
async def process_any_message(message: Message):
    await message.answer(message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
