import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext
from tinydb import Query

import constants
import config


def start(update: Update, context: CallbackContext) -> None:
    chat = update.message.chat
    User = Query()
    users = config.db.search(User.id == chat.id)
    if len(users) == 0:
        # if user don't exists, save it.
        config.db.insert({
            'id': chat.id,
            'first_name': chat.first_name,
            'last_name': chat.last_name,
            'username': chat.username,
            'type': chat.type
        })
    logging.info(update.message.chat)

    update.message.reply_text(
        text='Hola {0}. Este es el bot de telegram de Apimania.\n\nCon él puedes crear PDF a partir de páginas web, '
             'convertir texto a imágenes, convertir tablas HTML a json y mucho más'.format(
            update.message.chat.first_name),
        reply_markup=InlineKeyboardMarkup(constants.BUTTONS_MARKUP)
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
    back_button = InlineKeyboardButton(
        text='⬅️Regresar',
        callback_data='main'
    )
    update.message.reply_text(
        text=constants.about_text,
        reply_markup=InlineKeyboardMarkup([
            [ragnarok_button, dsoto_button],
            [back_button]
        ]),
        parse_mode=ParseMode.MARKDOWN
    )


def set_lang(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='work in progress'
    )


def not_implemented(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('NOT_IMPLEMENTED')
