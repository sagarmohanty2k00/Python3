import requests
response = requests.get("https://api.coinbase.com/v2/prices/spot?currency=INR")
print(response.text)