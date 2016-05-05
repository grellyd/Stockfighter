import requests

def getStatus():
    r = requests.get('https://api.stockfighter.io/ob/api/heartbeat')
    return r

def noBeat():
    # assume up by default
    serverDown = False
    r = getStatus()
    try:
        r.raise_for_status()
    except http_error:
        serverDown = True
    return serverDown

def status():
    r = getStatus()
    if (r.status_code == requests.codes.ok):
        print("Starfighter is at full warp!")
    else:
        print("Starfigher has crashed!")
        r.raise_for_status()


if __name__ == "__main__":
    status()
