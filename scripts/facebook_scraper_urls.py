#!usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, datetime
from facebook_scraper import get_posts
from json import dumps, JSONEncoder
from sys import argv

account = str(argv[1])
today = date.today().strftime("%Y%m%d")
posts = []

class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (date, datetime)):
            return str(o)
        else:
            return super().default(o)

if len(argv) == 3:
    cookies = str(argv[2])
    posts = get_posts(account=account, cookies=cookies)
elif len(argv) == 2:
    posts = get_posts(account=account)
else:
    print("ERROR only cookie argument is allowed")

with open("{}_{}_facebook.txt".format(today, account), 'w') as output_file:
    for post in posts:
        output_file.write('      - ' + post['post_url'])
        output_file.write("\n")
output_file.close()
