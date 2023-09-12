from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from Bookbot.database.database import user_dict_template, users_db
from Bookbot.filters.filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from Bookbot.keyboards.bookmarks_kb import create_bookmarks_keyboard, create_edit_keyboard
from Bookbot.keyboards.pagination_kb import create_pagination_keyboard
from Bookbot.lexicon.lexicon import LEXICON
from Bookbot.services.file_handling import book

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(LEXICON[message.text])

    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands=['beginning']))
async def process_beginning_cmd(message: Message):
    users_db[message.from_user.id]['page'] = 1
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(text=text,
                         reply_markup=create_pagination_keyboard(
                             'backward', f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                             'forward'))


@router.message(Command(commands=['continue']))
async def process_continue_cmd(message: Message):
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(text=text,
                         reply_markup=create_pagination_keyboard(
                             'backward',
                             f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                             'forward'))


@router.message(Command(commands=['bookmarks']))
async def process_bookmarks_cmd(message: Message):
    if users_db[message.from_user.id]['bookmarks']:
        await message.answer(text=LEXICON[message.text],
                             reply_markup=create_bookmarks_keyboard(
                                 *users_db[message.from_user.id]['bookmarks']
                             ))
    else:
        await message.answer(text=LEXICON['no_bookmarks'])


