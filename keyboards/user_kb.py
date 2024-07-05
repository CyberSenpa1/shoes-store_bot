from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


# Главное меню
start_btn = [
    [
        InlineKeyboardButton(text='Каталог', callback_data="catalog"),
        InlineKeyboardButton(text='О нас', callback_data='about', url="https://t.me/CyberSenpa1"),
    ]
         ]
kb_start = InlineKeyboardMarkup(inline_keyboard=start_btn)


# Профиль
kb_1 = [
    [KeyboardButton(text="имя")],
    [KeyboardButton(text="заказы")],
    [KeyboardButton(text="баланс")]
]

profile_kb = ReplyKeyboardMarkup(keyboard = kb_1)
