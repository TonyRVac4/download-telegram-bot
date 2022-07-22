from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Скачать из YouTube")
    button2 = KeyboardButton("Скачать из Instagram")
    markup.add(button1, button2)
    return markup
