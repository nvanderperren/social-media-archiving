#!usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, datetime
from facebook_scraper import get_posts
from json import dumps, JSONEncoder
from sys import argv
from argparse import ArgumentParser

class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (date, datetime)):
            return str(o)
        else:
            return super().default(o)


def write_urls(urls, account, crawler):
    today = date.today().strftime("%Y%m%d")
    with open("{}_{}_urls.txt".format(today, account), 'w') as output_file:
        for url in urls:
            if crawler == 'wget':
                output_file.write(url)
                output_file.write("\n")
            else:
                output_file.write('      - ' + url)
                output_file.write("\n")
    output_file.close()

def get_fb_urls(args):
    posts = []
    urls = []
    account = args.account
    crawler = args.crawler
    cookies = None
    
    if args.cookies:
        cookies = args.cookies

    if args.group:
        posts = get_posts(group=account, cookies=cookies)
    else:
        posts = get_posts(account=account, cookies=cookies)

    for post in posts:
        urls.append(post['post_url'])

    write_urls(urls, account, crawler)

parser = ArgumentParser()
parser.add_argument('--account', '-a', help="name of the account", required=True)
parser.add_argument('--cookies', help="cookie file for getting data of a private account", required=False)
parser.add_argument('--group', help="account is a group", action='store_true')
parser.add_argument('--crawler', choices=['browsertrix', 'wget'], required=True)
args = parser.parse_args()
get_fb_urls(args)