import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config
from telebot import types

TOKEN = "1892952559:AAFIyjUT1h-IPoM6jZJH2yT7ev29YApaSyE"
bot = telebot.TeleBot(token=TOKEN)

API_Key = "87395221864d4fa7a9319a0afc33b986"
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM(API_Key, config_dict)


class Bot():
    def massage(self):
        return "Hi, user Eduard"

    def owmprocess(self):
        return "Which City do you want??"


if __name__ == '__main__':
    @bot.message_handler(commands=["info"])
    def ask(message):
        reply_markup = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text="Yes", callback_data="yes")
        item_no = types.InlineKeyboardButton(text="No", callback_data="no")
        reply_markup.add(item_yes, item_no)
        bot.send_message(message.chat.id, "Do you want to know something about you?",
                         reply_markup=reply_markup)


    @bot.message_handler(commands=["start"])
    def starter(message):
        b = Bot()
        bot.send_message(message.chat.id, b.massage())


    @bot.message_handler(commands=["weather"])
    def owmstarter(message):
        b = Bot()
        bot.send_message(message.chat.id, b.owmprocess())


    @bot.callback_query_handler(func=lambda call: True)
    def ask2(call):
        if call.data == "yes":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_ID = types.KeyboardButton("ID")
            item_Name = types.KeyboardButton("Name")
            markup_reply.add(item_ID, item_Name)
            bot.send_message(call.message.chat.id, "Put button", reply_markup=markup_reply)
        elif call.data == "no":
            bot.send_message(call.message.chat.id, "Ok, Bye")


    @bot.message_handler(content_types=['text'])
    def message(message):
        if message.text == "ID":
            bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}")
        elif message.text == "Name":
            bot.send_message(message.chat.id,
                             f"Your Name: {message.from_user.first_name} {message.from_user.last_name}")
        else:
            text = message.text
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(text)
            weather = observation.weather
            weather1 = weather.temperature('celsius')["temp"]
            weather = observation.weather.detailed_status
            bot.send_message(message.chat.id, f"Сейчас {weather} \nTemp: {weather1}°")


    bot.polling(none_stop=True)
