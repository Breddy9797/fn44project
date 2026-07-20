import os
import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart, Command
from aiogram.webhook.aiohttp_server import setup_application, SimpleRequestHandler
from aiohttp import web

from database import connection, jadval_yaratish,malumot
from load import BOT_TOKEN
import logging

PORT = int(os.getenv("PORT"))

logging.basicConfig(level=logging.INFO)
TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
# Masalan: https://mening-botim.onrender.com
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"



@dp.message(CommandStart())
async def echo(message: types.Message):
    ismi=message.from_user.full_name
    telegram_id=message.from_user.id
    malumot(ismi,telegram_id)
    await message.answer("sizning malumotlaringiz saqlandi !")

async def on_startup(bot:Bot):
    await bot.set_webhook(WEBHOOK_URL)

async def main():
    dp.startup.register(on_startup)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    jadval_yaratish()

    setup_application(app,dp,port=PORT)
    await web._run_app(app,host="0.0.0.0",port=PORT)


if __name__ == '__main__':
    asyncio.run(main())