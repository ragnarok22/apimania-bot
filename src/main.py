from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler

from config import handlers, conversations, dp, updater, callbacks, BASE_DIR

if __name__ == '__main__':

    # conversations handlers
    for conversation in conversations:
        dp.add_handler(ConversationHandler(
            entry_points=conversation.get('entry_points'),
            states=conversation.get('states'),
            fallbacks=conversation.get('fallbacks', [])
        ))

    # callbacks
    for callback in callbacks:
        dp.add_handler(CallbackQueryHandler(callback.get('handler'), callback.get('pattern')))

    # handlers
    for handler in handlers:
        dp.add_handler(CommandHandler(handler.get('command'), handler.get('handler')))

    updater.start_polling()
    print('Bot is polling')
    updater.idle()
