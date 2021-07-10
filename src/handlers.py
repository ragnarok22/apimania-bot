from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from constants import WEB_TO_PDF


def start(update, context):
    apimania_button = InlineKeyboardButton(
        text='Página de Apimania',
        url='https://apimania.dsoto.dev'
    )
    web_to_pdf_button = InlineKeyboardButton(
        text='Web a PDF',
        callback_data='web_to_pdf'
    )
    update.message.reply_text(
        text='Este es el bot de telegram de Apimania.\n\nCon él puedes crear PDF a partir de páginas web, convertir '
             'texto a imágenes, convertir tablas HTML a json y mucho más',
        reply_markup=InlineKeyboardMarkup([
            [apimania_button],
            [web_to_pdf_button]
        ])
    )


def web_to_pdf(update, context):
    update.message.reply_text('Envíame la URL para enviártela en PDF')
    return WEB_TO_PDF


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
