import telebot as tg
import json

bot = tg.TeleBot('2013015491:AAHpuV0ToVFOvXIp4MBBUoSrSyxfutzA7M0')

with open('num1.json', 'r') as j:
    data = json.load(j)

for person in data['people']:
    lol = person['name']
    kek = person['phone']
    cheburek = person['emails'][0]
    cheburec = person['emails'][1]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Здравствуй, приятно с тобой познакомиться. Если нужна будет помощь по работе со мной, то просто напиши мне /help и я тебе все объясню')


@bot.message_handler(content_types=['text'])
def send_lessons(message):
    if message.text.lower() == '10':
        bot.send_message(message.chat.id, lol)
        bot.send_message(message.chat.id, kek)
        bot.send_message(message.chat.id, cheburek)
        bot.send_message(message.chat.id, cheburec)


bot.polling(none_stop=True)