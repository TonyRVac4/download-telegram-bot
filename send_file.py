import os
from telebot.types import Message
from loader import bot
from pydrive.auth import GoogleAuth
from config_data.config import DATA_BASE_PATH


def send_file(message: Message, file_name, file_type):
    file_path = os.path.abspath(os.path.join(DATA_BASE_PATH, str(message.chat.id), file_name))
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
