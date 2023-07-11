import asyncio
from email import message

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command, Text
from aiogram.types import Message, callback_query

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


@dp.message(F.content_type == ContentType.PHOTO)
async def echo(message: Message):
    await message.answer_photo(message.photo[0].file_id)


@dp.message(F.content_type == Content_type.STIKER)
async def echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)
@dp.message()
async def echo_all(message:Message):
    await message.send_copy(message.chat.id)
@dp.message(Text(text='Ответь'))
async def reply(message: Message):
    await message.reply('Ответил')