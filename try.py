import telebot
import contsts
token = "480284355:AAFr3T9YIPNj-kATXZUR5xblQri64FSw9aY"
bot = telebot.TeleBot(contsts.token)


#bot.send_message(225191458, "test")

"""
upd = bot.get_updates()
#print(upd)

last_upd = upd[-1]

msg_from_user = last_upd.message
print(msg_from_user)
"""

print(bot.get_me())

a = 42
b = "qweqeqqw"
print(type(a), type(b))

def log(message, answer):
    print("\n ------------------")
    from datetime import datetime
    print(datetime.now())
    print("Message from [0] [1]. (id = [2]) \n Text - [3]".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)



@bot.message_handler(commands=['help'])
def hendle_text(message):
    bot.send_message(message.chat.id, """Запрос "а" - ответ "b"
Запрос "b" - ответ "c" """)

@bot.message_handler(content_types=["text"])
def hendle_text(message):
    answer = "wut?"
    if message.text == "a":
        answer = "b"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "b":
        answer = "c"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "1" or message.text == "2":
        answer = "its 1 or 2"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)

bot.polling(none_stop=True, interval=0)
