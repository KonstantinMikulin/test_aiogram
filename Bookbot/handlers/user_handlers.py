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


# TODO: Done
@router.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(LEXICON[message.text])

    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


# TODO: Done
@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message):
    await message.answer(LEXICON[message.text])


# TODO: Done
@router.message(Command(commands=['beginning']))
async def process_beginning_cmd(message: Message):
    users_db[message.from_user.id]['page'] = 1
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(text=text,
                         reply_markup=create_pagination_keyboard(
                             'backward', f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                             'forward'))


# TODO: Done
@router.message(Command(commands=['continue']))
async def process_continue_cmd(message: Message):
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(text=text,
                         reply_markup=create_pagination_keyboard(
                             'backward',
                             f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                             'forward'))


# TODO: Done
@router.message(Command(commands=['bookmarks']))
async def process_bookmarks_cmd(message: Message):
    if users_db[message.from_user.id]['bookmarks']:
        await message.answer(text=LEXICON[message.text],
                             reply_markup=create_bookmarks_keyboard(
                                 *users_db[message.from_user.id]['bookmarks']
                             ))
    else:
        await message.answer(text=LEXICON['no_bookmarks'])


# TODO: выводить alert, если не происходит никакое действие
@router.callback_query(F.data == 'forward')
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < len(book):
        users_db[callback.from_user.id]['page'] += 1
        text = book[users_db[callback.from_user.id]['page']]
        await callback.message.edit_text(text=text,
                                         reply_markup=create_pagination_keyboard(
                                             'backward',
                                             f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                                             'forward'))
    else:
        await callback.answer(text='This is last page')

    await callback.answer()


# TODO: выводить alert, если не происходит никакое действие
@router.callback_query(F.data == 'backward')
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        text = book[users_db[callback.from_user.id]['page']]

        await callback.message.edit_text(text=text,
                                         reply_markup=create_pagination_keyboard(
                                             'backward',
                                             f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                                             'forward'
                                         ))
    else:
        await callback.answer(text='This is first page')

    await callback.answer()


# TODO: Done
@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
async def process_page_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].add(users_db[callback.from_user.id]['page'])

    await callback.answer('Страница добавлена в закладки!')


# TODO: проверить после исправления хэндлера "/bookmarks"
@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery):
    text = book[int(callback.data)]
    users_db[callback.from_user.id]['page'] = int(callback.data)

    await callback.message.edit_text(text=text,
                                     reply_markup=create_pagination_keyboard(
                                         'backward', f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
                                         'forward'
                                     ))
    await callback.answer()


# TODO: проверить после исправления хэндлера "/bookmarks"
@router.callback_query(F.data == 'edit_bookmarks')
async def process_edit_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON[callback.data],
                                     reply_markup=create_edit_keyboard(
                                         *users_db[callback.from_user.id]['bookmarks']
                                     ))
    await callback.answer()


# TODO: проверить после исправления хэндлера "/bookmarks"
@router.callback_query(F.data == 'cancel')
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['cancel_text'])
    await callback.answer()


# TODO: проверить после исправления хэндлера "/bookmarks"
@router.callback_query(IsDelBookmarkCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].remove(int(callback.data[:-3]))

    if users_db[callback.from_user.id]['bookmarks']:
        await callback.message.edit_text(text=LEXICON['/bookmarks'],
                                         reply_markup=create_edit_keyboard(
                                             *users_db[callback.from_user.id]['bookmarks']
                                         ))
    else:
        await callback.message.edit_text(text=LEXICON['no_bookmarks'])

    await callback.answer()
