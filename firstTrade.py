import sys, requests, heartbeat

api = 'https://api.stockfighter.io/ob/api'
api_key = 'b59767ec5f0716b59c17054c0714f01802afe963'

def getFullTicker():
    if (heartbeat.noBeat()):
        print('The servers are down. Terminating...')
        exit()
    r = requests.get(api + '/venues')
    venues_json = r.json()
    for venue_dict in venues_json['venues']:
        venue = venue_dict['venue']
        r = requests.get(api + '/venues/' + venue )
        venue_json = r.json()
        print('==========================')
        print('       ' + venue)
        print('==========================')
        for symbol_dict in venue_json['symbols']:
            symbol = symbol_dict['symbol']
            r = requests.get(api + '/venues/' + venue + '/stocks/' + symbol)
            symbol_json = r.json()
            print('====================')
            print('       ' + symbol)
            print('====================')
            print('====== ASKS ======')
            asks = symbol_json['asks']
            if asks is not None:
                for ask_dict in asks:
                    qty = ask_dict['qty']
                    isBuy = ask_dict['isBuy']
                    price = ask_dict['price']
                    print("qty: " , qty)
                    print("isBuy: " , isBuy)
                    print("price: " , price)
            else:
                print("None")
            print('====== BIDS ======')
            bids = symbol_json['bids']
            if bids is not None:
                for bid_dict in bids:
                    qty = bid_dict['qty']
                    isBuy = bid_dict['isBuy']
                    price = bid_dict['price']
                    print("qty: " , qty)
                    print("isBuy: " , isBuy)
                    print("price: " , price)
            else:
                print("None")
            print('')
        print('')
        print('')

def main():
    getFullTicker()
    r = requests.get(api + '/venues/TESTEX/stocks/FOOBAR')

if __name__ == "__main__":
    main()
