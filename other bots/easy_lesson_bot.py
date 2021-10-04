import telebot
import random
 
from telebot import types
 
bot = telebot.TeleBot('token')
 
@bot.message_handler(commands=['start'])
def welcome(message):
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("Расписание 10а")
    item3 = types.KeyboardButton("Расписание 11а")
 
    markup.add(item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - бот созданный чтобы отправлять Вам расписание 10а и 11а классов.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        # if message.text == '🎲 Рандомное число':
        #     bot.send_message(message.chat.id, str(random.randint(0,19)))
        if message.text == 'Расписание 10а':
 
            markup = types.InlineKeyboardMarkup(row_width=3)
            monday_10 = types.InlineKeyboardButton("Пн", callback_data='Mo10')
            tuesday_10 = types.InlineKeyboardButton("Вт", callback_data='Tu10')
            wednesday_10 = types.InlineKeyboardButton("Ср", callback_data='We10')
            thursday_10 = types.InlineKeyboardButton("Чт", callback_data='Th10')
            friday_10 = types.InlineKeyboardButton("Пт", callback_data='Fr10')

            markup.add(monday_10, tuesday_10, wednesday_10, thursday_10, friday_10)
 
            bot.send_message(message.chat.id, 'Какой день интересует?', reply_markup=markup)

        elif message.text == 'Расписание 11а':

            markup = types.InlineKeyboardMarkup(row_width=3)
            monday_11 = types.InlineKeyboardButton("Пн", callback_data='Mo11')
            tuesday_11 = types.InlineKeyboardButton("Вт", callback_data='Tu11')
            wednesday_11 = types.InlineKeyboardButton("Ср", callback_data='We11')
            thursday_11 = types.InlineKeyboardButton("Чт", callback_data='Th11')
            friday_11 = types.InlineKeyboardButton("Пт", callback_data='Fr11')

            markup.add(monday_11, tuesday_11, wednesday_11, thursday_11, friday_11)

            bot.send_message(message.chat.id, 'Какой день интересует?', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Mo10':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Пн:\n1. Информатика 203 \n2. Право 201 \n3. Экономика 201 \n4. Русс.яз 220 \n5. Литература 220 \n6. Литература 220 \n7. Англ.яз 322 \n8. Информатика 203')

            elif call.data == 'Tu10':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Вт:\n1. Математика проф. 201/322 \n2. __ \n3. __ \n4. Общество проф. 322 \n5. Общество проф. 322 \n6. Химия 322 \n7. История 201 \n8. Физ-ра 115 \n9. Физ-ра 115')

            elif call.data == 'We10':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Ср:\n1. __ \n2. __ \n3. Русс.яз 220 \n4. Русс.яз 220 \n5. Математика 322 \n6. Математика 322 \n7. Литература 220')

            elif call.data == 'Th10':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Чт:\n1. __ \n2. Математика 322 \n3. Математика 322 \n4. Астрономия 220 \n5. ОБЖ 220 \n6. __ \n7. Физика 322 \n8. Физика 322 \n9. Физика 322')

            elif call.data == 'Fr10':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Пт:\n1. Математика 322 \n2. Математика 322 \n3. Англ.яз 322 \n4. Англ.яз 322 \n5. __ \n6. История(1) 201 \n7. Биология')



            elif call.data == 'Mo11':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Пн:\n1. __ \n2. __ \n3. __ \n4. Информатика 203 \n5. __ \n6. География 311 \n7. История ?')

            elif call.data == 'Tu11':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Вт:\n1. Русс.яз 220 \n2. Математика 102 \n3. Математика 102 \n4. Литература 220 \n5. Литература 220 \n6. Англ.яз 110 \n7. Англ.яз 110 \n8. Физ-ра 115 \n9. Физ-ра 115')

            elif call.data == 'We11':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Ср:\n1. Математика 102 \n2. Общество 311 \n3. Общество 311 \n4. Физика 102 \n5. Физика 102 \n6. Химия 311 \n7. История 102 \n8. ОБЖ 102')

            elif call.data == 'Th11':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Чт:\n1. __ \n2. __ \n3. __ \n4. Математика 102 \n5. Математика 102')

            elif call.data == 'Fr11':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лови", reply_markup=None)
                bot.send_message(call.message.chat.id, 'Пт:\n1. Русс.яз 220 \n2. Русс.яз 220 \n3. Математика 102 \n4. Математика 102 \n5. Литература 220 \n6. Биология 311 \n7. Англ.яз 110')

            # # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #     text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")


    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
