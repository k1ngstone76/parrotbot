import telebot
import os

Token = os.environ.get("TOKEN")


bot = telebot.TeleBot(Token)


@bot.message_handler(content_types=['text'])
def lalal(message):
    str(message.text)
    message.text2 = message.text[::-1]
    bot.send_message(message.chat.id, message.text2)


bot.polling(none_stop=True)
