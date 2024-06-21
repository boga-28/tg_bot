from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton)


menubutton = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='меню')]
        ]
    )


linkbuttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Переход', url='https://www.youtube.com/watch?v=0tcyiwF2Yms')],
            [InlineKeyboardButton(text='Телеграм автора', url='https://www.youtube.com/watch?v=UiCHnwOndiM')],
            [InlineKeyboardButton(text='Ссылка на инстаграм', url='https://www.youtube.com/watch?v=PMhOgVvZzGo')]
        ]
    )


linkbuttons_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Поддержка 🖥', url='https://t.me/bogdan_mav')]
        ]
)


menu_options = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Помощь 🆘',), KeyboardButton(text='О боте ℹ️')],
                [KeyboardButton(text='Услуги 👑',), KeyboardButton(text='Локация 📍',)],
                [KeyboardButton(text='Пройти опрос ❓',), KeyboardButton(text='Бросить кубик 🎲',)]
            ]
        )

form_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='перейти к анкете')]
    ]
)
