import logging
from telegram.ext import ApplicationBuilder
from config import TOKEN
from base import start_handler, echo_handler
from ejemplo import ejemplo_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(ejemplo_handler)

    application.run_polling()