from aiogram import Bot, Dispatcher
import os

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
