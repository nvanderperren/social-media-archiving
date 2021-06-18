from argparse import ArgumentParser
from datetime import date, datetime
from facebook_scraper import get_posts
from json import dumps, JSONEncoder
from sys import argv

class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (date, datetime)):
            return str(o)
        else:
            return super().default(o)

def write_posts(account, posts):
    today = date.today().strftime("%Y%m%d")
    with open("{}_{}_facebook.jsonl".format(today, account), 'w') as output_file:
        for post in posts:
            output_file.write(dumps(post, cls=DateTimeEncoder))
            output_file.write("\n")
    output_file.close()

def get_fb_posts(args):
    account = args.account
    reactions = args.reactions
    comments = args.comments
    cookies = None
    if args.cookies:
        cookies = args.cookies
    if args.group:
        posts = get_posts(group=account, cookies=cookies, options={"comments": comments, "reactors": reactions})
    else:
        posts = get_posts(account=account, cookies=cookies, options={"comments": comments, "reactors": reactions})
    write_posts(account, posts)


parser = ArgumentParser()
parser.add_argument('--account', '-a', help="name of the account", required=True)
parser.add_argument('--cookies', help="cookie file for getting data of a private account", required=False)
parser.add_argument('--reactions', help="extract likes and so from posts", action='store_true')
parser.add_argument('--comments', help="scrape comments too", action='store_true')
parser.add_argument('--group', help="account is a group", action='store_true')
args = parser.parse_args()
get_fb_posts(args)