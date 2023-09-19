from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, PhotoSize

import config

BOT_TOKEN = config.TOKEN

storage = MemoryStorage()

bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=storage)

user_dict: dict[int, dict[str | int | bool]] = {}


class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_gender = State()
    upload_photo = State()
    fill_education = State()
    fill_wish_news = State()


@dp.message(CommandStart(), StateFilter(default_state))
async def process_start_cmd(message: Message):
    await message.answer(
        text='Этот бот демонстрирует работу FSM\n\n'
             'Чтобы перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )


@dp.message(Command(commands=['cancel']), State(default_state))
async def process_cancel_cmd(message: Message):
    await message.answer(
        text='Отменять нечего. Вы вне машины состояний\n\n'
             'Чтобы перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )


@dp.message(Command(commands=['cancel']), ~StateFilter(default_state))
async def process_cancel_cmd_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы вышли из машины состояний\n\n'
             'Чтобы снова перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )
    await state.clear()


@dp.message(Command(commands=['fillform']), StateFilter(default_state))
async def process_fillform_cmd(message: Message, state: FSMContext):
    await message.answer(text='Пожалуйста, введите ваше имя')
    await state.set_state(FSMFillForm.fill_name)


@dp.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите ваш возраст')
    await state.set_state(FSMFillForm.fill_age)


@dp.message(StateFilter(FSMFillForm.fill_name))
async def warning_not_name(message: Message):
    await message.answer(
        text='То, что вы отправили не похоже на имя\n\n'
             'Пожалуйста, введите ваше имя\n\n'
             'Если вы хотите прервать заполнение анкеты - '
             'отправьте команду /cancel'
    )


# Хэндлер, если введен корректный возраст и переводим в выбор пола
@dp.message(StateFilter(FSMFillForm.fill_age), lambda x: x.text.isdigit() and 4 <= int(x.text) <= 120)
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    male_button = InlineKeyboardButton(
        text='Мужской ♂',
        callback_data='male'
    )
    female_button = InlineKeyboardButton(
        text='Женский ♀',
        callback_data='female'
    )
    undefined_button = InlineKeyboardButton(
        text='🤷 Пока не ясно',
        callback_data='undefined_gender'
    )
    keyboard: list[list[InlineKeyboardButton]] = [
        [male_button, female_button],
        [undefined_button]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    await message.answer(
        text='Спасибо!\n\nУкажите ваш пол',
        reply_markup=markup
    )
    await state.set_state(FSMFillForm.fill_gender)


# Хэндлер, если возраст введен некорректно
@dp.message(StateFilter(FSMFillForm.fill_age))
async def warning_not_age(message: Message):
    await message.answer(
        text='Возраст должен быть целым числом от 4 до 120\n\n'
             'Попробуйте еще раз\n\nЕсли вы хотите прервать '
             'заполнение анкеты - отправьте команду /cancel'
    )


# Хэндлер нажатия выбора пола и перевод в состояния отправки фото
@dp.callback_query(StateFilter(FSMFillForm.fill_gender), F.data.in_(['male', 'female', 'undefined_gender']))
async def process_gender_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await callback.message.delete()
    await callback.message.answer(
        text='Спасибо! А теперь загрузите, пожалуйста, ваше фото'
    )
    await state.set_state(FSMFillForm.upload_photo)


# Хэндлер, если во время выбора пола было введено что-то некорректное
@dp.message(StateFilter(FSMFillForm.fill_gender))
async def warning_not_gender(message: Message):
    await message.answer(
        text='Пожалуйста, пользуйтесь кнопками '
             'при выборе пола\n\nЕсли вы хотите прервать '
             'заполнение анкеты - отправьте команду /cancel'
    )


# Хэндлер, если отправлено фото и перевод в состояние выбора образования
@dp.message(StateFilter(FSMFillForm.upload_photo), F.photo[-1].as_('largest_photo'))
async def process_photo_sent(message: Message, state: FSMContext, largest_photo: PhotoSize)
    await state.update_data(
        photo_unuque_id=largest_photo.file_unique_id,
        photo_id=largest_photo.file_id
    )
    secondary_button = InlineKeyboardButton(
        text='Среднее',
        callback_data='secondary'
    )
    higher_button = InlineKeyboardButton(
        text='Высшее',
        callback_data='higher'
    )
    no_edu_button = InlineKeyboardButton(
        text='🤷 Нету',
        callback_data='no_edu'
    )
    keyboard: list[list[InlineKeyboardButton]] = [
        [secondary_button], [higher_button],
        [no_edu_button]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    await message.answer(
        text='Спасибо!\n\nУкажите ваше образование',
        reply_markup=markup
    )


# Хэндлер, если отправлено не фото
@dp.message(StateFilter(FSMFillForm.upload_photo))
async def warning_not_photo(message: Message):
    await message.answer(
        text='Пожалуйста, на этом шаге отправьте '
             'ваше фото\n\nЕсли вы хотите прервать '
             'заполнение анкеты - отправьте команду /cancel'
    )


# Хэндлер, если выбрано образование и перевод в состояние новостей
@dp.callback_query(StateFilter(FSMFillForm.fill_education), F.data.in_(['secondary', 'higher', 'no_edu']))
async def process_education_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(education=callback.data)
    yes_news_button = InlineKeyboardButton(
        text='Да',
        callback_data='yes_news'
    )
    no_news_button = InlineKeyboardButton(
        text='Нет, спасибо',
        callback_data='no_news'
    )
    keyboard: list[list[InlineKeyboardButton]] = [
        [yes_news_button, no_news_button]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    await callback.message.edit_text(
        text='Спасибо!\n\nОстался последний шаг.\n'
             'Хотели бы вы получать новости?',
        reply_markup=markup
    )
    await state.set_state(FSMFillForm.fill_wish_news)


# Хэндлер, если не корректно выбрано образование
@dp.message(StateFilter(FSMFillForm.fill_education))
async def warning_not_education(message: Message):
    await message.answer(
        text='Пожалуйста, пользуйтесь кнопками при выборе образования\n\n'
             'Если вы хотите прервать заполнение анкеты - отправьте '
             'команду /cancel'
    )


# Хэндлер на выбор новостей и вывод из машины состояний
@dp.





































