from telebot.types import Message
from telebot import types
from loader import bot
from downloaders.youtube import YouTube
from downloaders.instagram import Instagram


@bot.message_handler(content_types=['text'])
def main_menu(message: Message):
    text = message.text
    chat_id = message.chat.id

    if text == "Скачать из YouTube":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Скачать Видео")
        button2 = types.KeyboardButton("Скачать Аудио")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, back)
        bot.send_message(chat_id, text="Выберите вариант скачивания?", reply_markup=markup)
        bot.register_next_step_handler(message, download_from_youtube)
    elif text == "Скачать из Instagram":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Скачать Фото")
        button2 = types.KeyboardButton("Скачать Аудио")
        button3 = types.KeyboardButton("Скачать Видео")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, back)
        bot.send_message(chat_id, text="Выберите вариант скачивания?", reply_markup=markup)
        bot.register_next_step_handler(message, download_from_instagram)
    elif text == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        bot.send_message(chat_id, text="На такую комманду я не запрограммирован")


@bot.message_handler(content_types=['text'])
def download_from_youtube(message):
    text = message.text
    chat_id = message.chat.id

    if text == "Скачать Видео":
        bot.send_message(chat_id, text="Введите URL:")
        bot.register_next_step_handler(message, YouTube.download_youtube_video)
    elif text == "Скачать Аудио":
        bot.send_message(chat_id, text="Введите URL:")
        bot.register_next_step_handler(message, YouTube.download_youtube_audio)
    elif text == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        bot.send_message(chat_id, text="На такую комманду я не запрограммирован")


@bot.message_handler(content_types=['text'])
def download_from_instagram(message):
    text = message.text
    chat_id = message.chat.id

    if text == "Скачать Фото":
        bot.send_message(chat_id, text="Введите URL:")
        bot.register_next_step_handler(message, Instagram.download_inst_photo)
    elif text == "Скачать Аудио":
        bot.send_message(chat_id, text="Введите URL:")
        bot.register_next_step_handler(message, Instagram.download_inst_audio)
    elif text == "Скачать Видео":
        bot.send_message(chat_id, text="Введите URL:")
        bot.register_next_step_handler(message, Instagram.download_inst_video)
    elif text == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        bot.send_message(chat_id, text="На такую комманду я не запрограммирован")


def return_to_main_menu(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать из YouTube")
    button2 = types.KeyboardButton("Скачать из Instagram")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


def return_to_download_from_youtube(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать Видео")
    button2 = types.KeyboardButton("Скачать Аудио")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(button1, button2, back)
    bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?", reply_markup=markup)
    bot.register_next_step_handler(message, download_from_youtube)


def return_to_download_from_instagram(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать Фото")
    button2 = types.KeyboardButton("Скачать Аудио")
    button3 = types.KeyboardButton("Скачать Видео")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(button1, button2, button3, back)
    bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?", reply_markup=markup)
    bot.register_next_step_handler(message, download_from_instagram)