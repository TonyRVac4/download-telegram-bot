from telebot.types import Message, CallbackQuery
from loader import bot
from database.models import db, History
from keyboards.inline.del_history import del_history, del_history_call_data
from send_file import send_file
import os

@bot.message_handler(commands=['864786'])
def history(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text="Выберите действие?", reply_markup=del_history())


@bot.callback_query_handler(func=lambda call: call.data in del_history_call_data)
def check_command(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    text = call.data
    # base_path = "/Users/Tony/PycharmProjects/download-telegram-bot/database/files"
    base_path = "TonyRVac4/download-telegram-bot/database/files/"
    counter = 0
    if text == "output":
        with db:
            for hotel in History.select().where(History.user_id == user_id):
                counter += 1

                send_file(message=call.message, file_name=hotel.file_path, file_type=hotel.type)

    elif text == "del":
        with db:
            for hotel in History.select().where(History.user_id == user_id or History.user_id == 0):
                counter += 1
                path = os.path.join(base_path, hotel.file_path)
                os.remove(path)
                hotel.delete_instance()
            bot.edit_message_text(text="История очищена",
                                  chat_id=chat_id,
                                  message_id=call.message.id)

    if counter == 0:
        bot.edit_message_text(text="История пуста",
                              chat_id=chat_id,
                              message_id=call.message.id)
