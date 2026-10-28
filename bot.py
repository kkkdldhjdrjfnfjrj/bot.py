
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ О боте")],
        [KeyboardButton(text="🆘 Помощь")],
        [KeyboardButton(text="🏠 Главное меню")],
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Добро пожаловать в моего бота!\n"
        "Выбери нужный раздел в меню ниже 👇",
        reply_markup=menu
    )


@dp.message(Command("help"))
@dp.message(lambda message: message.text == "🆘 Помощь")
async def help_message(message: Message):
    await message.answer(
        "🆘 Помощь\n\n"
        "/start — открыть меню\n"
        "/help — помощь"
    )


@dp.message(lambda message: message.text == "ℹ️ О боте")
async def about(message: Message):
    await message.answer(
        "🤖 Я твой Telegram-бот!\n\n"
        "Здесь будет информация о моём проекте."
    )


@dp.message(lambda message: message.text == "🏠 Главное меню")
async def home(message: Message):
    await message.answer(
        "🏠 Ты в главном меню.",
        reply_markup=menu
    )


@dp.message()
async def other_messages(message: Message):
    await message.answer(
        "Выбери один из разделов в меню 👇",
        reply_markup=menu
    )


async def main():
    if not TOKEN:
        raise RuntimeError("Не задана переменная BOT_TOKEN")

    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
