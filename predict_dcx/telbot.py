import json
import telegram

class TelNotificaion():
    token = ['5056219233:AAEudQXh4nwCF5JGLzGXizcnuLiKPV70yMs','5037761473:AAG6My2nXsO6lAdkurSyngF8nEPTgPBoZB0', '5024531672:AAGZ-6fbW3NwzIWtbU0LpvimWcY0X6sFjYM', '5011307168:AAEjh-3E4pgUijknXT6iYJZnTPgsHR2u2bo']
    chat_id = ['487433499','889544431', '416829571', '1006540215']
    bot = telegram.Bot(token=token[0])
    bot1 =  telegram.Bot(token=token[1])
    bot2 =  telegram.Bot(token=token[2])
    bot3 =  telegram.Bot(token=token[3])

    def notify_ending(self,message):
        self.bot.sendMessage(chat_id=self.chat_id[0], text=message)
        self.bot1.sendMessage(chat_id=self.chat_id[1], text=message)
        self.bot2.sendMessage(chat_id=self.chat_id[2], text=message)
        self.bot3.sendMessage(chat_id=self.chat_id[3], text=message)

# notify = TelNotificaion()
# notify.notify_ending("hii this is sagar")


