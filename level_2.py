import trade, requests, time

def main():
    account = 'DBL27132229'
    venue = 'GULBEX'
    stock = 'MEM'
    price = 3200
    qty = 1000

    secondTrade = trade.Trade(account, venue, stock, price, qty)
    while (True) :
        response = secondTrade.execute()
        time.sleep(3)
    print(response.text)

if __name__ == "__main__":
    main()
