import random
import telebot
import time
import config
from telebot import types
from tkinter import *

TOKEN = 'вставить токен бота'
bot = telebot.TeleBot(TOKEN)

try:

    # настрока приветствия у бота автоматизированной системы пожаротушнения
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Начало использования.")
        item2 = types.KeyboardButton("Проверка бота.")
        markup.add(item1, item2)

        bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>. Телеграм-бот уведомляющий вас о состоянии вашей автоматической системы пожаротушения.".format(
                             message.from_user, bot.get_me()), parse_mode='html')
        bot.send_message(message.chat.id, "Для запуска автоматической системы пожаротушения нажмите кнопку снизу.",
                         reply_markup=markup)


    # настройка принятия сообщений ботом автоматизированной системы пожаротушения
    @bot.message_handler(content_types=['text'])
    # основная функция работы бота
    def talks(message):
        # имитация работы датчика угарного газа
        def getGas(COinfo):
            if COinfo >= start_valve:
                print(COinfo - 0.2)
                return (COinfo - 0.2)
            elif COinfo <= start_valve:
                return (COinfo)
            else:
                return (-1)

        # имитация работы испонтельного устройства
        def checkIon(ionvalve):
            print(ionvalve)
            if ionvalve <= 0:
                return (0)
            elif ionvalve > 0:
                return (ionvalve - 5)
            else:
                return (-1)

        # имитация работы блока управления
        def fireAlarm(COinfo, ionvalve):
            try:
                if COinfo >= start_valve:
                    if ionvalve > 0:
                        bot.send_message(message.chat.id,
                                         "Было обнаружено возгорание. Система пожаротушения активирована")
                        ionvalve = checkIon(ionvalve)
                        print(ionvalve)
                        return (fireAlarm(getGas(COinfo), ionvalve))
                    if checkIon(ionvalve) <= 0:
                        bot.send_message(message.chat.id,
                                         "Было обнаружено возгорание. Система пожаротушения не может быть активирована. Малый запас газа в баллоне. Вызовите пожарную охрану.")
                        return (0)
                    else:
                        bot.send_message(message.chat.id,
                                         "Внутренняя ошибка. Перезапустите автоматическую систему пожаротушения.")
                        return (-1)
                elif COinfo <= start_valve and COinfo >= 0:
                    bot.send_message(message.chat.id, "Система пожаротушения справилась с огнем.")
                    return (1)
                else:
                    bot.send_message(message.chat.id, "Сбой системы. Неверные данные.")
            except Exception as E:
                bot.send_message(message.chat.id, "Сбой системы. Неверные данные.")

        if message.text == 'Проверка бота.':
            print(fireAlarm(1, 10))

        elif message.text == 'Начало использования.':
            try:
                while True:
                    now_valve = random.uniform(0, 1)
                    now_ionvalve = random.randint(5, 100)
                    if now_valve >= start_valve:
                        fireAlarm(now_valve, now_ionvalve)
                    if now_valve <= start_valve:
                        if checkIon(now_ionvalve) <= 5:
                            bot.send_message(message.chat.id,
                                             "В баллоне исполнительного устройства недостаточно газа для предотвращения пожара. <b>Заполните баллон газом, для предотвращения последующих пожаров.</b>".format(
                                                 message.from_user, bot.get_me()), parse_mode='html')
                    time.sleep(5)
            except Exception as E:
                bot.send_message(message.chat.id,
                                 "Ошибка системы. Перезагрузите систему, чтобы продолжить пользоваться ботом.")
        else:
            bot.send_message(message.chat.id, "Сообщение не распозано. Нажмите на кнопки снизу.")

        # создание внутренних переменных


    start_valve = 0.5
    start_ionvalve = 0

    bot.polling()
except Exception as E:
    root = Tk()
    root.title("Автоматизированная система пожаротушения.")
    root.geometry("400x300")
    btn1 = Button(text="НЕТ ИНТЕРНЕТ СОЕДИНЕНИЯ.", background="#555", foreground="#ccc", padx="15", pady="6", font="15",
                  command=lambda: quit_program())


    def quit_program():
        root.destroy()


    btn1.pack(expand=True, fill=BOTH)
    root.mainloop()
