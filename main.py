import telebot
from telebot import types


TOKEN = "5416303529:AAHa8me8WANsWCKs2FLf45VC-3o47sATNto"
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Скачать из YouTube")
    button2 = types.KeyboardButton("Скачать из Instagram")
    markup.add(button1, button2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Это бот для скачивания видео и аудио".format(
                         message.from_user
                     ),
                     reply_markup=markup
                     )


bot.polling(none_stop=True)
