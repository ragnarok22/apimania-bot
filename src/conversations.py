import os
from telegram import ChatAction
from telegram.ext import ConversationHandler

from utils import is_url, url_to_pdf


def input_web_url(update, context):
    url = update.message.text
    chat = update.message.chat
    print('URL', url)

    if is_url(url):
        print('the URL is correct')
        chat.send_action(
            action=ChatAction.UPLOAD_DOCUMENT,
            timeout=None
        )
        # capture de web
        filename = url_to_pdf(url)
        # send the pdf
        chat.send_document(
            document=open(filename, 'rb')
        )
        os.unlink(filename)
    else:
        print('wrong URL')
        update.message.reply_text('debes de enviar una URL válida. Ejemplo: http://google.com')
    return ConversationHandler.END
