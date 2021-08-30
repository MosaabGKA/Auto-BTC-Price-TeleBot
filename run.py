import requests
import time

API_KEY = 'YOUR_COINMARKETCAP_API'
BOT_KEY = 'YOUR_BOT_TOKEN'
CHAT_KEY = 'YOUR_CHAT_ID'
time_int = 86000

def get_price(currency):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        'start':'1',
        'limit':'5',
        'convert':currency
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    
    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response ['data'][0]['quote'][currency]['price'] 
    return btc_price
  
def send_update(CHAT_KEY, msg):
    url = f"https://api.telegram.org/bot{BOT_KEY}/sendMessage?chat_id={CHAT_KEY}&text={msg}" 
    requests.get(url)

def main():
    while True:
        price = round(get_price('USD'), 1)
        egp_price = round(get_price('EGP'), 1)
        msg = f"Hey, Man.. \n Bitcoin's price today is {price} USD, which means {egp_price} EGP. \n Have a nice day!"
        send_update(CHAT_KEY, msg)
        time.sleep(time_int)
main()
