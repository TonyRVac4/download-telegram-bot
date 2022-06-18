import os
import telebot
from telebot import types
from youtube_funcs import download_youtube_video, download_youtube_audio


TOKEN = "5416303529:AAHa8me8WANsWCKs2FLf45VC-3o47sATNto"
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать из YouTube")
    button2 = types.KeyboardButton("Скачать из Instagram")
    markup.add(button1, button2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Это бот для скачивания видео и аудио".format(
                         message.from_user
                     ),
                     reply_markup=markup
                     )


@bot.message_handler(content_types=['text'])
def main_menu(message):
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
        bot.register_next_step_handler(message, download_youtube_video)
    elif text == "Скачать Аудио":
        bot.send_message(chat_id, text="Введите URL:")
        bot.register_next_step_handler(message, download_youtube_audio)
    elif text == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        bot.send_message(chat_id, text="На такую комманду я не запрограммирован")


def return_to_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать из YouTube")
    button2 = types.KeyboardButton("Скачать из Instagram")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


def return_to_download_from_youtube(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать Видео")
    button2 = types.KeyboardButton("Скачать Аудио")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(button1, button2, back)
    bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?", reply_markup=markup)
    bot.register_next_step_handler(message, download_from_youtube)


def send_file(message, file_name, file_type):
    file_path = os.path.abspath(os.path.join("/Users/Tony/PycharmProjects/download-telegram-bot/files/", file_name))
    if file_type == "Y-video":
        with open(file_path, 'rb') as file:
            bot.send_video(message.chat.id, file)  # не отправляет большие файлы
    elif file_type == "Y-audio":
        with open(file_path, 'rb') as file:
            bot.send_audio(message.chat.id, file)
    os.remove(file_path)


bot.polling(none_stop=True)
