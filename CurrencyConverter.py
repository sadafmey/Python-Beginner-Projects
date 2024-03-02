import requests

def convert_currency(amount, from_currency, to_currency):

    api_key = 'YOUR_API_KEY' # Replace 'YOUR_API_KEY' with your actual API key from a currency conversion API.
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    response = requests.get(url)
    data = response.json()

    exchange_rate = data['rates'][to_currency]
    converted_amount = amount * exchange_rate

    return converted_amount


amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")