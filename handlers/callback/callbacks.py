from aiogram import F
from aiogram.types import CallbackQuery


@dp.callback_query(F.data == '')
async def process_button_1_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Nike:',
        reply_markup=callback.message.reply_markup
    )
