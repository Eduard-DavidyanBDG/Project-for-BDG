import telebot
from telebot import types
import config2
# from ProjectPython import data_tasks
from data_tasks import *

bot = telebot.TeleBot(token=config2.config["token"])


class Bot:
    def message(self):
        return "Hi, i'm a Bot For your course and i can give" \
               " you more interesting lessons about different topics" \
               "if you didn't know the commands please type - /help"

    def Choose_tasks(self):
        return "Please choose the topic you want"

    def help(self):
        return "At this moment commands is - /get_tasks, /stop"

    def Stop(self):
        return bot.stop_bot()


if __name__ == '__main__':
    B = Bot()


    @bot.message_handler(commands=["start"])
    def Hello(message):
        bot.send_message(message.chat.id, B.message())


    @bot.message_handler(commands=["help"])
    def Help(message):
        bot.send_message(message.chat.id, B.help())


    @bot.message_handler(commands=["stop"])
    def stop(message):
        bot.send_message(message.chat.id, "i'm off")


    @bot.message_handler(commands=["get_tasks"])
    def Choose_tasks(message):
        reply_markup = types.InlineKeyboardMarkup()
        item_1 = types.InlineKeyboardButton(text="Expressions", callback_data="Expressions")
        item_2 = types.InlineKeyboardButton(text="Loops", callback_data="Loops")
        item_3 = types.InlineKeyboardButton(text="Functions", callback_data="Functions")
        item_4 = types.InlineKeyboardButton(text="List", callback_data="List")
        item_5 = types.InlineKeyboardButton(text="Exceptions and Files", callback_data="Exceptions and Files")
        item_6 = types.InlineKeyboardButton(text="Classes", callback_data="Classes")
        reply_markup.add(item_1, item_2, item_3, item_4, item_5, item_6)
        bot.send_message(message.chat.id, B.Choose_tasks(), reply_markup=reply_markup)


    @bot.callback_query_handler(func=lambda call: True)
    def Answer(call):
        global count, topic
        if call.data == "Expressions":
            topic = Expressions
            count = 0
            for item in Expressions.keys():
                count = item
            bot.send_message(call.message.chat.id, f"At this moment i have {count} tasks, how much do you want??")
        elif call.data == "Loops":
            topic = Loops
            count = 0
            for item in Loops.keys():
                count = item
            bot.send_message(call.message.chat.id, f"At this moment i have {count} tasks, how much do you want??")
        elif call.data == "Functions":
            topic = Functions
            count = 0
            for item in Functions.keys():
                count = item
            bot.send_message(call.message.chat.id, f"At this moment i have {count} tasks, how much do you want??")
        elif call.data == "List":
            topic = List
            count = 0
            for item in List.keys():
                count = item
            bot.send_message(call.message.chat.id, f"At this moment i have {count} tasks, how much do you want??")
        elif call.data == "Exceptions and Files":
            topic = Exceptions_and_Files
            count = 0
            for item in Exceptions_and_Files.keys():
                count = item
            bot.send_message(call.message.chat.id, f"At this moment i have {count} tasks, how much do you want??")
        elif call.data == "Classes":
            topic = Classes
            count = 0
            for item in Classes.keys():
                count = item
            bot.send_message(call.message.chat.id, f"At this moment i have {count} tasks, how much do you want??")


    @bot.message_handler(content_types=["text"])
    def ans_tasks(message):
        count_tasks = message.text
        for item in range(1, count + 1):
            if item > int(count_tasks):
                break
            else:
                bot.send_message(message.chat.id, f"{item}-{topic[item]}")


    bot.polling(none_stop=True, interval=0)
