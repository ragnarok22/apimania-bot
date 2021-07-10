import os

from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import ConversationHandler

from constants import about_text
from utils import is_url, url_to_pdf, convert_text_to_img, convert_web_to_img, convert_table_to_json


def text_to_img_conversation(update, context):
    text = update.message.text
    chat = update.message.chat

    update.message.reply_text('Convirtiendo el texto en imagen')
    filename = convert_text_to_img(text)
    # send the img
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)
    return ConversationHandler.END


def web_to_img_conversation(update, context):
    url = update.message.text
    chat = update.message.chat

    update.message.reply_text('Tomándole una captura a la web')
    filename = convert_web_to_img(url)
    # send the img
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)
    return ConversationHandler.END


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
        text='Ragnarok22',
        url='https://ragnarok22.dev'
    )
    dsoto_button = InlineKeyboardButton(
        text='dsoto',
        url='https://dsoto.dev'
    )

    query.edit_message_text(
        text=about_text,
        reply_markup=InlineKeyboardMarkup([
            [ragnarok_button, dsoto_button]
        ]),
        parse_mode=ParseMode.MARKDOWN
    )
    return ConversationHandler.END


def table_to_json_conversation(update, context):
    url = update.message.text
    chat = update.message.chat

    update.message.reply_text('Convirtiendo la tabla en json')
    filename = convert_table_to_json(url)
    # send the json
    chat.send_action(
        action=ChatAction.UPLOAD_DOCUMENT,
        timeout=None
    )
    chat.send_document(
        document=open(filename, 'r')
    )
    os.unlink(filename)
    return ConversationHandler.END


def not_implemented_conversation(update, context):
    update.message.reply_text('NOT_IMPLEMENTED')
    return ConversationHandler.END
