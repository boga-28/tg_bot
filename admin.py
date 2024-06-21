from main import bot


async def admin(text):
    await bot.send_message(chat_id=850353673, text=text)
