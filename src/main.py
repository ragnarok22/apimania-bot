import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, ConversationHandler

from config import handlers, conversations

if __name__ == '__main__':
    load_dotenv()
    updater = Updater(token=os.getenv('ACCESS_TOKEN'), use_context=True)
    dp = updater.dispatcher

    # handlers
    for handler in handlers:
        dp.add_handler(CommandHandler(handler.get('command'), handler.get('handler')))

    # conversations handlers
    for conversation in conversations:
        dp.add_handler(ConversationHandler(
            entry_points=conversation.get('entry_points'),
            states=conversation.get('states'),
            fallbacks=conversation.get('fallbacks')
        ))

    updater.start_polling()
    print('Bot is polling')
    updater.idle()
