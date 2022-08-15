# -*- coding: utf-8 -*-

import telebot
import time
from keyboa.keyboards import keyboa_maker

import admin
import text_file
import config
import weather
from config import TOKEN


mes_info = ""
mes_img = ""
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # users = game_db.db_start(message.chat.id)
    fruits_with_ids = [
        {"Старт": "start"}, {"Мои очки": "score"},
        {"Погода": "weather"}, {"BAZA": "baza"}, {"Запись": "zapis"}]
    kb_fruits = keyboa_maker(items=fruits_with_ids, items_in_row=2)
    textsend = message.chat.first_name + " Хай :) нажми на кнопку"
    bot.send_message(chat_id=message.chat.id, reply_markup=kb_fruits, text=textsend)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global time_start
    time_start = int(time.time())
    print(f'Time start {time_start}')
    if call.data == "start":
        """
        Приветствие картинка1 + текст2
        bot.send_photo(ид_получателя, open('/путь/к/картинке.jpg', 'rb'));
        bot.send_photo(ид_получателя, 'https://example.org/адрес/картинки.jpg');
        """
        bot.send_photo(call.message.chat.id, open('static/hello.jpg', 'rb'))
        time.sleep(1)
        button = [{"НАЧАТЬ КУРС": "start_kurs"}]
        kb_fruits = keyboa_maker(items=button, items_in_row=2)
        bot.send_message(call.message.chat.id, reply_markup=kb_fruits, text=text_file.text_1, parse_mode="html")
    elif call.data == "score":
        if config.is_admin(call.message.chat.id) and config.admin_mode == True:
            print(call.message.chat.id)
            msg = bot.send_message(call.message.chat.id, f'Пожалуйста введите текст: ')
            bot.register_next_step_handler(msg, message_db)
        else:
            bot.send_message(call.message.chat.id, "No admin")
    elif call.data == "baza":
        if config.is_admin(call.message.chat.id) and config.admin_mode == True:
            print(call.message.chat.id)
            bot.send_message(call.message.chat.id, admin.db_created_table_art())
        else:
            bot.send_message(call.message.chat.id, "No admin")
    elif call.data == "start_kurs":
        print(call.message.chat.id, call.data)
        video = open('static/video_1.mp4', 'rb')
        bot.send_video(call.message.chat.id, video, timeout=2)
    elif call.data == "weather":
        print(call.message.chat.id, call.data)
        bot.send_message(call.message.chat.id, weather.weather())


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id
        file_info_1 = bot.get_file(message.photo[-1].file_id)
        bot.send_message(message.chat.id, str(file_info_1))
        downloaded_file = bot.download_file(file_info_1.file_path)

        src = dir + '\\' + file_info_1.file_path.split('/')[-1]
        bot.send_message(message.chat.id, src)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        print("photo ok")
    except Exception as e:
        bot.reply_to(message, e)


def message_db(message):
    global mes_info
    mes_info = message.text
    msg = bot.send_message(message.chat.id, f'Пожалуйста отправьте картинку')
    bot.register_next_step_handler(msg, send_img)

def send_img(message):
    global mes_img
    mes_img = message.text
    bot.send_message(message.chat.id, mes_info)
    bot.send_photo(message.chat.id, mes_info)






def zapis_date(message):
    global zap_d
    msg = bot.send_message(message.chat.id, f'Пожалуйста введите удобное для Вас дату записи в формате 01.01. ')
    bot.register_next_step_handler(msg, zapis_time)


def zapis_time(message):
    global zap_t
    print(f"Zapis: ")


if __name__ == "__main__":
    try:
        print("Start Bot")
        bot.polling(none_stop=True, interval=0)
    except:
        print("STOP")
