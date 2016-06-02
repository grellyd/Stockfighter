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
        self.response = r.json()
        return r

    def symbol(self):
        return self.response['symbol']

    def venue(self):
        return self.response['venue']

    def bid(self):
        return self.response['bid']

    def bidSize(self):
        return self.response['bidSize']

    def askSize(self):
        return self.response['askSize']

    def bidDepth(self):
        return self.response['bidDepth']

    def askDepth(self):
        return self.response['askDepth']

    def last(self):
        return self.response['last']

    def lastSize(self):
        return self.response['lastSize']
    
    def lastTrade(self):
        return self.response['lastTrade']

    def quoteTime(self):
        return self.response['quoteTime']

def main():
    t = Quote()
    t.setVenue('TESTEX')
    t.setStock('FOOBAR')
    
    r = t.refresh()
    print(r.text)

    print(t.bid())
    print(t.last())


if __name__ == "__main__":
    main()
