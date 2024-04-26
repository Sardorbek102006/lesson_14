from telebot import types


def generate_main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="Share contact", request_contact=True)
    keyboard.row(btn)
    return keyboard

def laptop_manu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="tovarlar")
    keyboard.row(btn)
    return keyboard


def buy_laptop():
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Batafsil", url='https://www.youtube.com/?hl=ru')
    keyboard.row(btn)
    return keyboard
