import logging
import os
from telegram.ext import Updater
from config import TOKEN
import base
import ejemplo


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


def set_handlers(updater):
    base.set_handlers(updater)
    ejemplo.set_handlers(updater)
  

logger.info('Starting Bot')

updater = Updater(TOKEN)

#models_db_connection()
set_handlers(updater)

updater.start_polling()