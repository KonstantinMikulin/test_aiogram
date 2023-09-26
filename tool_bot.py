from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StatesGroup, State

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import Dialog, setup_dialogs
from aiogram_dialog import DialogManager, StartMode

import config

storage = MemoryStorage()
bot = Bot(config.TOKEN)
dp = Dispatcher(storage=storage)


class MySG(StatesGroup):
    main = State()


main_window = Window(
    Const(text='Hello hello'),
    Button(Const('Some button'), id='nothing'),
    state=MySG.main
)

dialog = Dialog(main_window)
dp.include_router(dialog)
setup_dialogs(dp)


@dp.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.run_polling(bot)
