"""Doc."""
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime as dt
from spy import log
import emoji


async def hi_command(update: Update, context:
                     ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')
    victory = emoji.emojize(':victory_hand:')
    await update.message.reply_text(f'{victory}')


async def help_command(update: Update, context:
                       ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    await update.message.reply_text('/hi\n/time\n/help\nЧтобы '
                                    'посчитать сумму: "/sum number number" '
                                    '\n/delabv')


async def time_command(update: Update, context:
                       ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    time = dt.now().strftime('%H:%M')
    await update.message.reply_text(f'Сейчас: {time}')
    ok = emoji.emojize(':OK_hand:')
    await update.message.reply_text(f'{ok}')


async def sum_command(update: Update, context:
                      ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')
    ok = emoji.emojize(':nerd_face:')
    await update.message.reply_text(f'{ok}')


async def del_abv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Doc."""
    log(update, context)
    text = update.message.text[1:]
    await update.message.reply_text(
        f" {' '.join(list(i for i in list(text.split()) if 'абв' not in i))}"
    )
