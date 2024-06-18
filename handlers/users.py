from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()

from keyboards.user import menu_kb, profile_kb # Кнопки

# Хэндлер старта
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет!\nЭто магазин обуви", 
        reply_markup = menu_kb
    )    


# Хэндлер профиля
@router.message(F.text == "Профиль")
async def profile(message: Message):
    await message.answer(
        f"{message.from_user.id}, Ваш профиль:",
        reply_markup = profile_kb
    )