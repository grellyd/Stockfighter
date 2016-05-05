import requests, heartbeat

api = 'https://api.stockfighter.io/ob/api'

def getVenueList():
    r = requests.get(api + '/venues')
    venues_json = r.json()
    venueList = []
    for venue_dict in venues_json['venues']:
        venue = venue_dict['venue']
        venueList.append(venue)
    return venueList

def getSymbolList(venue):
    r = requests.get(api + '/venues/' + venue + '/stocks')
    venue_json = r.json()
    symbolList = []
    for symbol_dict in venue_json['symbols']:
        symbol = symbol_dict['symbol']
        symbolList.append(symbol)
    return symbolList

def getAsks(venue, symbol):
    r = requests.get(api + '/venues/' + venue + '/stocks/' + symbol)
    symbol_json = r.json()
    askList = []
    asks = symbol_json['asks']
    if asks is not None:
        for ask_dict in asks:
            askList.append(ask_dict)
    return askList

def getBids(venue, symbol):
    r = requests.get(api + '/venues/' + venue + '/stocks/' + symbol)
    symbol_json = r.json()
    bidList = []
    bids = symbol_json['bids']
    if bids is not None:
        for bid_dict in bids:
            bidList.append(bid_dict)
    return bidList

def getFullTicker():
    if (heartbeat.noBeat()):
        print('The servers are down. Terminating...')
        exit()
    ticker = {}
    venuesList = getVenueList()
    symbolListDict = { }
    asksDictDict = { }
    bidsDictDict = { }
    for venue in venuesList:
        symbols = getSymbolList(venue)
        symbolListDict[venue] = symbols
        for symbol in symbols:
            asks = getAsks(venue, symbol)
            bids = getBids(venue, symbol)
            if asks:
                asksDictDict[symbol] = asks
            else:
                asksDictDict[symbol] = None
            if bids:
                bidsDictDict[symbol] = bids
            else:
                bidsDictDict[symbol] = None
    ticker['venuesList'] = venuesList
    ticker['symbolListDict'] = symbolListDict
    ticker['asksDictDict'] = asksDictDict
    ticker['bidsDictDict'] = bidsDictDict
    return ticker

def prettyPrint(ticker):
    venuesList = ticker['venuesList']
    if venuesList:
        for venue in venuesList:
            print('==========================')
            print('       ' + venue)
            print('==========================')
            symbolList = ticker['symbolListDict'][venue]
            if symbolList:
                for symbol in symbolList:
                    print('====================')
                    print('       ' + symbol)
                    print('====================')
                    print('====== ASKS ======')
                    asks = ticker['asksDictDict'][symbol]
                    if asks:
                        for ask in asks:
                                qty = ask['qty']
                                isBuy = ask['isBuy']
                                price = ask['price']
                                print("qty: " , qty)
                                print("isBuy: " , isBuy)
                                print("price: " , price)
                    else:
                        print("None")
                    print('====== BIDS ======')
                    bids = ticker['bidsDictDict'][symbol]
                    if bids:
                        for bid in bids:
                            qty = bid['qty']
                            isBuy = bid['isBuy']
                            price = bid['price']
                            print("qty: " , qty)
                            print("isBuy: " , isBuy)
                            print("price: " , price)
                    else:
                        print("None")
                    print('')
            else:
                print('SymbolList is NoneType')
            print('')
            print('')
    else:
        print('Venues is NoneType')
            
def getFirstStock():
    

if __name__ == "__main__":
    prettyPrint(getFullTicker())
