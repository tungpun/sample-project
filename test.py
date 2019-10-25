import req
import sys

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
