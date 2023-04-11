from telegram.ext import Updater,MessageHandler,CommandHandler,CallbackQueryHandler, Filters
from handler import BotClass
TOKEN = '5677023630:AAGdskZAvZwdRix213Ho28QaN-NZVcQtuU8'


updater = Updater(TOKEN)
botClass = BotClass()
updater.dispatcher.add_handler(CommandHandler('start', botClass.start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, botClass.getTest))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.addp, pattern='🚫'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.adds, pattern='🆗'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.adda2, pattern='🔴'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.okaddmin, pattern='✅'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.stopaddmin, pattern='❎'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.adda, pattern='🟢'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.getQuery, pattern='ha'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.getQueryno, pattern='no'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.getK, '❌'))
updater.dispatcher.add_handler(CallbackQueryHandler(botClass.getKmadi, pattern='kemadi'))
updater.dispatcher.add_handler(MessageHandler(Filters.text, botClass.buttonRespons))

#Start the bot
updater.start_polling()
updater.idle()