from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

import config

API_TOKEN: str = config.TOKEN

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command='/help',
                                     description='About bot'),
                          BotCommand(command='/support',
                                     description='Command for support'),
                          BotCommand(command='/contacts',
                                     description='Get contacts'),
                          BotCommand(command='/payments',
                                     description='How to pay')]

    await bot.set_my_commands(main_menu_commands)


if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)