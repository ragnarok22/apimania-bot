import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from src.callbacks import web_to_pdf_handler
from src.constants import WEB_TO_PDF
from src.conversations import input_web_url
from src.handlers import start, about, set_lang, web_to_pdf

if __name__ == '__main__':
    load_dotenv()
    updater = Updater(token=os.getenv('ACCESS_TOKEN'), use_context=True)
    dp = updater.dispatcher

    # handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CommandHandler('setLang', set_lang))

    # conversations handlers
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('web_to_pdf', web_to_pdf),
            CallbackQueryHandler(pattern='web_to_pdf', callback=web_to_pdf_handler)
        ],
        states={
            WEB_TO_PDF: [MessageHandler(Filters.text, input_web_url)]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    print('Bot is polling')
    updater.idle()
