from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Скачать из YouTube")
    button2 = KeyboardButton("Скачать из Instagram")
    markup.add(button1, button2)
    return markup


def download_from_youtube_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Скачать Видео",)
    button2 = KeyboardButton("Скачать Аудио")
    back = KeyboardButton("Вернуться в главное меню")
    markup.add(button1, button2, back)
    return markup


def download_from_instagram_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Скачать Фото")
    button2 = KeyboardButton("Скачать Аудио")
    button3 = KeyboardButton("Скачать Видео")
    back = KeyboardButton("Вернуться в главное меню")
    markup.add(button1, button2, button3, back)
    return markup
