import os
from telebot import telebot
from telebot import types
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


BOT_TOKEN=BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
HELP_TEXT= """help text"""

button_example= types.InlineKeyboardButton('Help', callback_data='help')
#button_time=types.InlineKeyboardButton('Time', callback_data=datetime.now())
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button_example)

#keyboard.add(button_time)


@bot.message_handler(commands=['get_menu'])
def get_menu(message):
    bot.send_message(message.chat.id, text='Keyboard', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data=="help" )
def button_help_pressed(call: types.CallbackQuery):
    bot.send_message(call.message.chat.id, HELP_TEXT)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello")


@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, "HI!")
    
    
    
@bot.message_handler(commands=['help'])
def send_help(message):
   bot.send_message(message.chat.id, HELP_TEXT)
    

@bot.message_handler(commands=['example'])
def send_example(message):
     bot.send_message(message.chat.id, 'meow')
    

@bot.message_handler(commands=['time'])
def send_current_time(message):
    bot.send_message(message.chat.id, datetime.now() )
    
    
bot.polling(True)