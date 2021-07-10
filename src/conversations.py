import os
from telegram import ChatAction
from telegram.ext import ConversationHandler

from src.utils import is_url, url_to_pdf, get_filename_from_url


def input_web_url(update, context):
    url = update.message.text
    chat = update.message.chat
    print('URL', url)

    if is_url(url):
        print('the URL is correct')
        # capture de web
        filename = get_filename_from_url(url)
        url_to_pdf(url, filename)
        # send the pdf
        chat.send_action(
            action=ChatAction.UPLOAD_DOCUMENT,
            timeout=None
        )
        chat.send_document(
            document=open(filename, 'rb')
        )
        # os.unlink(filename)
    else:
        print('wrong URL')
        update.message.reply_text('debes de enviar una URL válida. Ejemplo: http://google.com')
    return ConversationHandler.END