import requests
from bs4 import BeautifulSoup

import datetime
import random

from telebot import types
import telebot

TOKEN = '5185038887:AAHcWPaBLH8-fxJKe04XzBy0iafe-UWAwss'
bot = telebot.TeleBot(TOKEN)

c = 0

special_cods_cinema_today = []
special_cods_cinema_tommorow = []
for t in range (24):
    special_cods_cinema_today.append("/cinema" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))
    special_cods_cinema_tommorow.append("/cinema" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))


special_cods_theatre_today = []
special_cods_theatre_tommorow = []
for t in range (24):
    special_cods_theatre_today.append("/theatre" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))
    special_cods_theatre_tommorow.append("/theatre" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))

print(special_cods_theatre_tommorow)
data_cinema = 'https://www.afisha.ru/msk/schedule_cinema/na-segodnya/'
data_theatre = 'https://www.afisha.ru/msk/schedule_theatre/na-segodnya/'

def link(url):
    array_link = []
    get_links = ""
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cinema = soup.findAll('div', {"class":"_1kwbj lkWIA _2Ds3f"})

    for film in cinema:
        search_name = film.find('div', class_="_1kwbj lkWIA _161Om")
        link = "https://www.afisha.ru" + search_name.find('a', class_='_3NqYW DWsHS _3lmHp wkn_c').get('href')
        array_link.append(link)
    
    for i in array_link:
        get_links = get_links + i + " "

    get_links = get_links.split()
    return (get_links)

def more_cinema(i):
    global c
    if i < 0:
        c == 0
    else:
        links = link(data_cinema)
        response = requests.get(links[i])
        soup = BeautifulSoup(response.text, 'lxml')

        #name of cinema
        array_name_film = soup.find('h1', class_="KOq_N").text
        array_name_film = array_name_film.split()

        name_film = ""
        for j in range (len(array_name_film)):
            if j+1 < len(array_name_film):
                name_film = name_film + array_name_film[j+1] + " "
            else:
                pass
            
        #description of cinema
        try:
            description = soup.find('span', class_="_27LvS").text
        except Exception as E:
            description = ""

        #rating of cinema
        try:
            rating = soup.find('h2', class_="_3Di4D _2qUBY").text
        except Exception as E:
            rating = ""
            
        #style of cinema
        try:
            style = soup.find('div', class_="_2jztV _98d6U L6xaR")
            style = style.find('span', class_="_1gC4P").text
        except Exception as E:
            style = ""
        

        return (name_film + '\n' + rating + '\n' + style + '\n' + description + '\n' + 'Подробнее на сайте: ' + links[i])        

def name_cinema(url):
    array_cinema = []
    array_type = []

    answer = ""
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cinema = soup.findAll('div', {"class":"_1kwbj lkWIA _2Ds3f"})
    
    for film in cinema:
        search_name = film.find('div', class_="_1kwbj lkWIA _161Om")
        ru_name = str(search_name.find('h2', class_='_3Yfoo').text)
        style = str(search_name.find('span', class_='_1gC4P').text)
        
        
        array_type.append(style)
        array_cinema.append(ru_name)
    if url == 'https://www.afisha.ru/msk/schedule_cinema/na-segodnya/':    
        for i in  range (len(array_cinema)):
            answer = answer + array_cinema[i] + " " + array_type[i] +'\n' + special_cods_cinema_today[i] + '\n' + '\n'
    if url == 'https://www.afisha.ru/msk/schedule_cinema/na-zavtra/':    
        for i in  range (len(array_cinema)):
            answer = answer + array_cinema[i] + " " + array_type[i] +'\n' + special_cods_cinema_tommorow[i] + '\n' + '\n'
    return (answer)

def name_theatre(url):
    array_theatre = []
    array_type = []

    answer = ""
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    theatre = soup.findAll('div', {"class":"_1kwbj lkWIA _2Ds3f"})
    
    for film in theatre:
        search_name = film.find('div', class_="_1kwbj lkWIA _161Om")
        ru_name = str(search_name.find('h2', class_='_3Yfoo').text)
        style = str(search_name.find('span', class_='_1gC4P').text)
        
        
        array_type.append(style)
        array_theatre.append(ru_name)
    if url == 'https://www.afisha.ru/msk/schedule_theatre/na-segodnya/':    
        for i in  range (len(array_theatre)):
            answer = answer + array_theatre[i] + '\n' + array_type[i] +'\n' + special_cods_theatre_today[i] + '\n' + '\n'
    if url == 'https://www.afisha.ru/msk/schedule_theatre/na-zavtra/':    
        for i in  range (len(array_theatre)):
            answer = answer + array_theatre[i] + '\n' + array_type[i] +'\n' + special_cods_theatre_tommorow[i] + '\n' + '\n'
    return (answer)

