from telegram.ext import CommandHandler

def start(bot, update):
    chat_id = update.message.chat_id

    if update.message.from_user.username is None:
        bot.send_message(
                chat_id=chat_id,
                text="""Hola! Necesitas tener un username primero.
                        \nCreate uno siguiendo esta guia: https://ewtnet.com/technology/how-to/how-to-add-a-username-on-telegram-android-app.
                        Y despues dame /start the nuevo :) """)

    elif update.message.from_user.username:
        bot.send_message(
                chat_id=chat_id,
                text='Hola ' + update.message.from_user.username +
                     '! Bienvenidx'
                )


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Ayudaaaaaaaaaaaaaaaaa')



def set_handlers(updater):
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('ayuda', help))
