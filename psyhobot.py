#version start

import random
import sqlite3
import telebot
import datetime, time
from keyboa.keyboards import keyboa_maker
from telebot import types
from telebot import TeleBot
import text_file


bot = telebot.TeleBot('1450495246:AAGQxl6uESY-VtdXJI9Uj-pLipCP7sSQfWg')


@bot.message_handler(commands=['start'])
def start(message):
    # users = game_db.db_start(message.chat.id)
    fruits_with_ids = [
        {"Старт": "start"}, {"Мои очки": "score"},
        {"Информация": "info"}, {"Викторина": "victorina"}, {"Запись": "zapis"}]
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
        print(call.message.chat.id)
        bot.send_message(call.message.chat.id, """
       <b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=91124946">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
       """, parse_mode="html")
    elif call.data == "start_kurs":
        print(call.message.chat.id, call.data)
        video = open('static/video_1.mp4', 'rb')
        bot.send_video(call.message.chat.id, video, timeout=2)

#     elif call.data == "info":
#         bot.send_message(call.message.chat.id, f'Info')
#     elif call.data == "victorina":
#         game_vic = game_victor.random_line()
#         print(type(game_vic))
#         game_start = game_vic.split("|")
#         print(game_start)
#         question = game_start[0]
#         answer = game_start[1].strip("")
#         msg = bot.send_message(call.message.chat.id, f'Внимание вопрос {question} - {answer}')
#         bot.register_next_step_handler(msg, victorina, game_vic)
#     elif call.data == "zapis":
#         print(f"Zapis {call.message.chat.id}")
#         bot.send_message(call.message.chat.id, f'Пожалуйста введите удобное '
#                                                f'для Вас дату записи в формате 01.01. {order.a}')
#
#
# def zapis(message):
#     msg = order.order.a
#     bot.send_message(message.chat.id, f'{msg}')


# def start_game(message, rand):
#     global score_game, time_finish
#     try:
#         a = int(message.text)
#         b = rand
#         print(b)
#         if a > b:
#             score_game -= 1
#             msg = bot.send_message(message.chat.id, f'Down, Ваши очки {score_game}')
#             bot.register_next_step_handler(msg, start_game, b)
#         elif a < b:
#             score_game -= 1
#             msg = bot.send_message(message.chat.id, f'UP, Ваши очки {score_game}')
#             bot.register_next_step_handler(msg, start_game, b)
#         elif a == b:
#             time_finish = int(time.time())
#             time_game = time_finish - time_start
#             print(f"{time_finish} - {time_start} ")
#             score_game += 5
#             game_db.db_score_add(message.chat.id, score_game, time_game)
#             fruits_with_ids = [
#                 {"Старт": "start"}, {f"Список игр": "list_game"},
#                 {"Информация": "info"}, {"Score": "score"}, ]
#             kb_fruits = keyboa_maker(items=fruits_with_ids, items_in_row=1)
#             textsend = message.chat.first_name + f"Ты выиграл {score_game} за {time_game} секунд, может еще поиграем?"
#             bot.send_message(chat_id=message.chat.id, reply_markup=kb_fruits, text=textsend)
#     except:
#         msg = bot.send_message(message.chat.id, f'Соори, это же не число: {message.text}, введите пожалуйста число!')
#         bot.register_next_step_handler(msg, start_game, rand)


# def victorina(message, game_vic):
#     print("vic")
#     game_vic = game_victor.random_line()
#     game_vic.split("|")
#     question = game_vic[0]
#     answer = game_vic[1].strip("")
#     print(answer)
#     print(message.text.lower())
#     if message.text.lower() == answer.lower():
#         bot.send_message(message.chat.id, f"yes")
#     else:
#         msg = bot.send_message(message.chat.id, f'Еще разок')
#         bot.register_next_step_handler(msg, victorina, game_vic)
#

def zapis_date(message):
    global zap_d
    msg = bot.send_message(message.chat.id, f'Пожалуйста введите удобное для Вас дату записи в формате 01.01. ')
    bot.register_next_step_handler(msg, zapis_time)


def zapis_time(message):
    global zap_t
    print(f"Zapis: ")


if __name__ == "__main__":
    print("Start Bot")
    bot.polling(none_stop=True, interval=0)