from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, KICKED, MEMBER
from aiogram.types import Message, ContentType, ChatMemberUpdated

import config

BOT_TOKEN = config.TOKEN

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello hello')


@dp.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer('I can do some')


@dp.message(F.photo)
async def process_phot(message: Message):
    await message.answer('You send photo')


@dp.message(F.content_type.in_({ContentType.VOICE,
                                ContentType.VIDEO,
                                ContentType.TEXT}))
async def process_vovite(message: Message):
    await message.answer('You send voice or video or text')


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'User {event.from_user.id} blocked bot')


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def process_user_restart_bot(event: ChatMemberUpdated):
    print(f'User {event.from_user.id} restart bot')


async def process_any(message: Message):
    await message.answer('I do not understand')


if __name__ == '__main__':
    dp.run_polling(bot)
