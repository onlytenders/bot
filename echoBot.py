import telebot
import requests
from datetime import datetime
from telebot import types

print("lol")

token = "518178480:AAHNjdNIAHBfJrPZGfJNTBTPLccNGvj1knQ"

bot = telebot.TeleBot(token)

def getTimeNow():
    return datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')

def writeToLog(who, text):
    file = open("log.history", "a+", encoding="utf-8")
    file.write(getTimeNow()+" "+str(who)+" "+text+'\n')
    file.close()
    

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "你好，朋友！")
    writeToLog(message.from_user.id, 'Started using this bot')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    translateButton = types.KeyboardButton("Translate the word")
    keyboard.add(translateButton)
    meanButton = types.KeyboardButton("Learn the meaning of the word")
    keyboard.add(meanButton)
    courseButton = types.KeyboardButton("Learn the course dollar-tenge")
    keyboard.add(courseButton)
    bot.send_message(message.chat.id, "Choose the option: ", reply_markup=keyboard)

try:   
    bot.polling(none_stop=True)
except:
    writeToLog('bot', 'Starting error')










