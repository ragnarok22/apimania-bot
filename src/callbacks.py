from constants import WEB_TO_PDF, TEXT_TO_IMG


def web_to_pdf_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL para enviártela en PDF'
    )
    return WEB_TO_PDF


def text_to_img_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame el texto a convertir en imagen'
    )
    return TEXT_TO_IMG
