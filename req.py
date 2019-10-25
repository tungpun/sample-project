import requests

def send(url):
    r = requests.get(url, timeout=6)
    return r.url + " " + str(r.status_code)
    