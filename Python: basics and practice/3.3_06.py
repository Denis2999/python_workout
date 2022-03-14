import requests
import re


def links_from(some_link):
    res = requests.get(some_link)
    urls_list = re.findall(r'(https?://[^\"\s>]+)', str(res.content))
    return urls_list


link_1, link_2 = [input() for i in range(2)]

links_list = links_from(link_1)

required_links = []
for i in links_list:
    required_links.extend(links_from(i))

if link_2 in required_links:
    print("Yes")
else:
    print("No")
