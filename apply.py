import sqlite3 as sq

db = sq.connect('persons.db')
cur = db.cursor()

# name = 'черепаха'
# id = 'AgACAgIAAxkBAAIGCmZtfI_GWalwjIUAAfxnA7MePXkDAQACK98xG8tpcEu-nVjRiLqh9gEAAwIAA20AAzUE'


async def get_photo(name):
    return cur.execute(f"SELECT id from images where name == '{name}'").fetchone()[0]