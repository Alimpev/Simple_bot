import telebot

from config import TOKEN
from extensions import Bot_api, APIException, check_data


currency = {
            'евро' : 'EUR',
            'доллар' : 'USD',
            'рубль' : 'RUB'
            }


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start","help"])
def start_help(message):
    bot.send_message(message.chat.id, f"You must enter data in the form: \n\n1 - name of the currency whose price you want to know \n2 - name of the currency in which you want to know the price of the first currency \n3 - amount of the first currency\n \nTo view the available currencies, enter the command '/ values'")


@bot.message_handler(commands=['values'])
def values(message):
    text = "Conversion into currencies:"
    for i in currency.keys():
        text += "\n" + i
    bot.send_message(message.chat.id, text)



@bot.message_handler(content_types=['text',"sticker", "voice", "photo", "audio", "document"])
def user_asks(message):

    if message.content_type == 'text':
        user_data = list(message.text.split(' '))

        if len(user_data) != 3:
            bot.reply_to(message, APIException())
            raise APIException()
        else:
            quote, base, amount = user_data[0], user_data[1], user_data[2]


        if check_data(quote, base, amount) == False:
            bot.reply_to(message, APIException())
            raise APIException()

        suitable_amount = check_data(quote, base, amount)

        result = Bot_api(quote, base, suitable_amount).get_price()
        bot.reply_to(message, f"{result}")


    else:
        bot.send_message(message.chat.id, "You must enter data in the TEXT form \nEnter  command '/start' or '/help' to find out the input format")



bot.infinity_polling()



















































































