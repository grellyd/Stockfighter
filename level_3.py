import requests, time
from trade import Trade
from quote import Quote
from classes import OrderType
from classes import OrderDirection

def main():

    account = 'SL57308766'
    venue = 'UDRYEX'
    stock = 'AREI'
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

    # when the quote last price is low, purchase and increase order size
    # when the quote last price is high, sell and decrease order size

    # tigher spread than existing bids/asks 

    # have both a buy and sell at same time
    # have very low limit buy and immed buy
    # have very high limit sell and immed sell

    while(True):
        quote.refresh()
        bigLimits(quote, trade)
        i = 0
        while (i < 30):
            trade.orderType = OrderType.immed
            trade.price = quote.bid + 5
            trade.direction = OrderDirection.buy
            trade.setQty(4)#max(quote.lastSize - 5, 1))
            trade.execute()
            trade.prt()

            trade.price = quote.last + 5
            trade.direction = OrderDirection.sell
            trade.setQty(4) #max(quote.lastSize - 5, 1))
            trade.execute()
            trade.prt()
            i += 1
            time.sleep(waitTime)



#    vol = 0
#    while (vol < 100000):
#        quote.refresh()
#        price = choosePrice(quote, trade)
#
#        trade.setPrice(price)
#        trade.setQty(quote.lastSize + 5)
#        trade.prt()
#        response = trade.execute()
#        vol += qty
#        time.sleep(waitTime)

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
