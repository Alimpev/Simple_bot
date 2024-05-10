import requests
import json


currency = {'евро' : 'EUR',
            'доллар' : 'USD',
            'рубль' : 'RUB'
            }

class APIException(Exception):
    def __str__(self):
        return "You entered the data incorrectly \nEnter  command '/start' or '/help' to find out the input format"



def check_data(quote, base, amount):


    if isinstance(quote, str) and isinstance(base, str):

        if amount.isdigit():
            amount = int(amount)

        else:
            if ',' in amount:
                amount = amount.replace(',', '.')

            if '.' in amount:
                check_details = amount.split('.')
                for i in check_details:
                    if i.isdigit():
                        pass
                    else:
                        return False
                amount = float(amount)


        if quote not in currency.keys():
            print(currency.keys())
            return False
        elif base not in currency.keys():
            return False
        elif amount < 0:
            return False
        else:
            return amount


    else:
        return False



class Bot_api:

    def __init__(self, quote, base, amount):
        self.quote = quote
        self.base = base
        self.amount = amount
        self.value = None
        self.result = None

    def set_result(self):
        self.result = self.amount * self.value

    def set_value(self, value):
        self.value = value

    def get_price(self):

        data_from_net = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={currency[self.quote]}&tsyms={currency[self.base]}")
        data = json.loads(data_from_net.content)[currency[self.base]]

        self.set_value(data)
        self.set_result()

        return f"--------RESULT--------\n {self.result}"



