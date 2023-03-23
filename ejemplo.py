import logging
from telegram.ext import CommandHandler

# Esto es un metodo que se llama ejemplo, pueden cambiarle
# el nombre a algo mas representativo de lo que quieran hacer.
# Recuerden tambien cambiar el nombre abajo en el ComandHandler.
def ejemplo(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
            chat_id=chat_id,
            text='Hola ' + update.message.from_user.username + ' esto es un ejemplo'
            )


    # Herramientas para empezar jugar: el metodo update tiene mucha informacion:
    username = update.message.from_user.username
    chat_id = update.message.chat_id



def set_handlers(updater):
# cuando pongan /ejemplo_comando en el bot se va a ejecutar el metodo ejemplo que esta arriba.
    updater.dispatcher.add_handler(CommandHandler('ejemplo_comando', ejemplo))
