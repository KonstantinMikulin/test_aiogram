from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message

import config

BOT_TOKEN = config.TOKEN

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer('Hello hello!')


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []

        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))

            if numbers:
                return {'numbers': numbers}

        return False


@dp.message(F.text.lower().startwith('найди числа'), NumbersInMessage)
async def process_if_numbers(message: Message, numbers: list[int]) -> None:



if __name__ == '__main__':
    dp.run_polling(bot)
