from aiogram import Bot, Dispatcher, F
from aiogram.types import (CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup,
                           InputMediaAudio, InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command
from aiogram.exceptions import TelegramBadRequest

import config

BOT_TOKEN = config.TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением,'
              'но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через'
              'редактирование.',
    'photo_id1': config.photos[0],
    'photo_id2': config.photos[1],
    'voice_id1': config.voices[0],
    'voice_id2': config.voices[1],
    'audio_id1': config.audios[0],
    'audio_id2': config.audios[1],
    'document_id1': config.documents[0],
    'document_id2': config.documents[1],
    'video_id1': config.videos[0],
    'video_id2': config.videos[1]
    }


def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


async def process_start_cmd(message: Message):
    pass


@dp.callback_query(F.data.in_(
    [['text', 'audio', 'video', 'document', 'photo', 'voice']]))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    pass


@dp.message()
async def send_echo(message: Message):
    await message.answer(text='Say what?')


if __name__ == '__main__':
    dp.run_polling(bot)
