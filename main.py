#!/usr/bin/python

import telebot
import GetRandomNumber as grn
from pyTelegramBotAPI.telebot import types

API_TOKEN = '5609895910:AAGgizUnGZayS13VMfvuwpWfmt8HE2QqN0k'

bot = telebot.TeleBot(API_TOKEN)


# Handles '/start', 'help'...
@bot.message_handler(commands=['start'])
def send_message(message):
    mess = f"""
        Hi {message.from_user.first_name} {message.from_user.last_name}!,
        I'm Emijah_Random_Bot.
        I'm offering random numbers to anyone on the telegram.
        Use /help to get list of available commands.
        """
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def send_message(message):
    help_message = '''
    This telegram bot will give u random number from any range u pick.
    USE:
    /random_number_100 to get random number from 1 to 100
    /random_number_1000 to get number from 1 to 1000
    /random_number to get random number in your range
    '''
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('random_number_100')
    itembtn2 = types.KeyboardButton('random_number_1000')
    markup.add(itembtn1, itembtn2)

    bot.send_message(message.chat.id, help_message, reply_markup=markup)

@bot.message_handler()
def get_random_number(message):
    random_number_100 = grn.random_100()
    random_number_1000 = grn.random_1000()
    if message.text == 'random_number_100':
       bot.send_message(message.chat.id, random_number_100)
    elif message.text == 'random_number_1000':
        bot.send_message(message.chat.id, random_number_1000)

@bot.message_handler(commands=['random_number_100'])
def get_random_number_100(message):
    random_number = grn.random_100()
    bot.send_message(message.chat.id, random_number)
@bot.message_handler(commands=['random_number_1000'])
def get_random_number_1000(message):
    random_number = grn.random_1000()
    bot.send_message(message.chat.id, random_number)


bot.infinity_polling()
