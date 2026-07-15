import os
import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart, Command
from database import connection, jadval_yaratish,malumot
from load import BOT_TOKEN
TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def echo(message: types.Message):
    ismi=message.from_user.full_name
    telegram_id=message.from_user.id
    malumot(ismi,telegram_id)
    await message.answer("sizning malumotlaringiz saqlandi !")

async def main():
    jadval_yaratish()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())