import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, CallbackQueryHandler, Filters, MessageHandler, Updater

from handlers import start, about, set_lang, web_to_pdf
from src.callbacks import web_to_pdf_handler
from src.constants import WEB_TO_PDF
from src.conversations import input_web_url

load_dotenv()
updater = Updater(token=os.getenv('ACCESS_TOKEN'), use_context=True)
dp = updater.dispatcher

handlers = [
    {
        'command': 'start',
        'handler': start
    },
    {
        'command': 'about',
        'handler': about
    },
    {
        'command': 'setLang',
        'handler': set_lang
    },
]

conversations = [
    {
        'entry_points': [
            CommandHandler('web_to_pdf', web_to_pdf),
            CallbackQueryHandler(pattern='web_to_pdf', callback=web_to_pdf_handler)
        ],
        'states': {
            WEB_TO_PDF: [MessageHandler(Filters.text, input_web_url)]
        },
        'fallbacks': []
    }
]
