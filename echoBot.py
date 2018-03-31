import telebot
import lolkek

print("lol")

token = "325324074:AAH2sjtsU4DRNz6R15U6zzkktzVqzCpUjuk"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types = ["text"])
def check_message(message):
    personInfo = {'Rakhat':'+77016738924',
                          'Vlad':'+77758426915',
                          'Oleg':'+77018539424',
                          'Viktor':'+77777777777'}
    lolilikek = message.text
    lolilikek = lolilikek.lower()
    try:
        bot.send_message(message.chat.id, personInfo[lolilikek])
    except:
        bot.send_message(message.chat.id, 'i ne lol i ne kek')
bot.polling(none_stop=True)
