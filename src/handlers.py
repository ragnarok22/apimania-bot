import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext

import constants


def start(update: Update, context: CallbackContext) -> None:
    logging.info(update.message.chat)
    about_authors = InlineKeyboardButton(
        text='Sobre el bot',
        callback_data='about'
    )
    apimania_button = InlineKeyboardButton(
        text='Página de Apimania',
        url='https://apimania.dsoto.dev'
    )
    web_to_pdf_button = InlineKeyboardButton(
        text='Web a PDF',
        callback_data='web_to_pdf'
    )
    web_to_img_button = InlineKeyboardButton(
        text='Captura a web',
        callback_data='web_to_img'
    )
    text_to_img_button = InlineKeyboardButton(
        text='Texto a imagen',
        callback_data='text_to_img'
    )
    table_to_json_button = InlineKeyboardButton(
        text='Tabla HTML a JSON',
        callback_data='table_to_json'
    )
    web_to_json_button = InlineKeyboardButton(
        text='Página web a JSON',
        callback_data='web_to_json'
    )
    update.message.reply_text(
        text='Hola {0}. Este es el bot de telegram de Apimania.\n\nCon él puedes crear PDF a partir de páginas web, '
             'convertir texto a imágenes, convertir tablas HTML a json y mucho más'.format(update.message.chat.first_name),
        reply_markup=InlineKeyboardMarkup([
            [web_to_pdf_button, web_to_img_button],
            [text_to_img_button],
            [table_to_json_button, web_to_json_button],
            [apimania_button, about_authors],
        ])
    )


def web_to_pdf(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Envíame la URL para enviártela en PDF')
    return constants.WEB_TO_PDF


def web_to_img(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Envíame la URL para tirarle una captura')
    return constants.WEB_TO_IMG


def web_to_json(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Envíame una URL para convertirla a JSON')
    return constants.WEB_TO_JSON


def table_to_json(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Envíame la URL de la tabla')
    return constants.TABLE_TO_JSON


def text_to_img(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Envíame el texto a convertir')
    return constants.TEXT_TO_IMG


def about(update: Update, context: CallbackContext) -> None:
    ragnarok_button = InlineKeyboardButton(
        text='Ragnarok22',
        url='https://ragnarok22.dev'
    )
    dsoto_button = InlineKeyboardButton(
        text='dsoto',
        url='https://dsoto.dev'
    )
    update.message.reply_text(
        text=constants.about_text,
        reply_markup=InlineKeyboardMarkup([
            [ragnarok_button, dsoto_button]
        ]),
        parse_mode=ParseMode.MARKDOWN
    )


def set_lang(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='work in progress'
    )


def not_implemented(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('NOT_IMPLEMENTED')
