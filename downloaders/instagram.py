from telebot.types import Message
from loader import bot
import instaloader
from send_file import send_file
from keyboards.reply.menu import menu, download_from_instagram_menu


class Instagram:
    @classmethod
    def download_inst_photo(cls, message: Message):
        chat_id = message.chat.id
        url = message.text
        if url == "Вернуться в главное меню":
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())
        else:
            try:
                bot.send_message(chat_id, 'Начинаем загрузку фото...')

                file_name = "{} - photo.MP4".format("").replace("/", "")
                output_path = '/Users/Tony/PycharmProjects/download-telegram-bot/files'

                bot.send_message(chat_id, text="Фото успешно загруженно")
                send_file(message, file_name, file_type="I-photo")
            except Exception:
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?",
                                 reply_markup=download_from_instagram_menu()
                                 )

    @classmethod
    def download_inst_video(cls, message: Message):
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())
        else:
            try:
                bot.send_message(chat_id, "Функция находится в разработке")
            except Exception:
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())

    @classmethod
    def download_inst_audio(cls, message: Message):
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())
        else:
            try:
                bot.send_message(chat_id, "Функция находится в разработке")
            except Exception:
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())

