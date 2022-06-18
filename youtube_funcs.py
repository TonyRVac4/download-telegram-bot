from main import return_to_main_menu, return_to_download_from_youtube, bot, send_file
from pytube import YouTube


def download_youtube_video(message) -> None:
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


def download_youtube_audio(message) -> None:
    chat_id = message.chat.id
    text = message.text

    if text == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        try:
            yt_obj = YouTube(message.text)
            bot.send_message(chat_id, text="Началась загрузка...")
            file_name = "{} - Audio.MP4".format(yt_obj.title)
            yt_obj.streams.get_audio_only().download(output_path='/Users/Tony/PycharmProjects/download-telegram-bot/files',
                                                     filename=file_name)
            bot.send_message(chat_id, text="Аудио файл успешно загружен")
            send_file(message, file_name, file_type="Y-audio")
        except Exception:
            bot.send_message(chat_id, text="Ошибка при скачивании!")
        finally:
            return_to_download_from_youtube(message)

