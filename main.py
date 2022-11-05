#!/usr/bin/python

import telebot

API_TOKEN ='5609895910:AAGgizUnGZayS13VMfvuwpWfmt8HE2QqN0k'

bot = telebot.TeleBot(API_TOKEN)

#Handles '/start', 'help'...
@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    bot.send_message(message.chat.id, """
        <b>Hi everyone, I'm Emijah_Random_Bot.
        I'm offering random numbers to anyone on the telegram.
        </b>""", parse_mode='html' )




bot.infinity_polling()