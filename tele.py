import telebot
from telebot import types
import os
import win10toast

def main():
    bot = telebot.TeleBot("5308870252:AAGVqh0BSRIoywcVSTHkG0WuWAR_UXZ42PQ")

    print('Типо запуск')

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, 'Я нагибатор3000, только напиши и комп отключится')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("/shutdown")
        but2 = types.KeyboardButton("/Online")
        but3 = types.KeyboardButton("/hiberdown")
        but4 = types.KeyboardButton("/cancel")
        markup.add(but1, but2, but3, but4)
        bot.reply_to(message, "Вывод кнопок", parse_mode='html', reply_markup=markup)

    @bot.message_handler(commands=['hiberdown'])
    def send(message):
        bot.reply_to(message, "Комп переходит в режим гибернации", )
        os.system('shutdown /h')

    @bot.message_handler(commands=['shutdown'])
    def send(message):
        sec = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but0 = types.KeyboardButton("0")
        but1 = types.KeyboardButton("1800")
        but2 = types.KeyboardButton("3600")
        but3 = types.KeyboardButton("7200")
        but4 = types.KeyboardButton("21600")
        but5 = types.KeyboardButton("Назад")
        sec.add(but0, but1, but2, but3, but4, but5)
        mesg: str = bot.send_message(message.chat.id, 'Через сколько отключить компьютер?(В секундах)',
                                     parse_mode='html', reply_markup=sec)
        bot.register_next_step_handler(mesg, test)

    def test(message):
        txt = message.text
        print(txt)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("/shutdown")
        but2 = types.KeyboardButton("/Online")
        but3 = types.KeyboardButton("/hiberdown")
        but4 = types.KeyboardButton("/cancel")
        markup.add(but1, but2, but3, but4)

        if txt == "Назад":
            bot.reply_to(message, "Возврат", parse_mode='html', reply_markup=markup)
            return

        if int(txt) >= 18000:
            cas = int(txt) / 3600
            print(cas)
            bot.reply_to(message, "Компьютер выключится через " + str(round(int(cas))) + " часов", parse_mode='html',
                         reply_markup=markup)

        if (int(txt) >= 7200) and (int(txt) < 18000):
            cas = int(txt) / 3600
            print(cas)
            bot.reply_to(message, "Компьютер выключится через " + str(round(int(cas))) + " часа", parse_mode='html',
                         reply_markup=markup)

        if (int(txt) > 3599) and (int(txt) < 7200):
            cas = int(txt) / 3600
            print(cas)
            bot.reply_to(message, "Компьютер выключится через " + str(round(int(cas))) + " час", parse_mode='html',
                         reply_markup=markup)

        if (int(txt) > 30) and (int(txt) < 120):
            minu = int(txt) / 60
            print(minu)
            bot.reply_to(message, "Компьютер выключится через " + str(round(int(minu))) + " минуту", parse_mode='html',
                         reply_markup=markup)

        if (int(txt) > 119) and (int(txt) < 300):
            minu = int(txt) / 60
            print(minu)
            bot.reply_to(message, "Компьютер выключится через " + str(round(int(minu))) + " минуты", parse_mode='html',
                         reply_markup=markup)

        if (int(txt) > 299) and (int(txt) < 3600):
            minu = int(txt) / 60
            print(minu)
            bot.reply_to(message, "Компьютер выключится через " + str(round(int(minu))) + " минут", parse_mode='html',
                         reply_markup=markup)

        if (int(txt) > 0) and (int(txt) < 31):
            minu = int(txt) / 60
            print(minu)
            bot.reply_to(message, "Компьютер выключится через " + txt + " секунд", parse_mode='html',
                         reply_markup=markup)

        if int(txt) == 0:
            bot.reply_to(message, "Компьютер отключается", parse_mode='html',
                         reply_markup=markup)
        os.system('shutdown /s /t ' + txt)

    @bot.message_handler(commands=['cancel'])
    def send(message):
        bot.reply_to(message, "Отключение отменено", )
        os.system('shutdown /a')

    @bot.message_handler(commands=['Online'])
    def send(message):
        bot.reply_to(message, "В данный момент комп онлайн", )
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("Ботяра", "Все знают, что комп онлайн", icon_path="PC-Computer-Deltarune-Spamton.ico")

    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
