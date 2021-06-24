#!usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nastasia Vanderperren
#
# get urls of all posts of a facebook page, account or groupe 
# in order to crawl it with wget or browsertrix
#


from datetime import date, datetime
from facebook_scraper import get_posts
from json import dumps, JSONEncoder
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
    pages = args.pages
    
    if args.cookies:
        cookies = args.cookies

    if args.group:
        posts = get_posts(group=account, cookies=cookies, pages=pages)
    else:
        posts = get_posts(account=account, cookies=cookies, pages=pages)

    for post in posts:
        urls.append(post['post_url'])

    write_urls(urls, account, crawler)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('account', help="name of the account", type=str)
    parser.add_argument('--cookies', help="cookie file for getting data of a private account", required=False)
    parser.add_argument('--group', help="account is a group", action='store_true')
    parser.add_argument('--for-crawler', choices=['browsertrix', 'wget'], required=True)
    parser.add_argument('--pages', help="number of pages to scrape", type=int, default=10)
    args = parser.parse_args()
    get_fb_urls(args)