def more_theatre(i):
    global c
    if i < 0:
        c == 0
    else:
        links = link(data_theatre)
        response = requests.get(links[i])
        soup = BeautifulSoup(response.text, 'lxml')

        #name of cinema
        array_name_theatre = soup.find('h1', class_="KOq_N").text
        array_name_theatre = array_name_theatre.split()

        name_theatre = ""
        for j in range (len(array_name_theatre)):
            if j+1 < len(array_name_theatre):
                name_theatre = name_theatre + array_name_theatre[j+1] + " "
            else:
                pass
            
        #description of cinema
        try:
            description = soup.find('span', class_="_27LvS").text
        except Exception as E:
            description = ""

        #rating of cinema
        try:
            rating = soup.find('h2', class_="_3Di4D _2qUBY").text
        except Exception as E:
            rating = ""
            
        #style of cinema
        try:
            style = soup.find('div', class_="_2jztV _98d6U L6xaR")
            style = style.find('span', class_="_1gC4P").text
        except Exception as E:
            style = ""
        

        return (name_theatre + '\n' + rating + '\n' + style + '\n' + description + '\n' + 'Подробнее на сайте: ' + links[i])

print (more_theatre(0))

def buy_tick_theatre(i):
    array_lin = []
    links = link(data_theatre)
    url = links[i]
    print (url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cinema = soup.findAll('div', class_='_3CqPZ')

    for film in cinema:
        hrefs = film.findAll('a', class_='_3NqYW _3e0o7 QWrbp Du7jw')
    tickets = 'https://www.afisha.ru' + hrefs[0].get('href')
    
    return (tickets)
print (buy_tick_theatre(0))

def buy_ticket(i):
    array_lin = []
    links = link(data_cinema)
    url = links[i]
    print (url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cinema = soup.findAll('div', class_='_3CqPZ')

    for film in cinema:
        hrefs = film.findAll('a', class_='_3NqYW _3e0o7 QWrbp Du7jw')
    try:
        tickets = 'https://www.afisha.ru' + hrefs[1].get('href')
    except Exception as E:
        tickets = 'https://www.afisha.ru' + hrefs[0].get('href')
    
    return (tickets)
print (buy_ticket(6))

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Как стать организатором?")
    item2 = types.KeyboardButton("Чем заняться?")


    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>. Помогу найти приключения на задницу в твое свободное время.".format(message.from_user, bot.get_me()),
        parse_mode='html')
    bot.send_message(message.chat.id, "Чем я могу помочь тебе?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def talks(message):
    if message.text == 'Как стать организатором?':
        bot.send_message(message.chat.id, "Позже")
    elif message.text == 'Чем заняться?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Кино.", callback_data='cinema')
            item2 = types.InlineKeyboardButton("Театр.", callback_data='theatre')
            item3 = types.InlineKeyboardButton("Выставки.", callback_data='show')
            item4 = types.InlineKeyboardButton("Клубные мероприятия.", callback_data='dance')
            item5 = types.InlineKeyboardButton("Выбери за меня пж-пж.", callback_data='rand')
 
            markup.add(item1, item2, item3, item4, item5)
 
            bot.send_message(message.chat.id, 'Что тебя больше интересует? У меня большой выбор!', reply_markup=markup)

    elif message.text == 'хочу купить негра':
        bot.send_message(message.chat.id, 'https://memepedia.ru/xochyu-olive/')

    elif message.text == 'Усман':
        bot.send_message(message.chat.id, 'еблан? я Стас.')
    elif message.text == 'Стас':
        bot.send_message(message.chat.id, 'Сам ты Стас.')
    

############################################################################################################################
    elif message.text == special_cods_cinema_today[0]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(0))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(0),reply_markup=markup)
    elif message.text == special_cods_cinema_today[1]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(1))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(1),reply_markup=markup)
    elif message.text == special_cods_cinema_today[2]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(2))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(2),reply_markup=markup)
    elif message.text == special_cods_cinema_today[3]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(3))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(3),reply_markup=markup)
    elif message.text == special_cods_cinema_today[4]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(4))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(4),reply_markup=markup)
    elif message.text == special_cods_cinema_today[5]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(5))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(5),reply_markup=markup)
    elif message.text == special_cods_cinema_today[6]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(6))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(6),reply_markup=markup)
    elif message.text == special_cods_cinema_today[7]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(7))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(7),reply_markup=markup)
    elif message.text == special_cods_cinema_today[8]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(8))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(8),reply_markup=markup)
    elif message.text == special_cods_cinema_today[9]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(9))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(9),reply_markup=markup)
    elif message.text == special_cods_cinema_today[10]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(10))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(10),reply_markup=markup)
    elif message.text == special_cods_cinema_today[11]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(11))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(11),reply_markup=markup)
    elif message.text == special_cods_cinema_today[12]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(12))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(12),reply_markup=markup)
    elif message.text == special_cods_cinema_today[13]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(13))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(13),reply_markup=markup)
    elif message.text == special_cods_cinema_today[14]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(14))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(14),reply_markup=markup)
    elif message.text == special_cods_cinema_today[15]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(15))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(15),reply_markup=markup)
    elif message.text == special_cods_cinema_today[16]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(16))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(16),reply_markup=markup)
    elif message.text == special_cods_cinema_today[17]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(17))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(17),reply_markup=markup)
    elif message.text == special_cods_cinema_today[18]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(18))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(18),reply_markup=markup)
    elif message.text == special_cods_cinema_today[19]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(19))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(19),reply_markup=markup)
    elif message.text == special_cods_cinema_today[20]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(20))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(20),reply_markup=markup)
    elif message.text == special_cods_cinema_today[21]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(21))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(21),reply_markup=markup)
    elif message.text == special_cods_cinema_today[22]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(22))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(22),reply_markup=markup)
    elif message.text == special_cods_cinema_today[23]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(23))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(23),reply_markup=markup)
