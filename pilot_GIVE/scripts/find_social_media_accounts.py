from csv import DictReader, writer
from collections import namedtuple
import os
from sys import argv
from googlesearch import search
from random import randint, random
from time import sleep
from uuid import uuid4

from facebook_scraper import get_profile

in_csv = argv[1]
wrong_words = ['/groups/', '/public/', '/videos/']
#Politician = namedtuple('Politician', ['name', 'ID', 'place', 'party'])

class Politician:
    def __init__(self, name, ID, place, party):
        self.name = name
        self.ID = ID
        self.place = place
        self.party = party

def get_politicians_info() -> set:
    """Parse the mandatendatabank CSV and store essential information in a set"""
    with open(in_csv) as input_file:
        reader = DictReader(input_file)
        all_politicians = []
        for row in reader:
            politician = Politician(row["volledige naam"], row['QID'], row["gemeente"], row["fractie"])
            if politician.ID == '':
                politician.ID = str(uuid4())
            print(politician.ID)
            all_politicians.append(politician)
        unique_politicians = set(all_politicians)
        return unique_politicians

def find_politician_profiles(set: Politician):
    """Find social media accounts via google with info from the politicians set"""
    for politician in politicians:
        for politician in politicians:
            platforms = ["twitter", "facebook"]
            for platform in platforms:
            # create the google query from our collection of politicians
                query = f"{politician.name} {politician.place} {platform}".replace(' ', '+')
                print(query)
                pause = randint(0,5) # random pause to have more human-like behaviour
                finds = search(query, num=3, stop=3, lang="nl", pause=pause) 
                finds = filter(lambda url: url.find(platform) >= 0, finds) 
                for find in finds:
                    get_account(find)
            sleep(random()) # let it sleep for random secs
        #TODO: verwijder ook de URL's met /public/ en /groups/ en ontdubbel de taalvarianten (nl-be, nl-nl, en-gb)
        #misschien dit al opslaan en de verschillende types facebook URL's opspliten


def get_account(url):
    for word in wrong_words:
        if word in url:
            print(f"{word} in {url}")
            return
    if '/people/' in url:
        identifier = url.split('/')[4]
    else:
        identifier = url.split('/')[3]
    print(identifier)
    



politicians = get_politicians_info()
find_politician_profiles(politicians)
