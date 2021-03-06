import requests, time
from trade import Trade
from quote import Quote
from classes import OrderType
from classes import OrderDirection

def main():

    account = 'CLS8002286'
    venue = 'VXEX'
    stock = 'KCYE'
    price = 0
    qty = 0
    direction = OrderDirection.buy
    orderType = OrderType.limit
    waitTime = 1
    oldPrice = 0

    trade = Trade(account, venue, stock, price, qty, direction, orderType)
    quote = Quote(venue, stock)

    # buy low, sell high
    # track stocks owned, and exposure (value per last trade)


    while (True):
        # get the spread
        quote.refresh()
        quote.prt()
        # work the spread
        trade.orderType = OrderType.limit

        if (quote.bid is not None and quote.ask is not None):
            # buy at the bid + 1
            trade.direction = OrderDirection.buy
            trade.price = quote.bid + 5
            trade.qty = quote.bidSize
            trade.prt()
            trade.execute()

            # sell at the ask - 1
            trade.direction = OrderDirection.sell
            trade.price = quote.ask - 5
            trade.size = quote.askSize
            trade.prt()
            trade.execute()

        time.sleep(2)

    # when the quote last price is low, purchase and increase order size
    # when the quote last price is high, sell and decrease order size

    # tigher spread than existing bids/asks 

    # have both a buy and sell at same time
    # have very low limit buy and immed buy
    # have very high limit sell and immed sell


def bigLimits(quote, trade):
    trade.setOrderType = OrderType.limit
    trade.setQty(quote.lastSize)
    # low
    trade.setPrice(max(quote.last - 500, 0))
    trade.setDirection(OrderDirection.buy)
    trade.execute()
    trade.prt()
    # high
    trade.setPrice(quote.last + 2000)
    trade.setDirection(OrderDirection.sell)
    trade.execute()
    trade.prt()

def choosePrice(quote, trade):
    price = trade.price
    if (price == quote.last):
        price += 10
    else:
        price = quote.last
    return price

def exposure(quote, numStockOwned):
    return numStockOwned * quote.last

    

if __name__ == "__main__":
    main()
