import requests, heartbeat, ticker

api = 'https://api.stockfighter.io/ob/api'
api_key = 'b59767ec5f0716b59c17054c0714f01802afe963'


def main():
    ticker.getFullTicker()
    r = requests.get(api + '/venues/TESTEX/stocks/FOOBAR')
    print(r.text)

if __name__ == "__main__":
    main()
