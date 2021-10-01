from datetime import time, date, datetime
import telebot as tg
import sysconfig
import sys
import math
import types

bot = tg.TeleBot("Your Token from BotFather")

#      0      1      2      3      4      5      6      7      8
num = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ']
#      0              1           2            3          4              5          6         7               8           9       10             11             12           13
sub = ['Математика ', 'Русс.яз ', 'Общество ', 'Физика ', 'Литература ', 'Физ-ра ', 'Химия ', 'Информатика ', 'История ', 'ОБЖ ', 'Астрономия ', 'География ',  'Биология ', 'Англ.яз ']
#       0        1         2         3          4         5
type = ['база ', 'проф. ', 'база 1', 'проф. 2', 'база 2', 'проф. 1']
#      0      1      2      3      4      5      6      7      8      9      10     11     12
cab = ['102', '110', '115', '123', '201', '203', '209', '217', '220', '309', '311', '321', '322']
#     0              1                      2          3              4
pc = ['220/201/322', '110/123/201/308/322', '220/102', '220/311/102', '110/123/308/102']
#     0        1        2        3        4        5
cl = ['(10а)', '(10б)', '(10в)', '(11а)', '(11б)', '(11в)']
#      0      1
ili = [' / ', '/']
#     0                     1
pr = ['(проф.Орловой Е.В)', '(проф.Лазепной Е.В)']
#      0матеша база;   1матеша проф;   2общество база; 3общество проф; 4физика база;   5физика проф;   6химия база;    7химия проф;    8история база;  9история проф;  10географ база;  11географ проф;  12биология база; 13биология проф;
pop = [sub[0]+type[0], sub[0]+type[1], sub[2]+type[0], sub[2]+type[1], sub[3]+type[0], sub[3]+type[1], sub[6]+type[0], sub[6]+type[1], sub[8]+type[0], sub[8]+type[1], sub[11]+type[0], sub[11]+type[1], sub[12]+type[0], sub[12]+type[1]]

time = ['1. 8:30 - 9:10 (10) \n', '2. 9:20 - 10:00 (15) \n', '3. 10:15 - 10:55 (15) \n', '4. 11:10 - 11:50 (15) \n', '5. 12:05 - 12:45 (10) \n', '6. 12:55 - 13:35 (25) \n', '7. 14:00 - 14:40 (15) \n', '8. 14:55 - 15:35 (15) \n', '9. 15:50 - 16:30 \n']

########################################################################################################################
day1_10_1 = [num[0] + sub[7] + cab[5]]
day1_10_2 = [num[2] + pop[3] + cab[4] + ili[0] + pop[7] + cab[11]]
day1_10_3 = [num[1] + pop[3] + cab[4] + ili[0] + pop[7] + cab[11]]
day1_10_4 = [num[3] + sub[1] + pc[0]]
day1_10_5 = [num[4] + sub[4] + pc[0]]
day1_10_6 = [num[5] + sub[4] + pc[0]]
day1_10_7 = [num[6] + sub[13] + pc[1]]
day1_10_8 = [num[7] + pop[0] + cab[12] + ili[0] + sub[5] + cab[2] + pr[0]]
day1_10_9 = [num[8] + pop[0] + cab[12] + ili[0] + sub[5] + cab[2] + pr[0]]
day1_10 = []

day2_10_1 = [num[0] + sub[] + cab[]]
day2_10_2 = [num[1] + sub[] + cab[]]
day2_10_3 = [num[2] + sub[] + cab[]]
day2_10_4 = [num[3] + sub[] + cab[]]
day2_10_5 = [num[4] + sub[] + cab[]]
day2_10_6 = [num[5] + sub[] + cab[]]
day2_10_7 = [num[6] + sub[] + cab[]]
day2_10_8 = [num[7] + sub[] + cab[]]
day2_10_9 = [num[8] + sub[] + cab[]]
day2_10 = []

day3_10_1 = [num[0] + sub[] + cab[]]
day3_10_2 = [num[1] + sub[] + cab[]]
day3_10_3 = [num[2] + sub[] + cab[]]
day3_10_4 = [num[3] + sub[] + cab[]]
day3_10_5 = [num[4] + sub[] + cab[]]
day3_10_6 = [num[5] + sub[] + cab[]]
day3_10_7 = [num[6] + sub[] + cab[]]
day3_10_8 = [num[7] + sub[] + cab[]]
day3_10_9 = [num[8] + sub[] + cab[]]
day3_10 = []

day4_10_1 = [num[0] + sub[] + cab[]]
day4_10_2 = [num[1] + sub[] + cab[]]
day4_10_3 = [num[2] + sub[] + cab[]]
day4_10_4 = [num[3] + sub[] + cab[]]
day4_10_5 = [num[4] + sub[] + cab[]]
day4_10_6 = [num[5] + sub[] + cab[]]
day4_10_7 = [num[6] + sub[] + cab[]]
day4_10_8 = [num[7] + sub[] + cab[]]
day4_10_9 = [num[8] + sub[] + cab[]]
day4_10 = []