#tommorow
    elif message.text == special_cods_cinema_tommorow[0]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(0))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(0),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[1]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(1))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(1),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[2]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(2))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(2),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[3]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(3))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(3),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[4]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(4))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(4),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[5]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(5))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(5),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[6]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(6))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(6),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[7]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(7))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(7),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[8]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(8))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(8),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[9]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(9))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(9),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[10]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(10))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(10),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[11]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(11))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(11),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[12]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(12))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(12),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[13]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(13))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(13),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[14]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(14))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(14),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[15]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(15))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(15),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[16]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(16))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(16),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[17]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(17))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(17),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[18]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(18))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(18),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[19]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(19))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(19),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[20]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(20))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(20),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[21]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(21))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(21),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[22]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(22))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(22),reply_markup=markup)
    elif message.text == special_cods_cinema_tommorow[23]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_ticket(23))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_cinema(23),reply_markup=markup)
######################################################################################################################   
    elif message.text == special_cods_theatre_today[0]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(0))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(0),reply_markup=markup)
    elif message.text == special_cods_theatre_today[1]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(1))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(1),reply_markup=markup)
    elif message.text == special_cods_theatre_today[2]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(2))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(2),reply_markup=markup)
    elif message.text == special_cods_theatre_today[3]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(3))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(3),reply_markup=markup)
    elif message.text == special_cods_theatre_today[4]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(4))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(4),reply_markup=markup)
    elif message.text == special_cods_theatre_today[5]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(5))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(5),reply_markup=markup)
    elif message.text == special_cods_theatre_today[6]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(6))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(6),reply_markup=markup)
    elif message.text == special_cods_theatre_today[7]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(7))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(7),reply_markup=markup)
    elif message.text == special_cods_theatre_today[8]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(8))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(8),reply_markup=markup)
    elif message.text == special_cods_theatre_today[9]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(9))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(9),reply_markup=markup)
    elif message.text == special_cods_theatre_today[10]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(10))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(10),reply_markup=markup)
    elif message.text == special_cods_theatre_today[11]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(11))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(11),reply_markup=markup)
    elif message.text == special_cods_theatre_today[12]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(12))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(12),reply_markup=markup)
    elif message.text == special_cods_theatre_today[13]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(13))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(13),reply_markup=markup)
    elif message.text == special_cods_theatre_today[14]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(14))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(14),reply_markup=markup)
    elif message.text == special_cods_theatre_today[15]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(15))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(15),reply_markup=markup)
    elif message.text == special_cods_theatre_today[16]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(16))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(16),reply_markup=markup)
    elif message.text == special_cods_theatre_today[17]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(17))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(17),reply_markup=markup)
    elif message.text == special_cods_theatre_today[18]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(18))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(18),reply_markup=markup)
    elif message.text == special_cods_theatre_today[19]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(19))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(19),reply_markup=markup)
    elif message.text == special_cods_theatre_today[20]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(20))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(20),reply_markup=markup)
    elif message.text == special_cods_theatre_today[21]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(21))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(21),reply_markup=markup)
    elif message.text == special_cods_theatre_today[22]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(22))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(22),reply_markup=markup)
    elif message.text == special_cods_theatre_today[23]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(23))
        markup.add(item1)

        bot.send_message(message.chat.id, more_theatre(23),reply_markup=markup)
