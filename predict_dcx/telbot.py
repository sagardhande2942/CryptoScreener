import json
import telegram

class TelNotificaion():
    token = ['5056219233:AAEudQXh4nwCF5JGLzGXizcnuLiKPV70yMs','5037761473:AAG6My2nXsO6lAdkurSyngF8nEPTgPBoZB0']
    chat_id = ['487433499','889544431']
    bot = telegram.Bot(token=token[0])
    bot1 =  telegram.Bot(token=token[1])

    def notify_ending(self,message):
        self.bot.sendMessage(chat_id=self.chat_id[0], text=message)
        self.bot1.sendMessage(chat_id=self.chat_id[1], text=message)

notify = TelNotificaion()
notify.notify_ending("hii this is sagar")


