import asyncio
from aiogram import Bot, Dispatcher
from os import getenv
from handlers import users
import logging


logging.basicConfig(level=logging.INFO)


# Запуск бота
async def main():
    bot = Bot(token=getenv("TOKEN"))
    dp = Dispatcher()

    dp.include_routers(users.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



    

if __name__ == "__main__":
    asyncio.run(main())