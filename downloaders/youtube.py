from telebot.types import Message
from loader import bot
from pytube import YouTube
from send_file import send_file
from keyboards.reply.menu import menu, download_from_youtube_menu
from logs.logers import downloader_loger
from config_data.config import DATA_BASE_PATH
import os


class Youtube:
    @classmethod
    def download_youtube_video(cls, message: Message) -> None:
        chat_id = message.chat.id
        url = message.text
        user_id = message.from_user.id

        if url == "Вернуться в главное меню":
            bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=menu())
        else:
            try:
                yt_obj = YouTube(url)
                filters = yt_obj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                file_name = "{} - Video.MP4".format(yt_obj.title).replace("/", "")
                data_base_path = os.path.join(DATA_BASE_PATH, str(user_id))
                if str(user_id) not in os.listdir(DATA_BASE_PATH):
                    os.mkdir(data_base_path)
                if not os.path.exists(os.path.join(data_base_path, file_name)):
                    bot.send_message(chat_id, 'Начинаем загрузку видео...')
                    filters.download(output_path=data_base_path,
                                     filename=file_name)
                    bot.send_message(chat_id, text="Видео успешно загруженно")
                else:
                    bot.send_message(chat_id, text="Данный файл найден в истории загрузок")
                send_file(message, file_name, file_type="Y-video")
            except Exception as exp:
                downloader_loger(exception=exp, text=url)
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?",
                                 reply_markup=menu()
                                 )

    @classmethod
    def download_youtube_audio(cls, message: Message) -> None:
        chat_id = message.chat.id
        url = message.text
        user_id = message.from_user.id
        if url == "Вернуться в главное меню":
            bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=menu())
        else:
            try:
                yt_obj = YouTube(url)
                file_name = "{} - Audio.MP4".format(yt_obj.title).replace("/", "")
                data_base_path = os.path.join(DATA_BASE_PATH, str(user_id))
                if str(user_id) not in os.listdir(DATA_BASE_PATH):
                    os.mkdir(data_base_path)
                if not os.path.exists(os.path.join(data_base_path, file_name)):
                    bot.send_message(chat_id, text="Начинаем загрузку аудио...")
                    yt_obj.streams.get_audio_only().download(
                        output_path=data_base_path,
                        filename=file_name)
                    bot.send_message(chat_id, text="Аудио файл успешно загружен")
                else:
                    bot.send_message(chat_id, text="Данный файл найден в истории загрузок")

                send_file(message, file_name, file_type="Y-audio")
            except Exception as exp:
                downloader_loger(exception=exp, text=url)
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?",
                                 reply_markup=menu()
                                 )
