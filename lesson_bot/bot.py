from datetime import date as dt
from datetime import time as tm
import telebot as tg
import config
import time
import json

bot = tg.TeleBot(config.token_test)

with open('lessons.json', 'r') as j:
    data = json.load(j)

today = dt.today().weekday()
yesterday = today - 1
tomorrow = today + 1

lesson = data[''.join('lessons')]

def get_time_table_today(cls_num, day='today'):
    for t in data[str(cls_num)]:
        res = t[str(today)]
    return ''.join(res)

def get_time_table_tomorrow(cls_num, day='tomorrow'):
    for t in data[str(cls_num)]:
        res = t[str(tomorrow)]
    return ''.join(res)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Здравствуй, приятно с тобой познакомиться. Если нужна будет помощь по работе со мной, то просто напиши мне /help и я тебе все объясню')


@bot.message_handler(content_types=['text'])
def send_lessons(message):
    if message.text.lower() == '10':
        bot.send_message(message.chat.id, get_time_table_today(10))
    elif message.text.lower() == 'завтра 10':
        bot.send_message(message.chat.id, get_time_table_tomorrow(10))

    elif message.text.lower() == '11':
        bot.send_message(message.chat.id, get_time_table_today(11))
    elif message.text.lower() == 'завтра 11':
        bot.send_message(message.chat.id, get_time_table_tomorrow(11))

    elif message.text.lower() == 'time':
        bot.send_message(message.chat.id, lesson)

    else:
        bot.reply_to(message, 'Error')


def telegram_polling():
    try:
        bot.polling()
    except:
        traceback_error_string = traceback.format_exc()
        with open("Error.log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime(
                "%c") + "\r\n<<ERROR polling>>\r\n" + traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

telegram_polling()