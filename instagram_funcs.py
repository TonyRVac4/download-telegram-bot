from main import return_to_main_menu, return_to_download_from_youtube, bot, send_file


def download_inst_photo(message):
    chat_id = message.chat.id
    url = message.text

    if url == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        bot.send_message(chat_id, "Функция находится в разработке")
        return_to_main_menu(message)


def download_inst_video(message):
    chat_id = message.chat.id
    url = message.text

    if url == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        bot.send_message(chat_id, "Функция находится в разработке")
        return_to_main_menu(message)


def download_inst_audio(message):
    chat_id = message.chat.id
    url = message.text

    if url == "Вернуться в главное меню":
        return_to_main_menu(message)
    else:
        bot.send_message(chat_id, "Функция находится в разработке")
        return_to_main_menu(message)
