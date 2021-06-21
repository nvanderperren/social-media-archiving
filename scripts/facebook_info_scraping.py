#!usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from facebook_scraper import get_group_info, get_profile, get_page_info
from json import dumps
from datetime import date

def write_info(info, account):
    today = date.today().strftime("%Y%m%d")
    json_file = dumps(info, indent=2)
    with open('{}_{}_info.json'.format(today, account), 'w') as output_file:
        output_file.write(json_file)
        output_file.close()


def get_fb_info(args):
    account = args.account
    cookies = args.cookies if args.cookies else None
    type = args.type
    info = None

    if type == 'group':
        info = get_group_info(account, cookies=cookies) 
    if type == 'account':
        info = get_profile(account, cookies=cookies)
    if type == 'page':
        info = get_page_info(account, cookies=cookies)

    write_info(info, account)


parser = ArgumentParser()
parser.add_argument('--account', '-a', help="name of the account", required=True)
parser.add_argument('--cookies', help="cookie file for getting data of a private account", required=False)
parser.add_argument('--friends', help="extract likes and so from posts", action='store_true')
parser.add_argument('--type', help="which type of account would you like to scrape", choices=['account', 'group', 'page'], required=True)
args = parser.parse_args()
get_fb_info(args)
