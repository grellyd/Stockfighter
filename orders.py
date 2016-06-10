import requests, time
from classes import OrderType
from classes import OrderDirection

api = 'https://api.stockfighter.io/ob/api'
b
def refresh(self):
    url = api + '/venues/' + self.venue + '/accounts/' + self.account + '/orders'
    r = requests.get(url)
    if (r.status_code == requests.codes.ok):
        self.response = r.json()
        if 'symbol' in self.response:
            self.symbol = self.response['symbol']
        if 'venue' in self.response:
            self.venue = self.response['venue']
        if 'direction' in self.response:
            self.direction = self.response['direction']
        if 'qty' in self.response:
            self.qty = self.response['qty']
        if 'price' in self.response:
            self.price = self.response['price']
        if 'orderType' in self.response:
            self.orderType = self.response['orderType']
        if 'id' in self.response:
            self.orderId = self.response['id']
        if 'account' in self.response:
            self.orderAccount = self.response['account']
        if 'ts' in self.response:
            self.ts = self.response['ts']
        if 'fills' in self.response:
            self.fills = self.response['fills']
        if 'totalFilled' in self.response:
            self.totalFilled = self.response['totalFilled']
        if 'open' in self.response:
            self.orderOpen = self.response['open']


def __init__(self, account, venue, stock = ''):
    self.account = account
    self.venue = venue
    self.stock = stock

def main():

    account = ''
    venue = ''
    stock = ''

if __name__ == '__main__':
    main()
