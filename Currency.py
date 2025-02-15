import requests

API_KEY = 'fca_live_iWR7w2U7IAfg5ZifTPH00tdW3n3gCAF2uHeiT2Ng'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCY = ["EUR","USD","CAD","INR"]

def convert_currency(base):
    currency = ",".join(CURRENCY)
    url = f"{BASE_URL}&base_currency={base}&currencies={currency}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None
    
while True:
    base = input("Enter the base currency to convert(q to quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue    
    del data[base]

    for ticker, value in data.items():
        print(f"{ticker}: {value}")
