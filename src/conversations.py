import os
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ConversationHandler

from utils import is_url, url_to_pdf


def input_web_url(update, context):
    url = update.message.text
    chat = update.message.chat
    print('URL', url)

    if is_url(url):
        print('the URL is correct')
        # capture de web
        update.message.reply_text('Convirtiendo la página en PDF')
        filename = url_to_pdf(url)
        # send the pdf
        chat.send_action(
            action=ChatAction.UPLOAD_DOCUMENT,
            timeout=None
        )
        chat.send_document(
            document=open(filename, 'rb')
        )
        os.unlink(filename)
    else:
        print('wrong URL')
        update.message.reply_text('debes de enviar una URL válida. Ejemplo: http://google.com')
    return ConversationHandler.END


def about_conversation(update, context):
    query = update.callback_query
    query.answer()
    ragnarok_button = InlineKeyboardButton(
        text='@Ragnarok22',
        url='https://ragnarok22.dev'
    )
    dsoto_button = InlineKeyboardButton(
        text='@dsoto',
        url='https://dsoto.dev'
    )

    query.edit_message_text(
        text='@Ragnarok22 es el creador del bot y @dsoto es el creador del API',
        reply_markup=InlineKeyboardMarkup([
            [ragnarok_button, dsoto_button]
        ])
    )
