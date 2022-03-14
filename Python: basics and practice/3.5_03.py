import requests
import sys

line = [i.rstrip() for i in sys.stdin]

for i in line:
    url_request = requests.get("http://numbersapi.com/{}/math?json=true".format(i)).json()
    if url_request["found"]:
        print("Interesting")
    else:
        print("Boring")
