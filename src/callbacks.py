from constants import WEB_TO_PDF, TEXT_TO_IMG, WEB_TO_IMG, NOT_IMPLEMENTED, TABLE_TO_JSON


def web_to_pdf_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL para enviártela en PDF'
    )
    return WEB_TO_PDF


def web_to_img_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL para tirarle una captura'
    )
    return WEB_TO_IMG


def text_to_img_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame el texto a convertir en imagen'
    )
    return TEXT_TO_IMG


def table_to_json_handler(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Envíame la URL de la tabla'
    )
    return TABLE_TO_JSON


def not_implemented_handler(update, context):
    query = update.callback_query
    query.answer()
    return NOT_IMPLEMENTED
