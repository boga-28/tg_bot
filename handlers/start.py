from buttons import form_button
from aiogram.types import (
    Message)
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.fsm.context import FSMContext
from system.states import Form
from apply import get_photo

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Form.wait)
    photo = await get_photo('кубики')
    await message.answer_photo(
        photo=photo)
    text = 'Здравствуйте! Мы приветствуем вас в нашем боте, для начала вам необходимо заполнить анкету! Нажмите на кнопку ниже чтобы начать 👇'
    await message.answer(text=text, reply_markup=form_button)
    await message.delete()
