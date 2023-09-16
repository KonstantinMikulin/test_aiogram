import copy
from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

import config

BOT_TOKEN = config.TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

FIELD_SIZE = 8

LEXICON = {
    '/start': 'Вот твое поле. Можешь делать ход',
    0: ' ',
    1: '🌊',
    2: '💥',
    'miss': 'Мимо!',
    'hit': 'Попал!',
    'used': 'Вы уже стреляли сюда!',
    'next_move': 'Делайте ваш следующий ход'}

ships: list[list[int]] = [
    [1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0]]

users: dict[int, dict[str, list]] = {}


class FieldCallbackFactory(CallbackData, prefix='user_field'):
    x: int
    y: int


def reset_field(user_id: int) -> None:
    users[user_id]['ships'] = copy.deepcopy(ships)
    users[user_id]['field'] = [[0 for _ in range(FIELD_SIZE)]
                               for _ in range(FIELD_SIZE)]


def get_field_kb(user_id: int) -> InlineKeyboardMarkup:
    array_buttons: list[list[InlineKeyboardButton]] = []

    for i in range(FIELD_SIZE):
        array_buttons.append([])
        for j in range(FIELD_SIZE):
            array_buttons[i].append(InlineKeyboardButton(
                text=LEXICON[users[user_id]['field'][i][j]],
                callback_data = FieldCallbackFactory(x=i, y=j).pack()
            ))

    markup = InlineKeyboardMarkup(inline_keyboard=array_buttons)

    return markup


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {}

    reset_field(message.from_user.id)

    await message.answer(text=LEXICON['/start'],
                         reply_markup=get_field_kb(message.from_user.id))


@dp.callback_query(FieldCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery,
                                 callback_data: FieldCallbackFactory):
    field = users[callback.from_user.id]['field']
    ships = users[callback.from_user.id]['ships']

    if field[callback_data.x][callback_data.y] == 0 and \
            ships[callback_data.x][callback_data.y] == 0:
        answer = LEXICON['miss']
        field[callback_data.x][callback_data.y] = 1
    elif field[callback_data.x][callback_data.y] == 0 and \
            ships[callback_data.x][callback_data.y] == 1:
        answer = LEXICON['hit']
        field[callback_data.x][callback_data.y] = 2
    else:
        answer = LEXICON['used']

    try:
        await callback.message.edit_text(
            text=LEXICON['next_move'],
            reply_markup=get_field_kb(callback.from_user.id)
        )
    except TelegramBadRequest:
        pass

    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
