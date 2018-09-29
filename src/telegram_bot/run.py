import telebot
from src import constants
from src.telegram_bot import bot_service
from src.data_manager import data_manipulator
from src.db_guard.user_manager import user_adder
from src.db_guard.access_granter import id_checker
bot = telebot.TeleBot(constants.BOT_TOKEN)
bot_service.create_db_conn("../../db/users.db")


@bot.message_handler(commands = ['login'])
def login(message):
    result = user_adder.sign_in(message)
    bot.send_message(message.chat.id, result)
    
@bot.message_handler(commands = ['start'])
def welcome(message):
    bot.send_message(message.chat.id, constants.WELCOME_MESSAGE%message.from_user.first_name)
    
@bot.message_handler(commands = ['help'])
def helper(message):
    bot.send_message(message.chat.id, constants.HELP_MESSAGE)
    
@bot.message_handler(commands = ['contact'])
def contact(message):
    bot.send_message(message.chat.id, constants.CONTACT_INFO)
    
@bot.message_handler(commands = ['scrape'])
def scrape(message):
    user_id = message.chat.id
    if not id_checker.check_id(user_id):
        bot.send_message(message.chat.id, constants.ACCESS_DENIED)
        return 
    return bot.send_document(user_id, bot_service.get_mobile_data(bot.send_message, user_id))   

@bot.message_handler(commands=['archive'])
def show_archive(message):
    bot.send_message(message.chat.id, constants.ARCHIVE_MESSAGE)
    for file in data_manipulator.show_archive():
        bot.send_message(message.chat.id, file)
        
@bot.message_handler(commands=['compare'])
def compare(message):
    user_id = message.chat.id
    if not id_checker.check_id(user_id):
        bot.send_message(message.chat.id, constants.ACCESS_DENIED)
        return 
    output = data_manipulator.compare_data(message.text)
    if isinstance(output, str):
        bot.send_message(user_id, output)    
    else:
        bot.send_document(user_id, output)
        
@bot.message_handler(func = lambda m: True)
def echo_all(message):
    bot.reply_to(message, constants.HELP_MESSAGE)
    
bot.polling(none_stop=True,interval=0,timeout=1000)
