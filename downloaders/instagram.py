from telebot.types import Message
from loader import bot
import instaloader
from send_file import send_file
from handlers.main_heandlers.main_menu import return_to_main_menu, return_to_download_from_instagram


class Instagram:
    @classmethod
    def download_inst_photo(cls, message: Message):
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
    def download_inst_video(cls, message: Message):
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            return_to_main_menu(message)
        else:
            bot.send_message(chat_id, "Функция находится в разработке")
            return_to_main_menu(message)

    @classmethod
    def download_inst_audio(cls, message: Message):
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            return_to_main_menu(message)
        else:
            bot.send_message(chat_id, "Функция находится в разработке")
            return_to_main_menu(message)


