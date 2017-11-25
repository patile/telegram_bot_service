import telegram
import threading
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import config
import requests,json
TOKEN = config["TOKEN"]
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

class Test:
    def __init__(self):
        self.txt = ""
        self.image_id = ""
        self.geolocation = ""
    def Start(self,bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text = "Hello Test.")

    def test2(self,bot,update):
        chat_id = bot.get_updates()
        print(chat_id)
        text = update.message.text
        file_id = update.message.photo[0] 

        print(file_id.file_id)

    def aciklama(self,bot,update):
        msg = update.message.text
        self.txt = msg
        print(self.txt)

    def parse_geolocation(self,bot,update):
        pass

    def run(self):
        dispatcher.add_handler(MessageHandler(Filters.photo, self.test2))

        aciklama_handler = CommandHandler('aciklama', self.aciklama)
        dispatcher.add_handler(aciklama_handler)

        updater.start_polling()

obj = Test()
th1 = threading.Thread(target=obj.run())