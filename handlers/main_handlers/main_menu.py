from telebot.types import Message
from loader import bot
from downloaders.youtube import Youtube
from downloaders.instagram import Instagram
from keyboards.reply.menu import menu, download_from_youtube_menu, download_from_instagram_menu
from handlers.main_handlers.history import history


@bot.message_handler(content_types=['text'])
def main_menu_handler(message: Message):
    text = message.text
    chat_id = message.chat.id

    if text == "Скачать из YouTube":
        bot.send_message(chat_id, text="Выберите вариант скачивания?", reply_markup=download_from_youtube_menu())
        bot.register_next_step_handler(message, download_from_youtube)
    elif text == "Скачать из Instagram":
        bot.send_message(chat_id, text="Выберите вариант скачивания?", reply_markup=download_from_instagram_menu())
        bot.register_next_step_handler(message, download_from_instagram)
    elif text == "Вернуться в главное меню":
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())
    elif text == "История скачиваний":
        bot.register_next_step_handler(message, history)
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
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())


@bot.message_handler(content_types=['text'])
def download_from_instagram(message):
    text = message.text
    chat_id = message.chat.id
    bot.send_message(chat_id, "Функция находится в разработке")
    bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=menu())
    # if text == "Скачать Фото":
    #     bot.send_message(chat_id, text="Введите URL:")
    #     bot.register_next_step_handler(message, Instagram.download_inst_photo)
    # elif text == "Скачать Аудио":
    #     bot.send_message(chat_id, text="Введите URL:")
    #     bot.register_next_step_handler(message, Instagram.download_inst_audio)
    # elif text == "Скачать Видео":
    #     bot.send_message(chat_id, text="Введите URL:")
    #     bot.register_next_step_handler(message, Instagram.download_inst_video)
    # elif text == "Вернуться в главное меню":
    #     bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=main_menu)
