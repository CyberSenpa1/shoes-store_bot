from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup
from keyboards.user_kb import kb_start, kb_catalog  # Кнопки
from aiogram.types import CallbackQuery


router = Router()

# Хэндлер старта
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет!\nЭто магазин обуви",
        reply_markup=kb_start
    )    


@router.callback_query(F.data.in_(['catalog_pressed']))
async def nike_catalog(callback: CallbackQuery):
    await callback.message.edit_text(text="Коллекция nike", reply_markup=kb_catalog)

@router.callback_query(F.data.in_(['back_pressed']))
async def back_press(callback: CallbackQuery):
    await callback.message.edit_text(text="И снова вы в главном меню", reply_markup=kb_start)