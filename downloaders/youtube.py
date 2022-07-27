from telebot.types import Message
from loader import bot
from pytube import YouTube
from send_file import send_file
from keyboards.reply.menu import menu, download_from_youtube_menu
from logs.logers import downloader_loger


class Youtube:
    @classmethod
    def download_youtube_video(cls, message: Message) -> None:
        chat_id = message.chat.id
        url = message.text

        if url == "Вернуться в главное меню":
            bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=menu())
        else:
            try:
                yt_obj = YouTube(url)
                bot.send_message(chat_id, 'Начинаем загрузку видео...')
                filters = yt_obj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                file_name = "{} - Video.MP4".format(yt_obj.title).replace("/", "")
                filters.download(output_path='/Users/Tony/PycharmProjects/download-telegram-bot/database/files',
                                 filename=file_name)
                bot.send_message(chat_id, text="Видео успешно загруженно")
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

        if url == "Вернуться в главное меню":
            bot.send_message(chat_id, text="Вы вернулись в главное меню", reply_markup=menu())
        else:
            try:
                yt_obj = YouTube(url)
                bot.send_message(chat_id, text="Началась загрузка...")
                file_name = "{} - Audio.MP4".format(yt_obj.title).replace("/", "")
                yt_obj.streams.get_audio_only().download(
                    output_path='/Users/Tony/PycharmProjects/download-telegram-bot/database/files',
                    filename=file_name)
                bot.send_message(chat_id, text="Аудио файл успешно загружен")
                send_file(message, file_name, file_type="Y-audio")
            except Exception as exp:
                downloader_loger(exception=exp, text=url)
                bot.send_message(chat_id, text="Ошибка при скачивании!")
            finally:
                bot.send_message(message.chat.id, text="Хотите скачать что-нибудь ещё?",
                                 reply_markup=menu()
                                 )
