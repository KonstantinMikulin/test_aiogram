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


@dp.message(F.text.lower().startswith('найди числа'),
            NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')


@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')


if __name__ == '__main__':
    dp.run_polling(bot)
