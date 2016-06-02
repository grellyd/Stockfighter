import trade, requests

def main():
    account = 'MSB68413501'
    venue = 'ICCEX'
    stock = 'RFC'
    price = 9000
    qty = 75

    firstTrade = trade.Trade(account, venue, stock, price, qty)
    firstTrade.printTrade()
    response = firstTrade.execute()
    print(response.text)

if __name__ == "__main__":
    main()
