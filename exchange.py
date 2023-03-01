import requests
import json
url = 'https://metals-api.com/api/latest?access_key=9i5jes71sd4ahp6l9jz0d2r687fvox2hktj948k23rcqxwfvv6bjtac8nt5f'

def currency_conservation():
    from_currency = input('From Country : ')
    to_currency = input('To Country : ')
    amount = int(input("Amount : ")) 
    response = requests.get(url)
    rate = response.json()['rates'][from_currency]
    amount_in_EUR = amount / rate
    amount = amount_in_EUR * (response.json()['rates'][to_currency])
    amount = round(amount,2)
    print(amount, to_currency)
    again = input('Again ? : ')
    if again == 'yes' :
        currency_conservation()

currency_conservation()
