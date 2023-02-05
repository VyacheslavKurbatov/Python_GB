from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_new = ReplyKeyboardMarkup(resize_keyboard=True)
kb_stop = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton(text='/start')
btn_new_game = KeyboardButton(text='/new_game')
btn_stop_game = KeyboardButton(text='/stop_game')
btn_level = KeyboardButton(text='/level')

kb_new.add(btn_start, btn_new_game, btn_level)
kb_stop.add(btn_stop_game, btn_level)
