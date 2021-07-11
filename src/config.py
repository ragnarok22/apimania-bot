import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, CallbackQueryHandler, Filters, MessageHandler, Updater

import callbacks
import constants
import conversations
import handlers as handlers_module

load_dotenv()
updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)
dp = updater.dispatcher

handlers = [
    {
        'command': 'start',
        'handler': handlers_module.start
    },
    {
        'command': 'about',
        'handler': handlers_module.about
    },
    {
        'command': 'setLang',
        'handler': handlers_module.set_lang
    },
]

conversations = [
    {
        'entry_points': [
            CommandHandler('web_to_pdf', handlers_module.web_to_pdf),
            CallbackQueryHandler(pattern='web_to_pdf', callback=callbacks.web_to_pdf_handler)
        ],
        'states': {
            constants.WEB_TO_PDF: [MessageHandler(Filters.text, conversations.input_web_url)]
        },
        'fallbacks': []
    },
    {
        'entry_points': [
            CallbackQueryHandler(pattern='about', callback=conversations.about_conversation),
        ],
        'states': {
        },
    },
    {
        'entry_points': [
            CommandHandler('text_to_img', handlers_module.text_to_img),
            CallbackQueryHandler(pattern='text_to_img', callback=callbacks.text_to_img_handler)
        ],
        'states': {
            constants.TEXT_TO_IMG: [MessageHandler(Filters.text, conversations.text_to_img_conversation)]
        },
    },
    {
        'entry_points': [
            CommandHandler('web_to_img', handlers_module.web_to_img),
            CallbackQueryHandler(pattern='web_to_img', callback=callbacks.web_to_img_handler)
        ],
        'states': {
            constants.WEB_TO_IMG: [MessageHandler(Filters.text, conversations.web_to_img_conversation)]
        },
    },
    {
        'entry_points': [
            CommandHandler('table_to_json', handlers_module.table_to_json),
            CallbackQueryHandler(pattern='table_to_json', callback=callbacks.table_to_json_handler)
        ],
        'states': {
            constants.TABLE_TO_JSON: [MessageHandler(Filters.text, conversations.table_to_json_conversation)]
        },
    },
    {
        'entry_points': [
            CommandHandler('web_to_json', handlers_module.web_to_json),
            CallbackQueryHandler(pattern='web_to_json', callback=callbacks.web_to_json_handler)
        ],
        'states': {
            constants.WEB_TO_JSON: [MessageHandler(Filters.text, conversations.web_to_json_conversation)]
        },
    },
]
