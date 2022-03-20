from aiogram import Bot, Dispatcher, executor, types
import logging

logging.basicConfig(level=logging.INFO)

API_TOKEN = '5011258514:AAG28ZT8tentMEBuY1M4qaAmizXIqLiSlQA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer(f"Xush kelibshiz! {message.from_user.full_name}")

@dp.message_handler()
async def text_handler(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dp, skip_updates=True)