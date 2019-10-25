import req
import sys


url = "http://example.com"

if len(sys.argv) > 1:
    url = sys.argv[1]
    print("Loaded url")

res = req.send(url)
print(res)