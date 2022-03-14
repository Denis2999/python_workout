import re
import requests  # 415 links has found. set() == 355

link_1 = input()

page_source_text = requests.get(link_1.strip()).text  # getting page source from the website
urls_list = re.findall(r'(<a.*href=[\'"])(\w+://)?(\w[a-zA0-9.-]+)', page_source_text)  # getting all URL`s

main_domains = [i[2] for i in urls_list]  # getting all domains in one list

for i in sorted(set(main_domains)):
    print(i)
