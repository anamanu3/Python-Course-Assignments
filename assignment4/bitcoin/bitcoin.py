import sys
import requests

try:
    amount = float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit("Please specify how much coin you want to buy?")

def get_price():
    try:
        bitcoin = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=91c2807d385eed1142f6ebcc1380962550ae4f5cd1776867dd8c39b38eb18af2")
        bitcoin.raise_for_status()
        content = bitcoin.json()
        return float(content["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

price = get_price()
total = amount * price
print(f"${total:,.4f}")
