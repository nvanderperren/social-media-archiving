from argparse import ArgumentParser
from datetime import date, datetime
from facebook_scraper import get_posts
from json import dumps, JSONEncoder
from sys import argv

cookies = str(argv[2])
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
    posts = get_posts(account=account, cookies=cookies)
elif len(argv) == 2:
    posts = get_posts(account=account)
else:
    print("ERROR only cookie argument is allowed")

with open("{}_{}_facebook.jsonl".format(today, account), 'w') as output_file:
    for post in posts:
        output_file.write(dumps(post, cls=DateTimeEncoder))
        output_file.write("\n")
output_file.close()

'''
parser = ArgumentParser()
parser.add_argument('-- acount', '-a', help="name of the account", required=True)
parser.add_argument('--cookies', help="cookie file for getting data of a private account", required=False)
'''