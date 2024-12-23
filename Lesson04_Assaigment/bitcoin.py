import requests
import sys

if len(sys.argv)!=2:
    sys.exit("Missing command line argument")
elif sys.argv[1].isalpha()==True:
    sys.exit("Command-line argument is not a number.")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
except requests.RequestException:
    print("File could not open.")
    sys.exit

while True:
    choice = input("USD or EUR : ")
    match choice.strip().lower():
        case "usd":
            btc = o["bpi"]["USD"]["rate_float"]
            sign = "$"
            break
        case "eur":
            btc = o["bpi"]["EUR"]["rate_float"]
            sign = "€"
            break

btc = float(btc)
btc = float(sys.argv[1]) * btc
print(f"{sign}{btc:,.4f}")