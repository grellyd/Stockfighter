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

    def refresh(self):
        headers = {'X-Starfighter-Authorization': api_key}
        url = api + '/venues/' + self.venue + '/stocks/' + self.stock + '/quote'
        r = requests.get(url, headers=headers)
        self.response = r.json()
        if 'symbol' in self.response:
            self.symbol = self.response['symbol']
        if 'venue' in self.response:
            self.venue = self.response['venue']
        if 'bid' in self.response:
            self.bid = self.response['bid']
        if 'bidSize' in self.response:
            self.bidSize = self.response['bidSize']
        if 'bidDepth' in self.response:
            self.bidDepth = self.response['bidDepth']
        if 'ask' in self.response:
            self.ask = self.response['ask']
        if 'askSize' in self.response:
            self.askSize = self.response['askSize']
        if 'askDepth' in self.response:
            self.askDepth = self.response['askDepth']
        if 'last' in self.response:
            self.last = self.response['last']
        if 'lastSize' in self.response:
            self.lastSize = self.response['lastSize']
        if 'lastTrade' in self.response:
            self.lastTrade = self.response['lastTrade']
        if 'quoteTime' in self.response:
            self.quoteTime = self.response['quoteTime']
        return r

    def prt(self):
        print('symbol: ' + str(self.symbol))
        print('venue: ' + str(self.venue))
        print('bid: ' + str(self.bid))
        print('bidSize: ' + str(self.bidSize))
        print('bidDepth: ' + str(self.bidDepth))
        print('ask: ' + str(self.ask))
        print('askSize: ' + str(self.askSize))
        print('askDepth: ' + str(self.askDepth))
        print('last: ' + str(self.last))
        print('lastSize: ' + str(self.lastSize))
        print('quoteTime: ' + str(self.quoteTime))

def main():
    t = Quote()
    t.setVenue('TESTEX')
    t.setStock('FOOBAR')
    
    r = t.refresh()
    print(r.text)

    print(t.bid)
    print(t.last)
    t.prt()


if __name__ == "__main__":
    main()
