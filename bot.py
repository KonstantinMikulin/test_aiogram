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