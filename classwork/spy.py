"""Doc."""
from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime as dt


def log(update: Update, context: CallbackContext):
    """Doc."""
    time = dt.now().strftime('%H:%M')
    file = open('db.csv', 'a', encoding='utf=8')
    file.write(
        f'{time}, {update.effective_user.first_name}, '
        f'{update.effective_user.id}, '
        f'{update.message.text}\n')
    file.close()
