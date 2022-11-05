#!/usr/bin/python

import telebot

API_TOKEN = '5609895910:AAGgizUnGZayS13VMfvuwpWfmt8HE2QqN0k'

bot = telebot.TeleBot(API_TOKEN)


# Handles '/start', 'help'...
@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    mess = f"""
        Hi {message.from_user.first_name} {message.from_user.last_name}!,
        I'm Emijah_Random_Bot.
        I'm offering random numbers to anyone on the telegram.
        Use /help to get list of available commands.
        """

    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.infinity_polling()
