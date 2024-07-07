from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup
from keyboards.user_kb import kb_start, kb_catalog, kb_nike, kb_fila, kb_vans, kb_puma, kb_adidas  # Кнопки
from aiogram.types import CallbackQuery


router = Router()

# Хэндлер старта
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет!\nЭто магазин обуви",
        reply_markup=kb_start
    )    




