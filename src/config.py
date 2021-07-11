import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, CallbackQueryHandler, Filters, MessageHandler, Updater

from callbacks import web_to_pdf_handler, text_to_img_handler, web_to_img_handler, table_to_json_handler, \
    web_to_json_handler
from constants import WEB_TO_PDF, TEXT_TO_IMG, WEB_TO_IMG, TABLE_TO_JSON, WEB_TO_JSON
from conversations import input_web_url, about_conversation, text_to_img_conversation, web_to_img_conversation, \
    table_to_json_conversation, web_to_json_conversation
from handlers import start, about, set_lang, web_to_pdf, text_to_img, web_to_img, table_to_json, \
    web_to_json

load_dotenv()
updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)
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
    },
    {
        'entry_points': [
            CallbackQueryHandler(pattern='about', callback=about_conversation),
        ],
        'states': {
        },
    },
    {
        'entry_points': [
            CommandHandler('text_to_img', text_to_img),
            CallbackQueryHandler(pattern='text_to_img', callback=text_to_img_handler)
        ],
        'states': {
            TEXT_TO_IMG: [MessageHandler(Filters.text, text_to_img_conversation)]
        },
    },
    {
        'entry_points': [
            CommandHandler('web_to_img', web_to_img),
            CallbackQueryHandler(pattern='web_to_img', callback=web_to_img_handler)
        ],
        'states': {
            WEB_TO_IMG: [MessageHandler(Filters.text, web_to_img_conversation)]
        },
    },
    {
        'entry_points': [
            CommandHandler('table_to_json', table_to_json),
            CallbackQueryHandler(pattern='table_to_json', callback=table_to_json_handler)
        ],
        'states': {
            TABLE_TO_JSON: [MessageHandler(Filters.text, table_to_json_conversation)]
        },
    },
    {
        'entry_points': [
            CommandHandler('web_to_json', web_to_json),
            CallbackQueryHandler(pattern='web_to_json', callback=web_to_json_handler)
        ],
        'states': {
            WEB_TO_JSON: [MessageHandler(Filters.text, web_to_json_conversation)]
        },
    },
]
