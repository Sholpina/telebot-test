
import telebot
import time
bot = telebot.TeleBot("5727680214:AAEG3EOoAhZOq74WrH7a2jHgewpvylDQ1ik")

# print(telebot.TeleBot.__dict__)
#
# for attribute, value in (bot.__dict__.items()):
#     print(attribute, '=', value)

# see all methods of class

# print(dir(bot))
# for method in enumerate((dir(bot))):
#     print(method)


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# Обрабатывает все отправленные документы и аудиофайлы
# @bot.message_handler(content_types=['text']])
# def handle_message(message):
#     bot.send_location(
#         r"https://api.telegram.org/bot['5727680214:AAEG3EOoAhZOq74WrH7a2jHgewpvylDQ1ik']/sendlocation?chat_id=[UserID]&latitude=51.6680&longitude=32.6546")
# @bot.message_handler(content_types=['text'])
# def answer_q1(message):
#     bot.send_message(
#         message.chat.id, "Добро пожаловать к нам, чем можем вам помочь?")
answers_en = ["hello", "good day"]
answers_az = ["salam"]
answers_ru = ["привет", "здравствуйте",
              "доброе утро", "добрый день", "добрый вечер", "доброго времени суток"]
answers_other = ["merhaba", "gamarjoba"]


@bot.message_handler(content_types=['text'])
def ans(message):
    t = time.ctime(time.time()).split()
    mess = message.text.lower()
    if mess[-1] == '?' or "!":
        mess = mess[:-1]
    if mess in answers_ru or mess == '/start':
        ans = "Здравствуйте! Чем можем вам помочь?"
    elif mess in answers_az or mess == '/start':
        ans = "Salam, Sizə necə kömək edə bilərəm?"
    elif mess in answers_en or mess == '/start':
        ans = "Welcome, how can i help you?"
    elif mess in answers_other or mess == '/start':
        ans = "Merhaba size nasıl yardımcı olabiliriz"
    elif mess == "сколько времени":
        ans = "Current time is : " + t[-2]
    elif mess == "какое сегодня число":
        ans = "Сегодняшнее число: " + t[2] + " " + t[1] + " " + t[4]
    else:
        ans = "???"
    bot.send_message(message.chat.id, ans)


if __name__ == '__main__':
    bot.infinity_polling()
