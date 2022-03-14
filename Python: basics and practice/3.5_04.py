import requests
import json
import sys

CLIENT_ID = 'de170fa1347cd0c6c720'
CLIENT_SECRET = 'c136503c172afec2d0ee9ad19e96ed91'

requests_post = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                              data={
                                  "client_id": CLIENT_ID,
                                  "client_secret": CLIENT_SECRET
                              })
headers = {"X-Xapp-Token": json.loads(requests_post.text)["token"]}

line = [i.rstrip() for i in sys.stdin]
dict_artist = {}
for i in line:
    requests_get = requests.get(f"https://api.artsy.net/api/artists/{i}", headers=headers)
    json_loads = json.loads(requests_get.text)

    dict_artist[json_loads["sortable_name"]] = json_loads["birthday"]

for i in sorted(dict_artist.items(), key=lambda x: (x[1], x[0])):
    print(i[0])
