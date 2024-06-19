from buttons import linkbuttons, form_button

from aiogram.types import (
    Message,)
from aiogram.filters import Command
from aiogram import Router
router = Router()



@router.message(Command('about'))
async def about(message: Message):
    text5 = "Бот 13.08.24"
    await message.answer(text=text5, reply_markup=linkbuttons)
    await message.delete()
