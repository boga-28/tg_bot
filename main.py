import asyncio
from handlers import help, start, about, form, poll
from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from system.antispam import AntiFloodMiddleware
from config_reader import config
from data import start_db

bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher()


async def main():
    await start_db()
    dp.message.middleware(AntiFloodMiddleware())
    dp.include_routers(
        start.router,
        form.router,
        help.router,
        about.router,
        poll.router
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