#tommorow
    elif message.text == special_cods_theatre_tommorow[0]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(0))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(0),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[1]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(1))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(1),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[2]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(2))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(2),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[3]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(3))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(3),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[4]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(4))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(4),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[5]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(5))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(5),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[6]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(6))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(6),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[7]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(7))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(7),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[8]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(8))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(8),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[9]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(9))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(9),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[10]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(10))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(10),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[11]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(11))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(11),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[12]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(12))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(12),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[13]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(13))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(13),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[14]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(14))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(14),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[15]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(15))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(15),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[16]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(16))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(16),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[17]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(17))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(17),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[18]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(18))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(18),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[19]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(19))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(19),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[20]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(20))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(20),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[21]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(21))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(21),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[22]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(22))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(22),reply_markup=markup)
    elif message.text == special_cods_theatre_tommorow[23]:
        markup = types.InlineKeyboardMarkup (row_width=2)

        item1 = types.InlineKeyboardButton(text = "Купить билет", url= buy_tick_theatre(23))
        markup.add(item1)
        
        bot.send_message(message.chat.id, more_theatre(23),reply_markup=markup)
                         
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'cinema':
                global data_cinema
                markup = types.InlineKeyboardMarkup (row_width=2)
                item1 = types.InlineKeyboardButton("Сегодня", callback_data='today_cinema')
                item2 = types.InlineKeyboardButton("Завтра", callback_data='tommorow_cinema')

                markup.add(item1, item2)

                bot.send_message(call.message.chat.id, "Когда ты бы хотел пойти в кино?", reply_markup=markup)

            if call.data == 'today_cinema':
                data_cinema = 'https://www.afisha.ru/msk/schedule_cinema/na-segodnya/'
                answer = name_cinema('https://www.afisha.ru/msk/schedule_cinema/na-segodnya/')
    
                bot.send_message(call.message.chat.id, answer)
                
            elif call.data == 'tommorow_cinema':
                data_cinema = 'https://www.afisha.ru/msk/schedule_cinema/na-zavtra/'
                answer = name_cinema('https://www.afisha.ru/msk/schedule_cinema/na-zavtra/')
                
                bot.send_message(call.message.chat.id, answer)             

                
            elif call.data == 'theatre':
                global data_theatre
                markup = types.InlineKeyboardMarkup (row_width=2)
                item1 = types.InlineKeyboardButton("Сегодня", callback_data='today_theatre')
                item2 = types.InlineKeyboardButton("Завтра", callback_data='tommorow_theatre')

                markup.add(item1, item2)

                bot.send_message(call.message.chat.id, "Когда ты бы хотел пойти в театр?", reply_markup=markup)

            if call.data == 'today_theatre':
                data_theatre = 'https://www.afisha.ru/msk/schedule_theatre/na-segodnya/'
                answer = name_theatre(data_theatre)

                bot.send_message(call.message.chat.id, answer)

            if call.data == 'tommorow_theatre':
                data_theatre = 'https://www.afisha.ru/msk/schedule_theatre/na-zavtra/'
                answer = name_theatre(data_theatre)

                bot.send_message(call.message.chat.id, answer)
    except Exception as e:
        print(repr(e))



bot.polling()
