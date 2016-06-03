import requests, heartbeat, ticker, json
from classes import OrderType
from classes import OrderDirection

api = 'https://api.stockfighter.io/ob/api'
api_key = 'b59767ec5f0716b59c17054c0714f01802afe963'

class Quote:

    def __init__(self, venue = '', stock = ''):
        # string: venue id
        self.venue = venue 
        # string: stock id
        self.stock = stock 

    def setVenue(self, venue):
        self.venue = venue

    def setStock(self, stock):
        self.stock = stock

    def refresh(self):
        headers = {'X-Starfighter-Authorization': api_key}
        url = api + '/venues/' + self.venue + '/stocks/' + self.stock + '/quote'
        r = requests.get(url, headers=headers)
        response = r.json()
        self.response = response
        if 'symbol' in response:
            self.symbol = response['symbol']
        if 'venue' in response:
            self.venue = response['venue']
        if 'bid' in response:
            self.bid = response['bid']
        if 'bidSize' in response:
            self.bidSize = response['bidSize']
        if 'askSize' in response:
            self.askSize = response['askSize']
        if 'bidDepth' in response:
            self.bidDepth = response['bidDepth']
        if 'askDepth' in response:
            self.askDepth = response['askDepth']
        if 'last' in response:
            self.last = response['last']
        if 'lastSize' in response:
            self.lastSize = response['lastSize']
        if 'lastTrade' in response:
            self.lastTrade = response['lastTrade']
        if 'quoteTime' in response:
            self.quoteTime = response['quoteTime']
        return r

def main():
    t = Quote()
    t.setVenue('TESTEX')
    t.setStock('FOOBAR')
    
    r = t.refresh()
    print(r.text)

    print(t.bid)
    print(t.last)


if __name__ == "__main__":
    main()
