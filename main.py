from loader import bot
import handlers
import os
from utils.set_bot_commands import set_default_commands

set_default_commands()
bot.polling(none_stop=True, interval=0)
