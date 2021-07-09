import os
from telegram import ChatAction
from telegram.ext import ConversationHandler

from src.utils import is_url, download_file


def input_web_url(update, context):
    url = update.message.text
    chat = update.message.chat
    print('URL', url)

    if is_url(url):
        print('the URL is correct')
        # capture de web
        filename = 'url-apimania.pdf'
        download_file(url, filename)
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