"""Doc."""
from config import TOKEN
from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import (hi_command, time_command,
                          help_command, sum_command, del_abv_command)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("delabv", del_abv_command))
# app.add_handler(CommandHandler("candies", candies_command))

print('server start')
app.run_polling()
