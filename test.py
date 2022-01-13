import json
import telegram

def notify_ending(message):
    token = '5056219233:AAEudQXh4nwCF5JGLzGXizcnuLiKPV70yMs'
    chat_id = '487433499'
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)


notify_ending("hii this is sagar")


