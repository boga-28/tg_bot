from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    wait = State()
    name = State()
    age = State()
    email = State()


class Menu(StatesGroup):
    to_menu = State()
    menu = State()
    point_1 = State()
    point_2 = State()
    point_3 = State()
    connection = State()


class Poll(StatesGroup):
    poll = State()
