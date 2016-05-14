import requests, heartbeat, ticker 
from enum import Enum


class Order(Enum):
    limit = 'limit'
    market = 'market'
    fill = 'fill-or-kill'
    immed = 'immediate-or-cancel'

class OrderDirection(Enum):
    buy = 'buy'
    sell = 'sell'

api = 'https://api.stockfighter.io/ob/api'
api_key = 'b59767ec5f0716b59c17054c0714f01802afe963'

class Trade:

    def __init__(self, account = '', venue = '', stock = '', price = 0, qty = 0, direction = OrderDirection.buy, orderType = Order.limit):
        # string: trading account id
        self.account = account 
        # string: venue id
        self.venue = venue 
        # string: stock id
        self.stock = stock 
        # int: price to ask/bid
        self.price = price 
        # int: quantity to trade
        self.qty = qty 
        # OrderDirection: buy or sell
        self.direction = direction 
        # Order: order type 
        self.orderType = orderType 

    def setAccount(self, account):
        self.account = account
        
    def setVenue(self, venue):
        self.venue = venue

    def setStock(self, stock):
        self.stock = stock

    def setPrice(self, price):
        self.price = price

    def setQty(self, qty):
        self.qty = qty

    def setDirection(self, direction):
        self.direction = direction

    def setOrderType(self, orderType):
        self.orderType = orderType

    def execute(self):
        payload = {
                'account' : self.account,
                'venue' : self.venue,
                'stock' : self.stock,
                'price' : self.price,
                'qty' : self.qty,
                'direction' : self.direction,
                'orderType' : self.orderType
                }
        r = requests.post(api + '/venues/' + self.venue + '/stocks/' + self.stock + '/orders X-Starfighter-Authorization:' + api_key, data = payload)
        return r


def main():
    t = Trade()
    t.setAccount('EXB123456')
    t.setVenue('TESTEX')
    t.setStock('FOOBAR')
    t.setQty(100)
    
    r = execute(t)
    print(r.text)


if __name__ == "__main__":
    main()
