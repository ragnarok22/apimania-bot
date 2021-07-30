from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

import constants


def main_menu_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='¿Qué deseas hacer?',
        reply_markup=InlineKeyboardMarkup(constants.BUTTONS_MARKUP)
    )


def web_to_pdf_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL para enviártela en PDF'
    )
    return constants.WEB_TO_PDF


def web_to_img_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL para tirarle una captura'
    )
    return constants.WEB_TO_IMG


def text_to_img_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame el texto a convertir en imagen'
    )
    return constants.TEXT_TO_IMG


def web_to_json_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame una URL para convertirla a JSON'
    )
    return constants.WEB_TO_JSON


def table_to_json_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL de la tabla'
    )
    return constants.TABLE_TO_JSON


def not_implemented_handler(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    return constants.NOT_IMPLEMENTED
