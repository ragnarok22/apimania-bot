from telegram import InlineKeyboardButton, InlineKeyboardMarkup

APIMANIA_URL = 'https://apimania.dsoto.dev/api'

# states
NOT_IMPLEMENTED = -1
WEB_TO_PDF = 0
WEB_TO_IMG = 1
TEXT_TO_IMG = 2
TABLE_TO_JSON = 3
WEB_TO_JSON = 4

about_text = '*Sobre el bot:*\n' \
             'Este bot está basado en [APImania](https://apimania.dsoto.dev). Todas las funcionalidades son usando ' \
             'sus APIs\n\n ' \
             '*Sobre los creadores:*\n' \
             'Creador del bot: [Reinier Hernández](https://twitter.com/RagnarokReinier) (Ragnarok22)\n' \
             'Creador de APImanía: [Damian Soto](https://twitter.com/sotoplatero) (dsoto)'

about_authors = InlineKeyboardButton(
    text='Sobre el bot',
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
web_to_img_button = InlineKeyboardButton(
    text='Captura a web',
    callback_data='web_to_img'
)
text_to_img_button = InlineKeyboardButton(
    text='Texto a imagen',
    callback_data='text_to_img'
)
table_to_json_button = InlineKeyboardButton(
    text='Tabla HTML a JSON',
    callback_data='table_to_json'
)
web_to_json_button = InlineKeyboardButton(
    text='Página web a JSON',
    callback_data='web_to_json'
)

BUTTONS_MARKUP = [
    [web_to_pdf_button, web_to_img_button],
    [text_to_img_button],
    [table_to_json_button, web_to_json_button],
    [apimania_button, about_authors],
]

BACK_BUTTON = InlineKeyboardButton(
    text='⬅️ Regresar',
    callback_data='main'
)
BACK_MARKUP = InlineKeyboardMarkup([
    [BACK_BUTTON]
])
