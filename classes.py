from enum import Enum

class OrderType(Enum):
    limit = 'limit'
    market = 'market'
    fillkill = 'fill-or-kill'
    immed = 'immediate-or-cancel'

class OrderDirection(Enum):
    buy = 'buy'
    sell = 'sell'
