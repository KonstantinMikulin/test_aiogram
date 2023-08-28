from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import config

API_TOKEN: str = config.TOKEN
photo: str = 'AgACAgIAAxkBAAIJFGTsn1Ol02qYwJWe8W1did2IpwSXAALhzzEbI1FoSz611afRKQt8AQADAgADcwADMAQ'

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


# handler for send photo
@dp.message(Command(commands=['photo']))
async def send_photo(message: Message):
    global photo
    await message.bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message()
async def get_photo_id(message: Message):
    global photo

    photo = message.photo[0].file_id
    print(photo)
    await message.answer(text='Photo ID was saved')


# handler for any messages
@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Not supported')


if __name__ == '__main__':
    dp.run_polling(bot)
