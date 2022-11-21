from loader import bot
import handlers
import os
from utils.set_bot_commands import set_default_commands

set_default_commands()
if str("files") not in os.listdir("TonyRVac4/download-telegram-bot/database"):
    os.mkdir("TonyRVac4/download-telegram-bot/database/files")
bot.polling(none_stop=True, interval=0)
