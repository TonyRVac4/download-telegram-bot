from telebot.types import Message
from loader import bot
from keyboards.reply.menu import menu


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    print("start")
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Это бот для скачивания видео и аудио".format(message.from_user),
                     reply_markup=menu())