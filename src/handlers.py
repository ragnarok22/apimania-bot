from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from constants import WEB_TO_PDF, TEXT_TO_IMG


def start(update, context):
    about_authors = InlineKeyboardButton(
        text='Autores',
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
    text_to_img = InlineKeyboardButton(
        text='Texto a imagen',
        callback_data='text_to_img'
    )
    update.message.reply_text(
        text='Este es el bot de telegram de Apimania.\n\nCon él puedes crear PDF a partir de páginas web, convertir '
             'texto a imágenes, convertir tablas HTML a json y mucho más',
        reply_markup=InlineKeyboardMarkup([
            [web_to_pdf_button, text_to_img],
            [apimania_button, about_authors],
        ])
    )


def web_to_pdf(update, context):
    update.message.reply_text('Envíame la URL para enviártela en PDF')
    return WEB_TO_PDF


def text_to_img(update, context):
    update.message.reply_text('Envíame el texto a convertir')
    return TEXT_TO_IMG


def about(update, context):
    ragnarok_button = InlineKeyboardButton(
        text='@Ragnarok22',
        url='https://ragnarok22.dev'
    )
    dsoto_button = InlineKeyboardButton(
        text='@dsoto',
        url='https://dsoto.dev'
    )
    update.message.reply_text(
        text='@Ragnarok22 es el creador del bot y @dsoto es el creador del API',
        reply_markup=InlineKeyboardMarkup([
            [ragnarok_button, dsoto_button]
        ])
    )


def set_lang(update, context):
    update.message.reply_text(
        text='work in progress'
    )
