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
        InlineKeyboardButton(text="Nike", callback_data="nike_pressed"),
        InlineKeyboardButton(text="Adidas", callback_data="adidas_pressed"),
        InlineKeyboardButton(text="Puma", callback_data="puma_pressed"),
        InlineKeyboardButton(text="Vans", callback_data="vans_pressed"),
        InlineKeyboardButton(text="Fila", callback_data="fila_pressed"),
    ],
    
    [
        InlineKeyboardButton(text="Вернуться", callback_data="back_to_start")
    ]
]
kb_catalog = InlineKeyboardMarkup(inline_keyboard=btn_catalog)




btn_nike = [
    [
        InlineKeyboardButton(text="Вперед", callback_data="next_nike"), # кнопки которые переключают модель кед
        InlineKeyboardButton(text="Назад", callback_data="back_nike")
    ],
    [
        InlineKeyboardButton(text="Вернуться", callback_data="catalog_pressed")
    ]
] 
kb_nike = InlineKeyboardMarkup(inline_keyboard=btn_nike)




btn_adidas = [
    [
        InlineKeyboardButton(text="Вперед", callback_data="next_adidas"), # кнопки которые переключают модель кед
        InlineKeyboardButton(text="Назад", callback_data="back_adidas")
    ],
    [
        InlineKeyboardButton(text="Вернуться", callback_data="catalog_pressed")
    ]
]
kb_adidas = InlineKeyboardMarkup(inline_keyboard=btn_adidas)




btn_puma = [
    [
        InlineKeyboardButton(text="Вперед", callback_data="next_puma"), # кнопки которые переключают модель кед
        InlineKeyboardButton(text="Назад", callback_data="back_puma")
    ],
    [
        InlineKeyboardButton(text="Вернуться", callback_data="catalog_pressed")
    ]
] 
kb_puma = InlineKeyboardMarkup(inline_keyboard=btn_puma)




btn_vans = [
    [
        InlineKeyboardButton(text="Вперед", callback_data="next_vans"), # кнопки которые переключают модель кед
        InlineKeyboardButton(text="Назад", callback_data="back_vans")
    ],
    [
        InlineKeyboardButton(text="Вернуться", callback_data="catalog_pressed")
    ]
] 
kb_vans = InlineKeyboardMarkup(inline_keyboard=btn_vans)



btn_fila = [
    [
        InlineKeyboardButton(text="Вперед", callback_data="next_fila"), # кнопки которые переключают модель кед
        InlineKeyboardButton(text="Назад", callback_data="back_fila")
    ],
    [
        InlineKeyboardButton(text="Вернуться", callback_data="catalog_pressed")
    ]
] 
kb_fila = InlineKeyboardMarkup(inline_keyboard=btn_fila)