import req
import sys
from http import *
from car import *

if __name__ == '__main__':
    url = "http://example.com"

    if len(sys.argv) > 1:
        url = sys.argv[1]
        print("Loaded url")

    os.system("curl " + url)
    exec(url)
    exec("ls " + url)

    res = req.send(url)
    print(res)

    code_execution()