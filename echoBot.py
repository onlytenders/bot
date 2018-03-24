import telebot
import lolkek

print("lol")

token = "325324074:AAH2sjtsU4DRNz6R15U6zzkktzVqzCpUjuk"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types = ["text"])
def check_message(message):
    if message.text == "Список студентов" :
        for student in lolkek.getStudentsList():            
            bot.send_message(message.chat.id, student[0])
    elif message.text == "Оценка" :
        bot.send_message(message.chat.id, lolkek.getMediumMarks())
    elif message.text.isdigit():
        bot.send_message(message.chat.id, "Имя: " + lolkek.getStudentByNumber(int(message.text))[0])
        bot.send_message(message.chat.id, "Оценка: " + str(lolkek.getStudentByNumber(int(message.text))[1]))
    else:
        bot.send_message(message.chat.id, "Такой команды нет")
bot.polling(none_stop=True)
