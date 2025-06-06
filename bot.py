import asyncio
from aiogram import Bot, Dispatcher
from router import router

API_TOKEN_BOT = '7790976582:AAH7vG0hbwzO1_7OYDfRvRJxNC5gyRVRhv8'
bot = Bot(token=API_TOKEN_BOT)
dp = Dispatcher()

dp.include_router(router)

async def main():
    print("Bot ishladi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())