from telebot.types import Message
from loader import bot
from handlers.main_heandlers.main_menu import main_menu
from keyboards.reply.main_menu import main_menu


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Это бот для скачивания видео и аудио".format(message.from_user),
                     reply_markup=main_menu())
    bot.register_next_step_handler(message, main_menu)
