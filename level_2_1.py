import requests, time
from trade import Trade
from quote import Quote
from classes import OrderType
from classes import OrderDirection

def main():

    account = 'WAM16101756'
    venue = 'SYTEX'
    stock = 'TMH'
    price = 3200
    qty = 1000
    direction = OrderDirection.buy
    orderType = OrderType.limit
    waitTime = 10
    oldPrice = 0

    trade = Trade(account, venue, stock, price, qty, direction, orderType)
    quote = Quote(venue, stock)

    vol = 0
    while (vol < 100000):
        quote.refresh()
        price = choosePrice(quote, trade)
       # if (price == 2608 or price > 2608):
       #     waitTime = 20
       #     price = 1700
       # else:
       #     waitTime = 1
        trade.setPrice(price)
        trade.setQty(quote.lastSize() + 5)
        trade.prt()
        response = trade.execute()
        vol += qty
        time.sleep(waitTime)

def choosePrice(quote, trade):
    price = trade.price
    if (price == quote.last()):
        price += 10
    else:
        price = quote.last()
    return price

if __name__ == "__main__":
    main()
