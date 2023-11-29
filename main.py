import telebot
import random

bot = telebot.TeleBot('6500079784:AAFyaCPgjqYKW83sjhbTtteK9mS5kq71M30')


# start cmd ////
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     '🎲Бот, в котором можно попытать удачу или выбрать число. \nКоммандой /help можно просмотреть все существующие комманды (или выбрать их из списка).')


# help cmd ////
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
                     '/rng1, /rng2, /rng3 - Попытайте удачу с разным уровнем сложности. \n/number - Генерирует любое число от 1 до 1,000,000.')


# rng cmd 1 ////
@bot.message_handler(commands=['rng1'])
def main(message):
    num = 50
    chosenNum = random.randint(1, num)

    if chosenNum == 1:
        bot.send_message(message.chat.id,
                         '🍀Удача на Вашей стороне! (шанс 1 из ' + str(num))

    else:
        bot.send_message(message.chat.id,
                         '♠️Не повезло...')


# rng cmd 2 ////
@bot.message_handler(commands=['rng2'])
def main(message):
    num = 200
    chosenNum = random.randint(1, num)

    if chosenNum == 1:
        bot.send_message(message.chat.id,
                         '🍀Удача на Вашей стороне!! (шанс 1 из ' + str(num))

    else:
        bot.send_message(message.chat.id,
                         '♠️Не повезло...')


# rng cmd 3 ////
@bot.message_handler(commands=['rng3'])
def main(message):
    num = 1000
    chosenNum = random.randint(1, num)

    if chosenNum == 1:
        bot.send_message(message.chat.id,
                         '🍀Удача на Вашей стороне!!! (шанс 1 из ' + str(num))

    else:
        bot.send_message(message.chat.id,
                         '♠️Не повезло...')


# number cmd ////
@bot.message_handler(commands=['number'])
def main(message):
    num = random.randint(1, 1000000)
    bot.send_message(message.chat.id,
                     '🃏Ваше число:', str(num))


bot.infinity_polling()