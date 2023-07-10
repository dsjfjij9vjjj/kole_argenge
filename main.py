import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message

from config import config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет!")


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Вот что я могу!')
    async def main():
        try:
            print('Bot Started')
            await dp.start_polling(bot)
        finally:
            await bot.session.close()



@dp.message(Text(text='1'))
async def easter_egg(message: Message):
    await message.answer('ХАХАХАХАХАХА')
    async def main():
        try:
            print('Bot Started')
            await dp.start_polling(bot)
        finally:
            await bot.session.close()


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

    async def main():
        try:
            print('Bot Started')
            await dp.start_polling(bot)
        finally:
            await bot.session.close()
