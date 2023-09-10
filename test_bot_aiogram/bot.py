import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config_data.config import load_config
from keyboards.set_menu import set_main_menu
from aiogram import Router


async def main():
    config = load_config('C:/Users/user/PycharmProjects/test_aiogram/test_bot_aiogram/config_data/.env')
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await set_main_menu(bot)


if __name__ == '__main__':
    asyncio.run(main())
