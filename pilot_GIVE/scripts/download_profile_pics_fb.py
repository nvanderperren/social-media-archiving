from csv import DictReader, writer
from collections import namedtuple
import os
from sys import argv
from googlesearch import search
import re
from random import randint, random
from time import sleep

in_csv = argv[1]
Politician = namedtuple('Politician', ['firstname', 'lastname', 'place', 'party'])

def get_politicians_info() -> set:
    """Parse the mandatendatabank CSV and store essential information in a set"""
    with open(in_csv) as input_file:
        reader = DictReader(input_file)
        all_politicians = []
        for row in reader:
            politician = Politician(row["voornaam"], row["achternaam"], row["werkingsgebiedLabel"], row["fractieNaam"])
            all_politicians.append(politician)
        unique_politicians = set(all_politicians)
        return unique_politicians

def find_politician_profiles(set: politicians):
    """Find social media accounts via google with info from the politicians set"""
    for politician in politicians:
        for politician in politicians:
            platforms = ["twitter", "facebook", "instagram"]
            for platform in platforms:
            # create the google query from our collection of politicians
                query = f"{politician.firstname} {politician.lastname} {politician.place} {platform}".replace(' ', '+')
                print(query)
                pause = randint(0,5) # random pause to have more human-like behaviour
                finds = search(query, num=3, stop=3, lang="nl", pause=pause) 
                finds = filter(lambda url: url.find(platform) >= 0, finds) 
                for find in finds:
                    print(find)
            sleep(random()) # let it sleep for random secs
        #TODO: verwijder ook de URL's met /public/ en /groups/ en ontdubbel de taalvarianten (nl-be, nl-nl, en-gb)
        #misschien dit al opslaan en de verschillende types facebook URL's opspliten


politicians = get_politicians_info()
find_politician_profiles(politicians)
