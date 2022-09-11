from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
import os,json

TOKEN = os.environ['TOKEN']

class BotClass:
    def __init__(self) -> None:
        self.name = None
        self.id = None

    def start(self, update:Update, context:CallbackContext):
        id = int(update.message.from_user.id)
        first = update.message.from_user.first_name
        full = update.message.from_user.full_name

        with open('admin.json', 'r') as f:
            admin = json.load(f)

        if id in admin.values():
            updater.bot.sendMessage(id, 'Xush kelbsiz admin')
            self.button(update, context)
        else:
            self.name = first
            self.id = id
            updater.bot.sendMessage(id, '🙂🙃Xush kilibsiz bizning botga!\n🙂🙃Bot admini sizni botga qo\'shginch kutib turing')
            for i in admin.values():
                text = f'{first}, {full}ni botga qo\'shasizmi'
                inlineKeyboard = InlineKeyboardButton(f'yo\'q qo\'shmayman❌',callback_data='no')
                inlineKeyboard1 = InlineKeyboardButton(f'ha qo\'shaman✅',callback_data=f'ha')
                reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
                updater.bot.sendMessage(i, text, reply_markup=reply_markup)

    def button(self, update:Update, context:CallbackContext):
        keyboard = [[KeyboardButton('test ✍️'), KeyboardButton('yo\'qlama✅')],[KeyboardButton('admin📥'), KeyboardButton('ro\'yhat📊')], [KeyboardButton('admin olib tashlash📤'),KeyboardButton('o\'quvchi olib tashlash📤')]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        updater.bot.sendMessage(update.message.from_user.id, 'natijalarni kiriting', reply_markup=reply_markup)

    def getDb(self,id):
        with open('db.json', 'r') as f:
            db = json.load(f)
        nams = ["👨‍💻O'quvchilar ro'yxati👨‍💻"]
        for k,v in db.items():
            nams.append('📌'+str(v['name']))
        updater.bot.sendMessage(id, '\n'.join(nams))

    def gety(self, update:Update, context:CallbackContext, id):
        with open('db.json', 'r') as f:
            db = json.load(f)

        for k,v in db.items():
            id2 = v['id']
            inlineKeyboard = InlineKeyboardButton(f'yo\'q kemadi❌',callback_data=f'❌{id2}')
            inlineKeyboard1 = InlineKeyboardButton(f'ha keldi✅',callback_data=f'kemadi')
            reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
            updater.bot.sendMessage(id, f"{v['name']} kildimi?", reply_markup=reply_markup)

    def addpuppel(self, update:Update, context:CallbackContext, id):
        with open('db.json', 'r') as f:
                user = json.load(f)

        for k,v in user.items():
            inlineKeyboard = InlineKeyboardButton(f'ha olinsin🚫',callback_data=f'🚫')
            inlineKeyboard1 = InlineKeyboardButton(f'yo\'q saqlansin🆗',callback_data=f'🆗')
            reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
            updater.bot.sendMessage(id, f"{v['name']} botdan olinsinmi?", reply_markup=reply_markup)

    def stopadd(self, update:Update, context:CallbackContext, id):
        with open('admin.json', 'r') as f:
                user = json.load(f)
        with open('db.json', 'r') as f:
                data = json.load(f)

        for k,i in user.items():
            for e,v in data.items():
                if v['id'] == i:
                    inlineKeyboard = InlineKeyboardButton(f'saqlabqolish✅',callback_data=f'✅')
                    inlineKeyboard1 = InlineKeyboardButton(f'yo\'qqolosh❎',callback_data=f'❎{i}')
                    reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
                    updater.bot.sendMessage(id, f"{v['name']} bot adminini olib tashlaysizmi?", reply_markup=reply_markup)

    def buttonRespons(self, update:Update, context:CallbackContext):
        with open('admin.json', 'r') as f:
            users = json.load(f)
        users = users.values()
        text = update.message.text
        id = update.message.chat.id

        if text == 'ro\'yhat📊':
            if id in users:
                self.getDb(id)
            else:
                updater.bot.sendMessage(id, 'Siz bot admin emassiz ‼️ kechirasiz sizga bunday imkoniyat berilmagan')

        if text == 'yo\'qlama✅':
            if id in users:
                id = update.message.from_user.id
                self.gety(update, context, id)
            else:
                updater.bot.sendMessage(id, 'Siz bot admin emassiz ‼️ kechirasiz sizga bunday imkoniyat berilmagan')

        if text == 'admin📥':
            if id in users:
                self.addAdmin(update, context, id)
            else:
                updater.bot.sendMessage(id, 'Siz bot admin emassiz ‼️ kechirasiz sizga bunday imkoniyat berilmagan')

        if text == 'test ✍️':
            if id in users:
                updater.bot.sendMessage(id,f'Test natijalarni rasim ko\'rinishida kiriting 📷')
            else:
                updater.bot.sendMessage(id, 'Siz bot admin emassiz ‼️ kechirasiz sizga bunday imkoniyat berilmagan')

        if text == 'admin olib tashlash📤':
            if id in users:
                self.stopadd(update, context, id)
            else:
                updater.bot.sendMessage(id, 'Siz bot admin emassiz ‼️ kechirasiz sizga bunday imkoniyat berilmagan')

        if text == 'o\'quvchi olib tashlash📤':
            if id in users:
                self.addpuppel(update, context, id)
            else:
                updater.bot.sendMessage(id, 'Siz bot admin emassiz ‼️ kechirasiz sizga bunday imkoniyat berilmagan')

    def getTest(self, update:Update, context:CallbackContext):
        id = update.message.chat.id
        with open('admin.json', 'r') as f:
            users = json.load(f)
        users = users.values()

        if id in users:
            photo = update.message.photo[0].file_id
            with open('db.json', 'r') as f:
                data = json.load(f)
            for k,v in data.items():
                updater.bot.sendPhoto(v['id'], photo, caption='test natijalari chiqdi❎✅❌☑️')
            updater.bot.sendMessage(id, 'Natijalar yuborildi🆗✅')
        else:
            updater.bot.sendMessage(id, 'Siz bot admin emassiz ‼️ kechirasiz sizga bunday imkoniyat berilmagan')

    def getControl(self):
        pass

    def addAdmin(self, update:Update, context:CallbackContext, id):
        with open('db.json', 'r') as f:
                user = json.load(f)

        for k,v in user.items():
            id2 = v['id']
            inlineKeyboard = InlineKeyboardButton(f'yo\'q admin🔴',callback_data=f'🔴')
            inlineKeyboard1 = InlineKeyboardButton(f'ha admin🟢',callback_data=f'🟢{id2}')
            reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1]])
            updater.bot.sendMessage(id, f"{v['name']} bot admini qilasizmi?", reply_markup=reply_markup)

    def getQuery(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        id = self.id
        name = self.name
        updater.bot.sendMessage(id, f'👩🏻‍🏫👨🏻‍🏫Hurmatli foydalanuvch {name}\nsizni bot admini botga qo\'shdi\nendi siz turli testlar,\nyo\'qlamalardan habardor bo\'lasiz👩🏻‍🏫👨🏻‍🏫\🎉🎊 bir bor botimizga hush kelibsiz🎉🎊')
        data = {'id':id, 'name':name}
        with open('db.json', 'r') as f:
            db = json.load(f)
        if data not in db.values():
            db[str(len(db)+1)] = data
        with open('db.json', 'w') as f:
            json.dump(db, f, indent=2)
        quere.edit_message_text(f'{self.name} botingizga qo\'shildi', reply_markup=None)

    def getQueryno(self, update:Update, context:CallbackContext):
        id = self.id
        name = self.name
        updater.bot.sendMessage(id, f'📵❗️Hurmatli foydalanuvch {name}\nsizni bot admini turli sabablarga ko\'ra\nbotga qo\'shmadi📵❗️')

    def getK(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        text = quere.data
        number = ''
        for i in text:
            if i.isdigit():
                number += i
        if len(number) > 0:
            updater.bot.sendMessage(int(number), 'bugun darsga nega kelmadingiz 😠😡 ‼️⁉️\nboshqa buhol takrorlanmasin 😠😡 ❌‼️\n yana takrorlansa sizbilan hayr lashamiz ✋')
        quere.edit_message_text('Yuborildi📲', reply_markup=None)

    def getKmadi(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        quere.edit_message_text('Yuborildi📲', reply_markup=None)

    def addp(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        text_data = quere.message.text
        text = text_data.split()[0]
        
        with open('db.json', 'r') as f:
                user = json.load(f)

        user2 = {}
        for k,v in user.items():
            if text != v['name']:
                user2[str(len(user2) + 1)] = v
            if text == v['name']:
                name = v['name']
                id = v['id']
                updater.bot.sendMessage(id, f'📵❗️Hurmatli foydalanuvch {name}\nsizni bot admini turli sabablarga ko\'ra\nbotdan olib tashladi📵❗️')

        with open('db.json', 'w') as f:
                json.dump(user2, f, indent=2)
        quere.edit_message_text('Bu o\'quvchi botdan o\'chirildi🚫', reply_markup=None)

    def adds(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        quere.edit_message_text('Bu o\'quvchi botda saqlandi✅', reply_markup=None)

    def adda(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        with open('admin.json', 'r') as f:
            data = json.load(f)

        user_id = quere.data

        adminid = int(user_id[1:])
        if adminid not in data.values():
            data[str(len(data) + 1)] = adminid
            updater.bot.sendMessage(adminid, '🎉🎊Siz bot admini bo\'ldingiz tabriklayman🎉🎊')

        with open('admin.json', 'w') as f:
            json.dump(data, f, indent=2)

        quere.edit_message_text('Bu foydalanuvchi adminlardan biri bo\'ldi✅', reply_markup=None)

    def adda2(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        quere.edit_message_text('Bu foydalanuvchi adminlikka tavsiya etilmadi❌', reply_markup=None)

    def okaddmin(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        quere.edit_message_text('Bu admin saqlab qolindi✅', reply_markup=None)

    def stopaddmin(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        id = int(quere.data[1:])
        with open('admin.json', 'r') as f:
            data = json.load(f)
        data2 = {}
        for k,v in data.items():
            if v != id:
                data2[str(len(data2) + 1)] = v
        with open('admin.json', 'w') as f:
            json.dump(data2, f, indent=2)
        updater.bot.sendMessage(id, '🚫📵siz turli sabablarga ko\'ra adminlikdan olindingiz📵🚫')
        quere.edit_message_text('Bu admin olib tashlandi❎', reply_markup=None)

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