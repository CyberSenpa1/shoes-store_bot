from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup

router = Router()

from keyboards.user_kb import kb_start, profile_kb # Кнопки

# Хэндлер старта
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет!\nЭто магазин обуви",
        reply_markup=kb_start
    )    


# Хэндлер профиля
#@router.message(F.text == "Каталог")
#async def profile(message: Message):
#    await message.answer(
#        f"Каталог",
#        reply_markup = profile_kb
#    )