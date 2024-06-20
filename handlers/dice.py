from aiogram.types import (
    Message)
from aiogram import Router

router = Router()


async def dice(message: Message):
    dice = await message.answer_dice()
    print(dice.dice.value)
