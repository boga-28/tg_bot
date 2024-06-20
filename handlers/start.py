from buttons import form_button
from aiogram.types import (
    Message)
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.fsm.context import FSMContext
from system.states import Form, Menu
from apply import get_photo
from data import check_profile

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    is_exist = await check_profile(message.from_user.id)
    if not is_exist:
        await state.set_state(Form.wait)
        photo = await get_photo('лого')
        await message.answer_photo(
            photo=photo)
        text = 'Здравствуйте! Мы приветствуем вас в нашем боте, для начала вам необходимо заполнить анкету. Нажмите на кнопку ниже чтобы начать 👇'
        await message.answer(text=text, reply_markup=form_button)
        await message.delete()
    else:
        text = 'Здравствуйте! Мы приветствуем вас в нашем боте, для начала вам необходимо заполнить анкету. Нажмите на кнопку ниже чтобы начать 👇'

        await state.set_state(Menu.to_menu)
        await message.answer(text=text, reply_markup=form_button)
