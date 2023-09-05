from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


API_TOKEN: str =

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# handler for command /start
@dp.message(Command(commands=['start']))
async def cmd_start(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))

    await message.answer('Hello! Im the Bot!')


# handler for command /help
@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer('Send me some and I will echo')


# handler for voice message
@dp.message(F.voice)
async def process_voice(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))

    await message.answer(text='It was voice')


if __name__ == '__main__':
    dp.run_polling(bot)
