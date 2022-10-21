from csv import DictReader, writer
from collections import namedtuple
import os
from sys import argv
from googlesearch import search

in_csv = argv[1]
Politician = namedtuple('Politician', ['firstname', 'lastname', 'place', 'party'])

def get_politicians_info():
    with open(in_csv) as input_file:
        reader = DictReader(input_file)
        #writer = writer(output_file, 'w')
        all_politicians = []
        for row in reader:
            politician = Politician(row["voornaam"], row["achternaam"], row["werkingsgebiedLabel"], row["fractieNaam"])
            all_politicians.append(politician)
        unique_politicians = set(all_politicians)
        return unique_politicians

def parse_politicians(politicians):
    for politician in politicians:
        query = f"{politician.firstname} {politician.lastname} {politician.place} facebook".replace(' ', '+')
        print(query)
        finds=search(query, num=3, stop=3, lang="nl", pause=2)
        for find in finds:
            print(find)


politicians = get_politicians_info()
parse_politicians(politicians)
