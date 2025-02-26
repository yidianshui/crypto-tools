import requests

def get_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(symbol, {}).get("usd", "Price not found")
    else:
        return "Error fetching price"

if __name__ == "__main__":
    crypto = input("Enter cryptocurrency (e.g., bitcoin): ").lower()
    price = get_crypto_price(crypto)
    print(f"The current price of {crypto} is: ${price}")
