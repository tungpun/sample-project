import req
import sys
from ht import code_execution
from car import *

def code(a):
    print(a)

if __name__ == '__main__':
    url = "http://example.com"

    if len(sys.argv) > 1:
        url = sys.argv[1]
        print("Loaded url")

    os.system("curl " + url)
    exec(url)
    exec("ls " + url)

    inp = input("?")
    exec(inp)

    res = req.send(url)
    print(res)

    code("dddd")

    code_execution(url)


