from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from database.models import History


set_default_commands()
History.create_table()
bot.polling(none_stop=True, interval=0)
