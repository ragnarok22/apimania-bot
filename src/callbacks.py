from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

import constants


def main_menu_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

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

    query.edit_message_text(
        text='¿Qué deseas hacer?',
        reply_markup=InlineKeyboardMarkup([
            [web_to_pdf_button, web_to_img_button],
            [text_to_img_button],
            [table_to_json_button, web_to_json_button],
            [apimania_button, about_authors],
        ])
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
