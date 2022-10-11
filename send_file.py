import os
from telebot.types import Message
from loader import bot
from pydrive.auth import GoogleAuth

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database/files")


def send_file(message: Message, file_name, file_type):
    file_path = os.path.join(BASE_DIR, file_name)
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
