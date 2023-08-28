from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

import config

API_TOKEN: str = config.TOKEN
sticker = 'CAACAgIAAxkBAAIIvGTsR9sePO1SEv5YRWK2lHl83Nz1AAI0IAACVz2BSf9B1DFOwQwMMAQ'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# handler for command /start
async def cmd_start(message: Message):
    await message.answer('Hello! Im the Bot!')


# handler for command /help
async def cmd_help(message: Message):
    await message.answer('Send me some and I will echo')


# handler for photo echo
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# handler for echo sticker
async def send_sticker_echo(message: Message):
    global sticker
    print(message)

    sticker = message.sticker.file_id
    await message.bot.send_sticker(sticker=message.sticker.file_id, chat_id=message.chat.id)


# test handler for sending sticker
async def send_sticker(message: Message):
    await message.bot.send_sticker(chat_id=message.chat.id, sticker=sticker)


# handler for any messages
async def send_echo(message: Message):
    await message.answer(text=message.text)


dp.message.register(cmd_start, Command(commands=['start']))
dp.message.register(cmd_help, Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_sticker, Command(commands=['send']))
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
