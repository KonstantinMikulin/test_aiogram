from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

import config

BOT_TOKEN = config.TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int


button_1 = InlineKeyboardButton(text='Category 1',
                                callback_data=GoodsCallbackFactory(
                                    category_id=1,
                                    subcategory_id=0,
                                    item_id=0).pack())

button_2 = InlineKeyboardButton(text='Category 2',
                                callback_data=GoodsCallbackFactory(
                                    category_id=1,
                                    subcategory_id=0,
                                    item_id=0).pack())

markup = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2]])


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(text='This type of keyboard',
                         reply_markup=markup)


@dp.callback_query()
async def process_any_inline_btn_press(callback: CallbackQuery):
    print(callback.model_dump_json(indent=4, exclude_none=True))

    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
