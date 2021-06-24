#!usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nastasia Vanderperren
#
# get posts of a fb page, group or account
# returns a json lines files with a line for each post
#

from argparse import ArgumentParser
from datetime import date, datetime
from facebook_scraper import get_posts
from json import dumps, JSONEncoder

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
            del post['text']
            output_file.write(dumps(post, cls=DateTimeEncoder, ensure_ascii=False))
            output_file.write("\n")
    output_file.close()

def get_fb_posts(args):
    account = args.account
    reactions = args.reactions
    comments = args.comments
    pages = args.pages
    cookies = None
    if args.cookies:
        cookies = args.cookies
    if args.group:
        posts = get_posts(group=account, cookies=cookies, pages=pages, options={"comments": comments, "reactors": reactions})
    else:
        posts = get_posts(account=account, cookies=cookies, pages=pages, options={"comments": comments, "reactors": reactions})
    write_posts(account, posts)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('account', help="name of the account", type=str)
    parser.add_argument('--cookies', help="cookie file for getting data of a private account", required=False)
    parser.add_argument('--reactions', help="extract likes and so from posts", action='store_true')
    parser.add_argument('--comments', help="scrape comments too", action='store_true')
    parser.add_argument('--group', help="account is a group", action='store_true')
    parser.add_argument('--pages', help="number of pages to scrape", type=int, default=10)
    args = parser.parse_args()
    get_fb_posts(args)