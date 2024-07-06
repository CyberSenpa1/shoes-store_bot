from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Главное меню
start_btn = [
    [
        InlineKeyboardButton(text='Каталог', callback_data='catalog_pressed'),
        InlineKeyboardButton(text='О нас', callback_data='about_pressed'),
    ]
         ]
kb_start = InlineKeyboardMarkup(inline_keyboard=start_btn)


# Профиль
btn_catalog = [
    [
        InlineKeyboardButton(text="Nike", callback_data="Nike"),
        InlineKeyboardButton(text="Adidas", callback_data="Adidas"),
        InlineKeyboardButton(text="Puma", callback_data="Puma"),
        InlineKeyboardButton(text="Vans", callback_data="Vans"),
        InlineKeyboardButton(text="Fila", callback_data="Fila"),
    ],
    
    [
        InlineKeyboardButton(text="Назад", callback_data="back_pressed")
    ]
]

kb_catalog = InlineKeyboardMarkup(inline_keyboard=btn_catalog)