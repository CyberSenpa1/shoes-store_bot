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


@router.callback_query(F.data.in_(['catalog_pressed']))
async def nike_catalog(callback: CallbackQuery):
    await callback.message.edit_text(text="Наша коллекция обуви", reply_markup=kb_catalog)

@router.callback_query(F.data.in_(['back_to_start']))
async def back_press(callback: CallbackQuery):
    await callback.message.edit_text(text="И снова вы в главном меню", reply_markup=kb_start)

@router.callback_query(F.data.in_(['nike_pressed']))
async def back_press(callback: CallbackQuery):
    await callback.message.edit_text(text="Nike", reply_markup=kb_nike)

@router.callback_query(F.data.in_(['adidas_pressed']))
async def back_press(callback: CallbackQuery):
    await callback.message.edit_text(text="Adidas", reply_markup=kb_adidas)

@router.callback_query(F.data.in_(['puma_pressed']))
async def back_press(callback: CallbackQuery):
    await callback.message.edit_text(text="Puma", reply_markup=kb_puma)

@router.callback_query(F.data.in_(['vans_pressed']))
async def back_press(callback: CallbackQuery):
    await callback.message.edit_text(text="Vans", reply_markup=kb_vans)

@router.callback_query(F.data.in_(['fila_pressed']))
async def back_press(callback: CallbackQuery):
    await callback.message.edit_text(text="Fila", reply_markup=kb_fila)





