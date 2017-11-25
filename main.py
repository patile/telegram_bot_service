import telegram
import threading
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram_photo_wrapper import Photo2Down
from location import Location
from message.message_methods import SendWarning
import math


TOKEN = "399989817:AAGvj_tw7gcRCBdpI68L11uvafH6fHSEoF4"
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
sender = SendWarning()
photo_wrapper = Photo2Down(TOKEN=TOKEN)

class Test:
    def __init__(self):
        self.ihbar_data = {}
        self.location_obj = Location()
        self.flag = 0
        self.txt = ""
        self.image_id = ""
        self.geolocation = ""
        self.telegram_obj = Photo2Down(TOKEN=TOKEN)
        self.ihbar_location = []



    def Start(self,bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text = "Hello Test.")







    def test2(self,bot,update):
        file_id = update.message.photo[2].file_id
        print(file_id)

    def aciklama(self,bot,update): ### aciklama datasini cekiyoruz

        msg = update.message.text
        self.txt = msg
        print(self.txt)

        print("DEbug First ! ")



    def parse_geolocation(self, bot, update):

        geolocation_data = update.message.location  ##setting location
        tmp_ihbar_location = {}#tmp ihbar_location

        self.ihbar_data['latitude'] = geolocation_data["latitude"]
        self.ihbar_data['longitude'] = geolocation_data["longitude"]


        if self.ihbar_data["longitude"] == '' or self.ihbar_data['latitude']:
            ##bot send message
            bot.sendMessage(chat_id=update.message.chat_id, ##validation koordinat data
                            text="Lütfen Konum Bilginizi Doğru Giriniz")

        self.ihbar_data['description'] = self.txt


        url = photo_wrapper.download_and_save(file_id=self.image_id,file_name=str("asdasdasd"))

        try:
            sender.warning_publish(warning_json=self.ihbar_data)
            print("Hnaled")###loggging
        except:
            print("Error")



    def run(self):
        dispatcher.add_handler(MessageHandler(Filters.photo, self.test2))
        aciklama_handler = CommandHandler('aciklama', self.aciklama)

        dispatcher.add_handler(MessageHandler(Filters.location, self.parse_geolocation))

        dispatcher.add_handler(aciklama_handler)

        updater.start_polling()

obj = Test()
th1 = threading.Thread(target=obj.run())