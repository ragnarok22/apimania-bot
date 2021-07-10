from constants import WEB_TO_PDF


def web_to_pdf_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL para enviártela en PDF'
    )
    return WEB_TO_PDF
