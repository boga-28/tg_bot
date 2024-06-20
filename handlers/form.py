from buttons import menu_options, linkbuttons
from aiogram.types import (
    Message,
    ReplyKeyboardRemove)
from aiogram import Router
from aiogram.fsm.context import FSMContext
from system.states import Form, Menu
from re import fullmatch
from buttons import menubutton, linkbuttons_2
from handlers.poll import survey
from data import create_profile, edit_profile
from handlers.dice import dice


router = Router()


@router.message(Form.wait)
async def waiting(message: Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)
    if message.text.lower() == 'перейти к анкете':
        await state.set_state(Form.name)
        text = 'Введите ваше имя:'
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    else:
        text = 'Я вас не понял, нажмите на кнопку ниже чтобы начать заполнение анкеты.'
        await message.answer(text=text)


@router.message(Form.name)
async def name(message: Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name=message.text)
        await state.set_state(Form.age)
        text = 'Отлично, введите ваш возраст:'
        await message.answer(text=text)
    else:
        text = 'Введите корректное имя.'
        await message.answer(text=text)


@router.message(Form.age)
async def age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.set_state(Form.email)
        await state.update_data(age=message.text)
        text = 'Отлично, введите ваш email:'
        await message.answer(text=text)
    else:
        text = 'Введите корректный возраст.'
        await message.answer(text=text)


@router.message(Form.email)
async def email(message: Message, state: FSMContext):
    if fullmatch('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+)', message.text):
        await state.set_state(Menu.to_menu)
        await state.update_data(email=message.text)
        text = 'Замечательно. Ваша анкета сохранена. Нажмите на кнопку ниже и перейдите в меню👇'
        data_dict = await state.get_data()
        await create_profile(data_dict['id'])
        await edit_profile(data_dict['id'], data_dict['name'], data_dict['age'], data_dict['email'])
        await message.answer(text=text, reply_markup=menubutton)

    else:
        text = 'Введите корректный email.'
        await message.answer(text=text)

data = []


@router.message(Menu.to_menu)
async def reply(message: Message):
    text = '<i>Привет! Я чат-бот и готов помочь вам</i>. Вот список доступных функций:' \
           '\n\n1. Помощь - показать список доступных команд\n2. О боте - узнать больше о чат-боте' \
           '\n3. Услуги - узнать о доступных услугах\n4. Контакты - связаться с нами' \
           '\n\nЧтобы выбрать нужную функцию, просто укажите соответствующий номер. Спасибо, что обратились! '
    if message.text.lower() == 'меню' or message.text.lower() == '/menu':
        await message.answer(text=text, reply_markup=menu_options, parse_mode='html')
    elif message.text == 'Помощь 🆘':
        await message.answer(text='Если у вас возникли какие либо проблемы с ботом вы можете обратится в поддержку!',
                             reply_markup=linkbuttons_2)
    elif message.text == 'О боте ℹ️':
        await message.answer(text='Добро пожаловать в раздел О боте! Здесь вы найдете информацию о создателях этого'\
                                                                    'удивительного бота, его функциях и возможностях.'\
                                                                    'Мы всегда готовы помочь вам и ответить на' \
                                                                    ' любые ваши вопросы. Спасибо, что выбрали' \
                                                                    ' нашего бота')
    elif message.text == 'Услуги 👑':
        text = 'Наш бот предлагает широкий спектр услуг для вашего удобства:\n\n'\
               '1. Консультации и помощь в решении задач.\n' \
               '2. Поиск информации и обновлений по вашему запросу.\n'\
               '3. Помощь в планировании задач и организации времени.\n'\
               '4. Интерактивные игры и развлечения для разнообразия.\n'
        await message.answer(text=text)
    elif message.text == 'Локация 📍':
        await message.answer_location(latitude=55.818748210701465, longitude=49.1208645081678)
    elif message.text == 'Пройти опрос ❓':
        await survey(message)
    elif message.text == 'Бросить кубик 🎲':
        await dice(message)
    elif message.text == '/help':
        text = '/start - запустить бота\n/help - помощь\n/about - информация о боте\n/menu - вывод меню '
        await message.answer(text=text)
        await message.delete()
    elif message.text == '/about':
        text5 = "Бот 13.08.24"
        await message.answer(text=text5, reply_markup=linkbuttons)
        await message.delete()
    else:
        await message.answer('Извините я вас не понимаю, попробуйте вызвать другую функцию)')
