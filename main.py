import os
import telebot
from telebot import types
from pytube import YouTube
import instaloader

TOKEN = "5416303529:AAHa8me8WANsWCKs2FLf45VC-3o47sATNto"
bot = telebot.TeleBot(token=TOKEN)


class Youtube:
    @classmethod
    def download_youtube_video(cls, message) -> None:
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            return_to_main_menu(message)
        else:
            try:
                yt_obj = YouTube(message.text)
                bot.send_message(chat_id, 'Начинаем загрузку видео...')
                filters = yt_obj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                file_name = "{} - Video.MP4".format(yt_obj.title)
                filters.download(output_path='/Users/Tony/PycharmProjects/download-telegram-bot/files',
                                 filename=file_name)
                bot.send_message(chat_id, text="Видео успешно загруженно")
                send_file(message, file_name, file_type="Y-video")
            except Exception:
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                return_to_download_from_youtube(message)

    @classmethod
    def download_youtube_audio(cls, message) -> None:
        chat_id = message.chat.id
        text = message.text

        if text == "Вернуться в главное меню":
            return_to_main_menu(message)
        else:
            try:
                yt_obj = YouTube(message.text)
                bot.send_message(chat_id, text="Началась загрузка...")
                file_name = "{} - Audio.MP4".format(yt_obj.title)
                yt_obj.streams.get_audio_only().download(
                    output_path='/Users/Tony/PycharmProjects/download-telegram-bot/files',
                    filename=file_name)
                bot.send_message(chat_id, text="Аудио файл успешно загружен")
                send_file(message, file_name, file_type="Y-audio")
            except Exception:
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                return_to_download_from_youtube(message)


class Instagram:
    @classmethod
    def download_inst_photo(cls, message):
        chat_id = message.chat.id
        url = message.text
        if url == "Вернуться в главное меню":
            return_to_main_menu(message)
        else:
            try:
                bot.send_message(chat_id, 'Начинаем загрузку фото...')

                file_name = "{} - photo.MP4".format(1)
                output_path = '/Users/Tony/PycharmProjects/download-telegram-bot/files'

                bot.send_message(chat_id, text="Фото успешно загруженно")
                send_file(message, file_name, file_type="I-photo")
            except Exception:
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                return_to_download_from_instagram(message)

    @classmethod
    def download_inst_video(cls, message):
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            return_to_main_menu(message)
        else:
            bot.send_message(chat_id, "Функция находится в разработке")
            return_to_main_menu(message)

    @classmethod
    def download_inst_audio(cls, message):
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            return_to_main_menu(message)
        else:
            bot.send_message(chat_id, "Функция находится в разработке")
            return_to_main_menu(message)


# ----------Основной код----------

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
        bot.register_next_step_handler(message, Youtube.download_youtube_video)
    elif text == "Скачать Аудио":
        bot.send_message(chat_id, text="Введите URL:")
        bot.register_next_step_handler(message, Youtube.download_youtube_audio)
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


def return_to_download_from_instagram(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать Фото")
    button2 = types.KeyboardButton("Скачать Аудио")
    button3 = types.KeyboardButton("Скачать Видео")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(button1, button2, button3, back)
    bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?", reply_markup=markup)
    bot.register_next_step_handler(message, download_from_instagram)


def send_file(message, file_name, file_type):
    file_path = os.path.abspath(os.path.join("/Users/Tony/PycharmProjects/download-telegram-bot/files/", file_name))
    if file_type == "Y-video":
        with open(file_path, 'rb') as file:
            bot.send_video(message.chat.id, file)  # не отправляет большие файлы
    elif file_type == "Y-audio":
        with open(file_path, 'rb') as file:
            bot.send_audio(message.chat.id, file)
    elif file_type == "I-photo":
        pass
    elif file_type == "I-audio":
        pass
    elif file_type == "I-video":
        pass
    os.remove(file_path)


bot.polling(none_stop=True)
