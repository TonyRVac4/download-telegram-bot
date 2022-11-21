from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands

set_default_commands()
bot.polling(none_stop=True, interval=0)
