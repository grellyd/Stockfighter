import sys, requests, heartbeat

api = 'https://api.stockfighter.io/ob/api'
api_key = 'b59767ec5f0716b59c17054c0714f01802afe963'

def getFullTicker():
    if (heartbeat.noBeat()):
        print('The servers are down. Terminating...')
        exit()
    r = requests.get(api + '/venues')
    venues_json = r.json()
    print(r.text)
    for venue_dict in venues_json['venues']:
        venue = venue_dict['venue']
        r = requests.get(api + '/venues/' + venue )
        venue_json = r.json()
        for symbol_dict in venue_json['symbols']:
            symbol = symbol_dict['symbol']
            r = requests.get(api + '/venues/' + venue + '/stocks/' + symbol)
            symbol_json = r.json()
            print('========== ' + symbol + ' ==========')
            print('===== ASKS =====')
            print (symbol_json['asks'])
            print('===== BIDS =====')
            print (symbol_json['bids'])

def main():
    getFullTicker()
    r = requests.get(api + '/venues/TESTEX/stocks/FOOBAR')
    print(r.text)

if __name__ == "__main__":
    main()
