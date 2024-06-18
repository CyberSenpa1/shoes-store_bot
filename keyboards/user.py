from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# Кнопки

# Главное меню
kb_0 = [
    [KeyboardButton(text="Профиль")],
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="О нас")]
]
menu_kb = ReplyKeyboardMarkup(keyboard = kb_0)



# Профиль
kb_1 = [
    [KeyboardButton(text="имя")],
    [KeyboardButton(text="заказы")],
    [KeyboardButton(text="баланс")]
]
profile_kb = InlineKeyboardMarkup(inline_keyboard = kb_1)

# Инлайн кнопки