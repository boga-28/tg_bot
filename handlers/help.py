from aiogram.types import (
    Message,)
from aiogram.filters import Command
from aiogram import Router
router = Router()


@router.message(Command('help'))
async def help(message: Message):
    text = '/start - запустить бота\n/help - помощь\n/about - информация о боте\n/menu - вывод меню '
    await message.answer(text=text)
    await message.delete()