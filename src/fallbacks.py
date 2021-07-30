from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler


def back_fallback(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Adiós',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
