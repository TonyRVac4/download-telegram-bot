import telebot
from telebot import types
from pytube import YouTube


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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Скачать из YouTube")
        button2 = types.KeyboardButton("Скачать из Instagram")
        markup.add(button1, button2)
        bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=markup)
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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Скачать из YouTube")
        button2 = types.KeyboardButton("Скачать из Instagram")
        markup.add(button1, button2)
        bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(chat_id, text="На такую комманду я не запрограммирован")


def download_youtube_video(message) -> None:
    chat_id = message.chat.id
    text = message.text

    if text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Скачать из YouTube")
        button2 = types.KeyboardButton("Скачать из Instagram")
        markup.add(button1, button2)
        bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        try:
            yt_obj = YouTube(message.text)
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
            filters.get_highest_resolution().download()
            bot.send_message(chat_id, text="Видео успешно загруженно")
        except Exception:
            bot.send_message(chat_id, text="Ошибка при скачивании!")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Скачать Видео")
            button2 = types.KeyboardButton("Скачать Аудио")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(button1, button2, back)
            bot.send_message(chat_id, text="Выберите вариант скачивания?", reply_markup=markup)
            bot.register_next_step_handler(message, download_from_youtube)


def download_youtube_audio(message) -> None:
    chat_id = message.chat.id
    text = message.text

    if text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Скачать из YouTube")
        button2 = types.KeyboardButton("Скачать из Instagram")
        markup.add(button1, button2)
        bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        try:
            yt_obj = YouTube(message.text)
            print(yt_obj.title)
            file_name = "{} - Audio.mp4".format(yt_obj.title)
            yt_obj.streams.get_audio_only().download(output_path='/Users/Tony/Downloads', filename=file_name)
            bot.send_message(chat_id, text="Аудио файл успешно загружен")
        except Exception:
            bot.send_message(chat_id, text="Ошибка при скачивании!")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Скачать Видео")
            button2 = types.KeyboardButton("Скачать Аудио")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(button1, button2, back)
            bot.send_message(chat_id, text="Выберите вариант скачивания?", reply_markup=markup)
            bot.register_next_step_handler(message, download_from_youtube)


bot.polling(none_stop=True)
