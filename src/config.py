import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram.ext import CommandHandler, CallbackQueryHandler, Filters, MessageHandler, Updater
from tinydb import TinyDB

import callbacks as callbacks_module
import constants
import conversations
import handlers as handlers_module
import fallbacks

load_dotenv()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('APImaniaBot')

updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)
dp = updater.dispatcher

BASE_DIR = Path(__file__).resolve().parent.parent

handlers = [
    {
        'command': 'start',
        'handler': handlers_module.start
    },
    {
        'command': 'stats',
        'handler': handlers_module.stats
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

callbacks = [
    {
        'handler': callbacks_module.main_menu_callback,
        'pattern': 'main',
    }
]

conversations = [
    {
        'entry_points': [
            CommandHandler('web_to_pdf', handlers_module.web_to_pdf),
            CallbackQueryHandler(pattern='web_to_pdf', callback=callbacks_module.web_to_pdf_handler)
        ],
        'states': {
            constants.WEB_TO_PDF: [MessageHandler(Filters.text, conversations.input_web_url)]
        },
        'fallbacks': [
            CallbackQueryHandler(pattern='main', callback=callbacks_module.main_menu_callback)
        ]
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
            CallbackQueryHandler(pattern='text_to_img', callback=callbacks_module.text_to_img_handler)
        ],
        'states': {
            constants.TEXT_TO_IMG: [MessageHandler(Filters.text, conversations.text_to_img_conversation)]
        },
        'fallbacks': [
            CallbackQueryHandler(pattern='main', callback=callbacks_module.main_menu_callback)
        ]
    },
    {
        'entry_points': [
            CommandHandler('web_to_img', handlers_module.web_to_img),
            CallbackQueryHandler(pattern='web_to_img', callback=callbacks_module.web_to_img_handler)
        ],
        'states': {
            constants.WEB_TO_IMG: [MessageHandler(Filters.text, conversations.web_to_img_conversation)]
        },
        'fallbacks': [
            CallbackQueryHandler(pattern='main', callback=callbacks_module.main_menu_callback)
        ]
    },
    {
        'entry_points': [
            CommandHandler('table_to_json', handlers_module.table_to_json),
            CallbackQueryHandler(pattern='table_to_json', callback=callbacks_module.table_to_json_handler)
        ],
        'states': {
            constants.TABLE_TO_JSON: [MessageHandler(Filters.text, conversations.table_to_json_conversation)]
        },
        'fallbacks': [
            CallbackQueryHandler(pattern='main', callback=callbacks_module.main_menu_callback)
        ]
    },
    {
        'entry_points': [
            CommandHandler('web_to_json', handlers_module.web_to_json),
            CallbackQueryHandler(pattern='web_to_json', callback=callbacks_module.web_to_json_handler)
        ],
        'states': {
            constants.WEB_TO_JSON: [MessageHandler(Filters.text, conversations.web_to_json_conversation)]
        },
        'fallbacks': [
            CallbackQueryHandler(pattern='main', callback=callbacks_module.main_menu_callback)
        ]
    },
]

DATABASE = {
    'NAME': 'db.json'
}
db = TinyDB(os.path.join(BASE_DIR, DATABASE.get('NAME', 'db.json')))
