"""Doc."""
import logging
import bot
import time
import log_generate as lg
import os
os.system('cls')

# Встроенное логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename='bot.log', filemode='a'
)
logger = logging.getLogger(__name__)


def main():
    """Doc."""
    lg.write_data('{} {}'.format('Старт работы бота:',
                  time.strftime('%d.%m.%y %H:%M')))
    bot.start_bot()


if __name__ == '__main__':
    main()
