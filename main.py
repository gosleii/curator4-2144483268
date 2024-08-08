import telebot

bot = telebot.TeleBot("7192629699:AAEFE1nYvkoCTPKLcICN4PQd-tFW02Iup5Q")

@bot.message_handler(commands=["start"])
def your_handler(message):
    bot.send_message(message.chat.id, "Салам")

@bot.message_handler(commands=["school_1"])
def your_handler(message):
    bot.send_message(message.chat.id, "*ссылка: https://beeschool.team*", parse_mode="Markdown")

@bot.message_handler(commands=["school_2"])
def your_handler(message):
    bot.send_message(message.chat.id, "*ссылка: https://100points.ru/student/courses*", parse_mode="Markdown")

@bot.message_handler(commands=["school_3"])
def your_handler(message):
    bot.send_message(message.chat.id, "*ссылка: https://edu.sirius.online/#/*", parse_mode="Markdown")

bot.infinity_polling()