day5_10_1 = [num[0] + sub[] + cab[]]
day5_10_2 = [num[1] + sub[] + cab[]]
day5_10_3 = [num[2] + sub[] + cab[]]
day5_10_4 = [num[3] + sub[] + cab[]]
day5_10_5 = [num[4] + sub[] + cab[]]
day5_10_6 = [num[5] + sub[] + cab[]]
day5_10_7 = [num[6] + sub[] + cab[]]
day5_10_8 = [num[7] + sub[] + cab[]]
day5_10_9 = [num[8] + sub[] + cab[]]
day5_10 = []

#======================================================================================================================#

day1_11_1 = [num[0] + sub[] + cab[]]
day1_11_2 = [num[1] + sub[] + cab[]]
day1_11_3 = [num[2] + sub[] + cab[]]
day1_11_4 = [num[3] + sub[] + cab[]]
day1_11_5 = [num[4] + sub[] + cab[]]
day1_11_6 = [num[5] + sub[] + cab[]]
day1_11_7 = [num[6] + sub[] + cab[]]
day1_11_8 = [num[7] + sub[] + cab[]]
day1_11_9 = [num[8] + sub[] + cab[]]
day1_11 = []

day2_11_1 = [num[0] + sub[] + cab[]]
day2_11_2 = [num[1] + sub[] + cab[]]
day2_11_3 = [num[2] + sub[] + cab[]]
day2_11_4 = [num[3] + sub[] + cab[]]
day2_11_5 = [num[4] + sub[] + cab[]]
day2_11_6 = [num[5] + sub[] + cab[]]
day2_11_7 = [num[6] + sub[] + cab[]]
day2_11_8 = [num[7] + sub[] + cab[]]
day2_11_9 = [num[8] + sub[] + cab[]]
day2_11 = []

day3_11_1 = [num[0] + sub[] + cab[]]
day3_11_2 = [num[1] + sub[] + cab[]]
day3_11_3 = [num[2] + sub[] + cab[]]
day3_11_4 = [num[3] + sub[] + cab[]]
day3_11_5 = [num[4] + sub[] + cab[]]
day3_11_6 = [num[5] + sub[] + cab[]]
day3_11_7 = [num[6] + sub[] + cab[]]
day3_11_8 = [num[7] + sub[] + cab[]]
day3_11_9 = [num[8] + sub[] + cab[]]
day3_11 = []

day4_11_1 = [num[0] + sub[] + cab[]]
day4_11_2 = [num[1] + sub[] + cab[]]
day4_11_3 = [num[2] + sub[] + cab[]]
day4_11_4 = [num[3] + sub[] + cab[]]
day4_11_5 = [num[4] + sub[] + cab[]]
day4_11_6 = [num[5] + sub[] + cab[]]
day4_11_7 = [num[6] + sub[] + cab[]]
day4_11_8 = [num[7] + sub[] + cab[]]
day4_11_9 = [num[8] + sub[] + cab[]]
day4_11 = []

day5_11_1 = [num[0] + sub[] + cab[]]
day5_11_2 = [num[1] + sub[] + cab[]]
day5_11_3 = [num[2] + sub[] + cab[]]
day5_11_4 = [num[3] + sub[] + cab[]]
day5_11_5 = [num[4] + sub[] + cab[]]
day5_11_6 = [num[5] + sub[] + cab[]]
day5_11_7 = [num[6] + sub[] + cab[]]
day5_11_8 = [num[7] + sub[] + cab[]]
day5_11_9 = [num[8] + sub[] + cab[]]
day5_11 = []

########################################################################################################################

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Здравствуй, приятно с тобой познакомиться. Если нужна будет помощь по работе со мной, то просто напиши мне /help и я тебе все объясню')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, f'Мои команды: \n \n' + '/about - что-то обо мне \n' + '10 - расписание 10-го класса \n' + '11 - расписание 11-го класса \n' + "звонки - список всех звонков" )

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, f'Я - бот, который умеет отправлять расписание, если тебе будет нужна помощь по командам, напиши /help, и я отправлю список команд, которые я понимаю')

@bot.message_handler(content_types=['text'])
def send_about(message):
    if message.text.lower() == '10':
        if date.today().weekday() == 0:
            bot.send_message(message.chat.id, day1_10)
        if date.today().weekday() == 1:
            bot.send_message(message.chat.id, day1_10)
        if date.today().weekday() == 2:
            bot.send_message(message.chat.id, day1_10)
        if date.today().weekday() == 3:
            bot.send_message(message.chat.id, day1_10)
        if date.today().weekday() == 4:
            bot.send_message(message.chat.id, day1_10)

    elif message.text.lower() == '11':
        if date.today().weekday() == 0:
            bot.send_message(message.chat.id, day1_11)
        if date.today().weekday() == 1:
            bot.send_message(message.chat.id, day1_11)
        if date.today().weekday() == 2:
            bot.send_message(message.chat.id, day1_11)
        if date.today().weekday() == 3:
            bot.send_message(message.chat.id, day1_11)
        if date.today().weekday() == 4:
            bot.send_message(message.chat.id, day1_11)

    elif message.text.lower() == 'звонки':
        bot.reply_to(message, "".join(time))

    else:
        bot.send_message(message.from_user.id, 'Ошибка, я не понял запроса. Пожалуйста, повторите ещё раз')

# Обязательное условие!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
bot.polling(none_stop=True)