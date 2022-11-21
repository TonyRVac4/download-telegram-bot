from telebot.types import Message, CallbackQuery
from loader import bot
from keyboards.inline.del_history import del_history, del_history_call_data
from send_file import send_file
import os
from config_data.config import DATA_BASE_PATH


@bot.message_handler(commands=['864786'])
def history(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text="Выберите действие?", reply_markup=del_history())


@bot.callback_query_handler(func=lambda call: call.data in del_history_call_data)
def check_command(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    text = call.data

    counter = 0
    file_type = str()
    user_db_path = os.path.join(DATA_BASE_PATH, str(user_id))

    if text == "output":
        for i_file in os.listdir(user_db_path):

            if i_file.endswith("Video.MP4"):
                file_type = "Y-video"
            elif i_file.endswith("Audio.MP4"):
                file_type = "Y-audio"

            send_file(message=call.message, file_name=i_file, file_type=file_type)
    elif text == "del":
        for i_file in os.listdir(user_db_path):
            os.remove(os.path.join(user_db_path, i_file))
        counter += 1
        bot.edit_message_text(text="История очищена",
                              chat_id=chat_id,
                              message_id=call.message.id)

    if counter == 0:
        bot.edit_message_text(text="История пуста",
                              chat_id=chat_id,
                              message_id=call.message.id)
