import sys

from telegram.ext import Updater, CommandHandler


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='I am tw_bot!')


def hello(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello {}'.format(update.message.from_user.first_name))

updater = Updater(sys.argv[1])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
