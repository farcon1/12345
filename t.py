from threading import Thread
import telebot 
from telebot import types
bot=telebot.TeleBot('1292714271:AAFto5D4qOOmTbRDfYVY28DQguWr3FJWKlc')   #бот для принятия анкет и для отправки других
bot_checker = telebot.TeleBot('1147234538:AAHFUcJE44cGiFFBISV5YCtK8TggG2Jf9ps') #бот для проверки анкет

@bot.message_handler(content_types=['text'])
def get_start_message(message):
    if message.text == '/start':  #начало диалога с клиентом
        bot.send_message(message.from_user.id,"Работает на телефоне в termux")
@bot_checker.message_handler(content_types=['text'])
def get_start_message1(message):
    if message.text == '/start':  #начало диалога с клиентом
        bot.send_message(message.from_user.id,"Работает на телефоне в termux")
        
thread1 = Thread(target=bot.polling, args=())
thread2 = Thread(target=bot_checker.polling, args=())
thread1.start()
thread2.start()
thread1.join()
thread2.join()