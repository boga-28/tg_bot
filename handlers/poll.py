from aiogram.types import (
    Message, PollAnswer, )
from aiogram import Router
import asyncio
from main import bot

router = Router()



async def survey(message: Message):
    questions = 'Насколько вы довольны функционалом нашего бота?'
    options = ['Очень доволен', 'Доволен', 'Нейтрально', 'Недоволен', 'Очень недоволен']
    await message.answer_poll(question=questions, options=options, is_anonymous=False)
    await asyncio.sleep(3)
    await survey_2(message)



@router.poll_answer()
async def poll_answer(poll_answer: PollAnswer):
    answer_ids = poll_answer.option_ids
    print(answer_ids)




async def survey_2(message: Message):
    questions2 = 'Какую часто вы пользуетесь нашим сервесом?'
    options2 = ['Ежедневно', "Пару раз в неделю", "Раз в неделю", "Несколько раз в месяц", "Реже"]
    await message.answer_poll(question=questions2, options=options2, is_anonymous=False)

#     questions2 = 'Какую часто вы пользуетесь нашим сервесом?'
#     options2 = ['Ежедневно', "Пару раз в неделю", "Раз в неделю", "Несколько раз в месяц", "Реже"]
#     await bot.send_message(question=questions2, options=options2, is_anonymous=False)
#     # poll_answer.
